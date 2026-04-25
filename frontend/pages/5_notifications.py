import streamlit as st
from services.notification_client import NotificationClient

st.title("🔔 Notifications")

notifications = NotificationClient.get_notifications()

for n in notifications:
    st.info(f"{n['message']} ({n['type']})")