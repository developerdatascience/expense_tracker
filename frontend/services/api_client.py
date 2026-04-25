import requests
from state.session_manager import SessionManager

BASE_URL = "https://localhost:8000"

class APIClient:

    @staticmethod
    def get_headers():
        token = SessionManager.get_token()
        return {
            "Authorization": f"Bearer {token}"
        } if token else {}
    
    @staticmethod
    def get(endpoint):
        return requests.get(f"{BASE_URL}{endpoint}", headers=APIClient.get_headers())
    
    @staticmethod
    def post(endpoint, json=None):
        return requests.post(f"{BASE_URL}{endpoint}", json=json, headers=APIClient.get_headers())

    @staticmethod
    def delete(endpoint):
        return requests.delete(f"{BASE_URL}{endpoint}", headers=APIClient.get_headers())