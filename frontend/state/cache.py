import streamlit as st


class Cache:

    @staticmethod
    @st.cache_data(ttl=60)
    def get_categories(client):
        return client.get_categories()

    @staticmethod
    @st.cache_data(ttl=60)
    def get_summary(client):
        return client.get_category_summary()

    @staticmethod
    @st.cache_data(ttl=60)
    def get_trend(client):
        return client.get_daily_trend()