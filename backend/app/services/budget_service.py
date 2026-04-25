from app.repositories.budget_repo import BudgetRepository
from app.repositories.expense_repo import ExpenseRepository

class BudgetService:
    def __init__(self, db):
        self.repo = BudgetRepository(db=db)
        self.expense_repo = ExpenseRepository(db)
    
    def set_budget(self, user_id, category_id, amount):
        return self.repo.create_or_update(user_id, category_id, amount)
    
    def check_budget_beach(self, user_id):
        budgets = self.repo.get_by_user(user_id=user_id)

        summaries = self.expense_repo.category_summary(user_id)

        summary_map = {s.category_id: s.total for s in summaries}

        alerts = []

        for b in budgets:
            spent = summary_map.get(b.category_id, 0)

            if spent > b.amount:
                alerts.append({
                    "category_id": b.category_id,
                    "budget": b.amount,
                    "spent": spent
                })
        
        return alerts