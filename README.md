# Fake Job Prediction using Machine Learning
Fake job postings are increasing day by day, leading to scams and fraud.
This project aims to detect whether a job posting is real or fake using Machine Learning.


🎯 Objective
To build a classification model that predicts:
✅ Real Job
❌ Fake Job

📊 Dataset
Contains job descriptions, company details, requirements, etc.
Includes labeled data (real vs fake)
🛠️ Technologies Used
Python 🐍
Pandas
NumPy
Scikit-learn
Streamlit (for web app)
🔄 Project Workflow
1. Data Preprocessing
Handling missing values
Removing unnecessary columns
Text cleaning
2. Feature Engineering
Converted text data into numerical format using:
TF-IDF Vectorizer
3. Model Building
Used classification algorithms like:
Logistic Regression
Naive Bayes
4. Model Evaluation
Accuracy
Precision
Recall
F1-score
📈 Results
Achieved good accuracy in detecting fake job postings
Model can generalize well to new data
💻 Streamlit App
User inputs job description
Model predicts whether job is:
Real or Fake
▶️ How to Run the Project
git clone https://github.com/your-username/fake-job-prediction.git
cd fake-job-prediction
pip install -r requirements.txt
streamlit run app.py
📌 Future Improvements
Improve accuracy using advanced models
Deploy using cloud (AWS / Render)
Add more real-time datasets
🙌 Conclusion

This project helps in identifying fraudulent job postings and can be useful for job seekers to avoid scams.
