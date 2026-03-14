🎓 AI Student Performance Analytics Platform

An AI-powered web application that predicts student math scores and provides interactive analytics dashboards to understand academic performance patterns.

The system uses machine learning models trained on student performance data to analyze relationships between different academic factors and predict student outcomes.

🚀 Live Demo

🔗 Access the deployed application here

👉 https://ai-student-performance-kagaxfmtgwugvkjwqkyfrz.streamlit.app/

📌 Project Overview

The AI Student Performance Analytics Platform is designed to analyze and predict student academic performance using machine learning.

The application allows users to input student academic attributes and predict the Math Score based on learned patterns from historical data.

The system also provides interactive visualizations that help users explore performance trends and insights.

✨ Key Features

🎯 Predict Student Math Scores using Machine Learning

📊 Interactive analytics dashboard

📈 Data visualization using Plotly

🔐 User authentication system

🕓 Prediction history tracking

📥 Download prediction results

🌐 Web application built using Streamlit

🧠 Machine Learning Models

The following machine learning models were implemented and evaluated:

Model	Description
Linear Regression	Predicts scores using linear relationships
Decision Tree	Captures nonlinear patterns and decision rules
Random Forest	Ensemble learning method for improved accuracy
Model Performance
Model	MSE	R² Score
Linear Regression	30.28	0.87
Decision Tree	71.54	0.69
Random Forest	35.82	0.84

✅ Linear Regression achieved the best performance with the highest R² score.

📊 Input Features

The prediction model uses the following inputs:

📖 Reading Score

✍️ Writing Score

👩‍🎓 Gender

🍱 Lunch Type

Output

🎯 Predicted Math Score

🛠 Tech Stack
Programming Language

Python

Framework

Streamlit

Machine Learning

Scikit-learn

Data Processing

Pandas

NumPy

Visualization

Plotly

Database

SQLite

Version Control

Git & GitHub

📂 Project Structure
AI-Student-Performance
│
├── app.py
├── model.pkl
├── dataset
│   └── StudentsPerformance.csv
├── requirements.txt
├── README.md
└── database.db
▶️ Run the Project Locally

If you want to run the project on your own system, follow these steps.

1️⃣ Clone the Repository
git clone https://github.com/anuskagupta123/AI-Student-Performance.git
2️⃣ Navigate to the Project Folder
cd AI-Student-Performance
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the Streamlit Application
streamlit run app.py

The application will open in your browser.

📈 Example Prediction
Input

Reading Score: 75
Writing Score: 80
Gender: Female
Lunch Type: Standard

Output

🎯 Predicted Math Score: 78

The prediction is generated using the trained machine learning model based on patterns learned from the dataset.

📊 Dataset

This project uses the Students Performance Dataset, which contains academic scores and demographic factors of students.

Dataset attributes include:

Gender

Reading Score

Writing Score

Math Score

Lunch Type

Test Preparation Course

Parental Level of Education

👩‍💻 Author

Anuska Gupta
Computer Science Student | Machine Learning Enthusiast

🔗 GitHub
https://github.com/anuskagupta123

⭐ Future Improvements

Add deep learning models

Improve model accuracy

Add teacher/admin analytics dashboards

Add more academic features

Deploy using Docker and cloud infrastructure