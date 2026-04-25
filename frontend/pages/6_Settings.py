import streamlit as st
from services.category_client import CategoryClient
from services.budget_client import BudgetClient

st.title("⚙ Settings - Budgets")

categories = CategoryClient.get_categories()
cat_map = {c["name"]: c["id"] for c in categories}

category = st.selectbox("Category", list(cat_map.keys()))
amount = st.number_input("Monthly Budget")

if st.button("Set Budget"):
    BudgetClient.set_budget(cat_map[category], amount)
    st.success("Budget set!")