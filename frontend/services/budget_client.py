from services.api_client import APIClient


class BudgetClient:

    @staticmethod
    def set_budget(category_id, amount):
        return APIClient.post(f"/budgets/?category_id={category_id}&amount={amount}")
    
    @staticmethod
    def get_alerts():
        return APIClient.get("/budgets/alerts").json()