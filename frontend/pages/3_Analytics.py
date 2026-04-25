import streamlit as st
from services.expense_client import ExpenseClient
from components.charts import pie_charts

st.title("Analytics")

data = ExpenseClient.get_category_summary()

pie_charts(data)