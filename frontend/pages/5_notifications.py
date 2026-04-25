import streamlit as st

st.title("🔔 Notification")

notifications = [
    "⚠️ Budget exceeds for food",
    "💡 You spent 30% more this week",
    "📆 Electricity bill due tomorrow"
]

for note in notifications:
    st.info(note)