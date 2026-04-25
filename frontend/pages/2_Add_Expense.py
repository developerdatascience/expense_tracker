import streamlit as st
from services.expense_client import ExpenseClient


st.title("Add Expense")

with st.form("expense_form"):
    amount = st.number_input("Amount")
    description = st.text_input("Description")
    category_id = st.number_input("Category ID")
    payment_method = st.selectbox("Payment Method", ["Cash", "Card", "UPI"])

    submitted = st.form_submit_button("Submit")

    if submitted:
        data = {
            "amount": amount,
            "description": description,
            "category_id": category_id,
            "payment_method": payment_method
        }
        response = ExpenseClient.add_expense(data=data)
        st.success("Expense added", icon="🔥")