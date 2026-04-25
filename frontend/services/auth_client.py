from services.api_client import APIClient

class AuthClient:

    @staticmethod
    def login(email: str, password: str):
        response = APIClient.post("/auth/login", {
            "email": email,
            "password": password
        })

        return response.json()
    
    @staticmethod
    def regiser(email: str, username: str, password: str):
        response = APIClient.post("/auth/register", {
            "email": email,
            "username": username,
            "password": password    
        })
        return response.json()
    