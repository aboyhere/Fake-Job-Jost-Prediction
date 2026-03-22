import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download once
nltk.download('stopwords')
nltk.download('wordnet')

# Load model and vectorizer
model = pickle.load(open("fakejob_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidfvectorizer.pkl", "rb"))

# Preprocessing setup
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    words = text.split()
    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]
    return " ".join(words)

# UI Title
st.title("💼 Fake Job Detection System")
st.write("Fill the job details below to check if it's real or fake.")

# User Inputs
title = st.text_input("Job Title")
company_profile = st.text_area("Company Profile")
description = st.text_area("Job Description")
requirements = st.text_area("Requirements")
benefits = st.text_area("Benefits")

# Predict Button
if st.button("🔍 Predict"):

    # 🔴 Basic Validation
    if not title or not description:
        st.warning("⚠ Please fill at least Job Title and Description")
    
    else:
        # 🟡 Handle missing optional fields
        if not company_profile:
            company_profile = "no company profile"
        if not requirements:
            requirements = "no requirements"
        if not benefits:
            benefits = "no benefits"

        # 🔵 Combine all text
        full_text = (
            title + " " +
            company_profile + " " +
            description + " " +
            requirements + " " +
            benefits
        )

        # 🔴 Small input warning
        if len(full_text.split()) < 20:
            st.warning("⚠ Please provide more details for better prediction")

        # 🔵 Clean text
        cleaned = clean_text(full_text)

        # 🔵 Vectorize
        vector = vectorizer.transform([cleaned])

        # 🔵 Predict
        prediction = model.predict(vector)[0]
        probability = model.predict_proba(vector)[0][1]

        # 🔥 Show Result
        if prediction == 1:
            st.error(f"⚠ This job post might be FAKE (Confidence: {probability:.2f})")
        else:
            st.success(f"✅ This job post looks REAL (Confidence: {1 - probability:.2f})")

        # 🔍 Suspicious keyword check
        suspicious_words = ["earn", "money", "easy", "home", "quick", "income"]
        if any(word in full_text.lower() for word in suspicious_words):
            st.warning("⚠ Suspicious keywords detected in the job post")