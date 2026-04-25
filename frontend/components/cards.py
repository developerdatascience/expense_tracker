import streamlit as st

def kpi_card(title, value, delta=None):
    st.metric(
        label=title,
        value=f"₹ {value}",
        delta=delta
    )