import streamlit as st
from services.expense_client import ExpenseClient
from components.charts import pie_chart, line_chart
from components.cards import kpi_card
from state.cache import Cache

st.title("Dashboard")

expenses = ExpenseClient.get_expenses()
category_summary = Cache.get_summary(ExpenseClient)
daily_trend = Cache.get_trend(ExpenseClient)

total_spend = sum([e["amount"] for e in expenses]) if expenses else 0
monthly_spend = total_spend

col1, col2, col3 = st.columns(3)

with col1:
    kpi_card("Total Spend", total_spend)

with col2:
    kpi_card("Monhtly Spend", monthly_spend)

with col3:
    kpi_card("Transactions", len(expenses))

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Category Distribution")
    pie_chart(category_summary)

with col2:
    st.subheader("Daily Spending Trend")
    line_chart(daily_trend)

st.divider()

st.subheader("Recent Transactions")
st.dataframe(expenses)
