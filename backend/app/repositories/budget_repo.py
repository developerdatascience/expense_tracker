from sqlalchemy.orm import Session
from app.models.budget import Budget


class BudgetRepository:

    def __init__(self, db: Session):
        self.db = db
    
    def create_or_update(self, user_id, category_id, amount):
        budget = self.db.query(Budget).filter(
            Budget.user_id == user_id,
            Budget.category_id == category_id
        ).first()

        if budget:
            budget.amount = amount
        else:
            budget = Budget(
                user_id=user_id,
                category_id=category_id,
                amount=amount
            )
            self.db.add(budget)
        
        self.db.commit()
        self.db.refresh(budget)
        return budget
    

    def get_by_user(self, user_id):
        return self.db.query(Budget).filter(Budget.user_id == user_id).all()