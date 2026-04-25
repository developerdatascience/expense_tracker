from app.repositories.expense_repo import ExpenseRepository
from app.services.notification_service import NotificationService
from app.services.budget_service import BudgetService

class ExpenseService:

    def __init__(self, db):
        self.expense_repo = ExpenseRepository(db)
    
    def add_expense(self, user_id, expense_data):
        expense_data["user_id"] = user_id
        expense = self.expense_repo.create(expense_data)

        budget_service = BudgetService(self.expense_repo.db)
        notif_service = NotificationService(self.expense_repo.db)

        alerts = budget_service.check_budget_beach(user_id)

        for alert in alerts:
            notif_service.create(
                user_id=user_id,
                message=f"Budget exceeded for category {alert['category_id']}",
                type_="budget_alert"
                )

        return expense
    
    def list_expenses(self, user_id, skip=0, limit=100):
        return self.expense_repo.get_all(user_id, skip, limit)
    
    def filter_expenses(self, user_id, filters):
        return self.expense_repo.filter(user_id, **filters)
    
    def get_category_summary(self, user_id):
        return self.expense_repo.category_summary(user_id)
    
    def get_daily_trend(self, user_id):
        return self.expense_repo.daily_trend(user_id)

    def get_monthly_summary(self, user_id):
        return self.expense_repo.get_monthly_summary(user_id)