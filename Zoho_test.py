import streamlit as st
import psycopg2

Jk = psycopg2.connect(user = "postgres", password = "Jaya9698", host = "localhost", port = 5432, database = "Zohotest")

x = Jk.cursor()

st.markdown("<h1 style=color:orange> Registration Login Page <h1>", unsafe_allow_html = True)


tab1, tab2 = st.tabs(["Login page", "New user registration"])

with tab1:

    users = st.text_input("Enter user name")

    user_password = st.text_input("Enter your password")

    Login = st.button("Login")

    if Login:
        info = x.execute("SELECT * FROM user_list WHERE user_name = users AND passwords = user_password;")
        st.write(info)
        

with tab2:
    Name = st.text_input("Full Name")
    DOY = st.text_input("Year of birth")
    Age = st.text_input("Age")
    contact = st.text_input("Mobile Number")
    mailid = st.text_input("Mail ID")
    User = st.text_input("User name")
    passwords = st.text_input("Password")
    select = st.button("Register now")

    if select:
        x.execute("INSERT into user_list VALUES (user, passwords, Age, DOY, contact, mailid);")
        Jk.commit()