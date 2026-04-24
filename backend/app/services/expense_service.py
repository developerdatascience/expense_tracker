from app.repositories.expense_repo import ExpenseRepository

class ExpenseService:

    def __init__(self, db):
        self.expense_repo = ExpenseRepository(db)
    
    def add_expense(self, user_id, expense_data):
        expense_data["user_id"] = user_id
        return self.expense_repo.create(expense_data)
    
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