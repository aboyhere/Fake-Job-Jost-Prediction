# Fake Job Prediction using Machine Learning
Fake job postings are increasing day by day, leading to scams and fraud.
This project aims to detect whether a job posting is real or fake using Machine Learning.

The goal is simple: take job-related information and predict if it is genuine or fraudulent.

### 🔍 How it works

The project follows a basic machine learning pipeline:

 * Cleaned the dataset by handling missing values
 * Processed text data (job descriptions, requirements)
 * Converted text into numbers using TF-IDF
 * Trained models like Logistic Regression and Naive Bayes
 * Evaluated performance using accuracy, precision, recall
  
 ### 📊 Why this matters

Detecting fake jobs is important because:

  It helps users avoid scams
  Improves trust in job platforms
  Saves time and effort for job seekers
💻 Application

  I built a simple Streamlit app where:
  
  User enters job details
  Model predicts → Real or Fake
🚀 Result
  
  The model performs well in identifying fake job postings and can be used as a basic tool for filtering suspicious listings.
