import streamlit as st
import pandas as pd
import pickle
import sqlite3
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

from auth import login_signup
from database import create_db, save_prediction

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Student AI Analytics",
    page_icon="🎓",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------

model = pickle.load(open("model.pkl", "rb"))
features = pickle.load(open("features.pkl", "rb"))

# ---------------- CREATE DATABASE ----------------

create_db()

# ---------------- SESSION STATE ----------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- TITLE ----------------

st.title("🎓 Student Performance AI Platform")

# ---------------- LOGIN PAGE ----------------

if not st.session_state.logged_in:
    login_signup()

else:

    # ---------------- SIDEBAR ----------------

    st.sidebar.success(f"Logged in as {st.session_state.user}")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    page = st.sidebar.radio(
        "Navigation",
        ["🏠 Dashboard", "📊 Predict Score", "📜 Prediction History", "📈 Analytics", "ℹ About"]
    )

    # ---------------- DASHBOARD ----------------

    if page == "🏠 Dashboard":

        st.header("Platform Overview")

        try:
            df = pd.read_csv("exams.csv")
        except:
            st.error("Dataset not found.")
            st.stop()

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Students", df.shape[0])
        col2.metric("Features", df.shape[1])
        col3.metric("Avg Math Score", round(df["math score"].mean(), 2))
        col4.metric("Max Math Score", df["math score"].max())

        st.subheader("Dataset Preview")
        st.dataframe(df.head(10), use_container_width=True)

        # ---------------- MODEL COMPARISON ----------------

        st.subheader("Machine Learning Model Comparison")

        results = pd.DataFrame({
            "Model": ["Linear Regression", "Decision Tree", "Random Forest"],
            "MSE": [30.28, 71.54, 35.82],
            "R2 Score": [0.8706, 0.6943, 0.8469]
        })

        st.dataframe(results, use_container_width=True)

        fig = px.bar(
            results,
            x="Model",
            y="R2 Score",
            title="Machine Learning Model Comparison (R² Score)"
        )

        st.plotly_chart(fig, use_container_width=True)

        best_model = results.loc[results["R2 Score"].idxmax()]

        st.success(
            f"🏆 Best Model: **{best_model['Model']}** with R² Score **{best_model['R2 Score']:.2f}**"
        )

    # ---------------- PREDICTION ----------------

    elif page == "📊 Predict Score":

        st.header("Predict Student Math Score")

        col1, col2 = st.columns(2)

        with col1:
            reading = st.slider("Reading Score", 0, 100, 60)
            writing = st.slider("Writing Score", 0, 100, 60)

        with col2:
            gender = st.selectbox("Gender", ["male", "female"])
            lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])

        input_df = pd.DataFrame(columns=features)
        input_df.loc[0] = 0

        input_df["reading score"] = reading
        input_df["writing score"] = writing
        input_df[f"gender_{gender}"] = 1
        input_df[f"lunch_{lunch}"] = 1

        if st.button("Predict Score"):

            prediction = model.predict(input_df)[0]

            st.success(f"🎯 Predicted Math Score: {prediction:.2f}")

            save_prediction(
                st.session_state.user,
                reading,
                writing,
                prediction
            )

            fig = px.bar(
                x=["Predicted Score"],
                y=[prediction],
                labels={"x": "Result", "y": "Score"},
                title="Prediction Result"
            )

            st.plotly_chart(fig)

    # ---------------- HISTORY ----------------

    elif page == "📜 Prediction History":

        st.header("Your Prediction History")

        conn = sqlite3.connect("student.db")

        query = "SELECT * FROM predictions WHERE username=?"

        df = pd.read_sql_query(
            query,
            conn,
            params=(st.session_state.user,)
        )

        conn.close()

        if df.empty:
            st.info("No predictions yet.")
        else:

            st.dataframe(df, use_container_width=True)

            csv = df.to_csv(index=False)

            st.download_button(
                "Download Predictions",
                csv,
                "predictions.csv",
                "text/csv"
            )

    # ---------------- ANALYTICS ----------------

    elif page == "📈 Analytics":

        st.header("Student Performance Analytics")

        df = pd.read_csv("exams.csv")

        col1, col2 = st.columns(2)

        with col1:

            fig = px.scatter(
                df,
                x="reading score",
                y="math score",
                title="Reading vs Math Score"
            )

            st.plotly_chart(fig)

        with col2:

            fig = px.scatter(
                df,
                x="writing score",
                y="math score",
                title="Writing vs Math Score"
            )

            st.plotly_chart(fig)

        st.subheader("Subject Correlation")

        corr = df[['math score', 'reading score', 'writing score']].corr()

        fig2, ax = plt.subplots()

        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)

        st.pyplot(fig2)

    # ---------------- ABOUT ----------------

    elif page == "ℹ About":

        st.header("About the Project")

        st.write("""
        **Student Performance AI Platform**

        This platform predicts student math performance using machine learning.

        **Technologies Used**

        - Python  
        - Scikit-learn  
        - Streamlit  
        - SQLite  
        - Plotly  

        **Machine Learning Models Compared**

        - Linear Regression  
        - Decision Tree  
        - Random Forest  

        **Features**

        - AI score prediction  
        - Interactive analytics dashboard  
        - User authentication  
        - Prediction history  
        - Download reports  
        """)