import streamlit as st
from services.auth_client import AuthClient
from state.session_manager import SessionManager

st.set_page_config(page_title="Expense Tracker", 
                   page_icon="💰", 
                   layout="wide", 
                   initial_sidebar_state="expanded")

def login_page():
    st.title("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        response = AuthClient.login(email, password)

        if "access_token" in response:
            SessionManager.set_token(response["access_token"])
            st.rerun()
        else:
            st.error("Invalid credentials")


def register_page():
    st.title("Register")

    email = st.text_input(label="Email")
    username = st.text_input(label="Username")
    password = st.text_input(label="Password", type="password")

    if st.button("Register"):
        response = AuthClient.regiser(email=email, username=username, password=password)
        st.success(body="User created. Please Login!!", icon="✅")
    
    if not SessionManager.is_authenticated():
        tab1, tab2 = st.tabs(["Login", "Register"])
        with tab1:
            login_page()
        with tab2:
            register_page()
        
    
    else:
        st.sidebar.title("Navigation")
        st.sidebar.page_link("pages/1_Dashboard.py", label="Dashboard")
        st.sidebar.page_link("pages/2_Add_Expense.py", label="Add Expense")
        st.sidebar.page_link("pages/3_Analytics.py", label="Analytics")

        if st.sidebar.button("Logout"):
            SessionManager.logout()
            st.rerun()

