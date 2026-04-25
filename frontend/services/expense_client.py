from services.api_client import APIClient


class ExpenseClient:

    @staticmethod
    def add_expense(data):
        return APIClient.post("/expenses/", json=data).json()
    
    @staticmethod
    def get_category_summary():
        return APIClient.get("/expenses/summary/category").json()
    
    @staticmethod
    def get_expenses():
        return APIClient.get("/expenses/").json()
    
    @staticmethod
    def get_daily_trend():
        return APIClient.post("/expenses/summary/daily").json()