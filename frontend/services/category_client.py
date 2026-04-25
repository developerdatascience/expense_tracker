from services.api_client import APIClient

class CategoryClient:

    @staticmethod
    def get_categories():
        return APIClient.get("/categories/").json()
    
    