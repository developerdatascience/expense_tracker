import streamlit as st

class SessionManager:

    @staticmethod
    def set_token(token: str):
        """Set the authentication token in session state"""
        st.session_state["token"] = token
    
    @staticmethod
    def get_token():
        """Get the authentication token from session state"""
        return st.session_state.get("token")
    
    @staticmethod
    def is_authenticated():
        """Check if the user is authenticated"""
        return "token" in st.session_state
    
    @staticmethod
    def logout():
        """Logout the user by clearing the session state"""
        st.session_state.clear()

    
