import streamlit as st
from database import add_user, login_user

def login_signup():

    menu = ["Login","Signup"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Signup":

        st.subheader("Create Account")

        new_user = st.text_input("Username")
        new_pass = st.text_input("Password",type="password")

        if st.button("Signup"):
            add_user(new_user,new_pass)
            st.success("Account Created!")

    if choice == "Login":

        st.subheader("Login")

        username = st.text_input("Username")
        password = st.text_input("Password",type="password")

        if st.button("Login"):
            result = login_user(username,password)

            if result:
                st.session_state.logged_in = True
                st.session_state.user = username
                st.success("Logged in successfully")
            else:
                st.error("Incorrect username/password")