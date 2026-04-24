from sqlalchemy.orm import Session
from app.models.expense import Expense
from sqlalchemy import func

class ExpenseRepository:

    def __init__(self, db: Session):
        self.db = db
    
    def create(self, data: dict):
        expense = Expense(**data)
        self.db.add(expense)
        self.db.commit()
        self.db.refresh(expense)
        return expense
    
    def get_all(self, user_id: int, skip=0, limit=100):
        return self.db.query(Expense) \
            .filter(Expense.user_id == user_id) \
            .order_by(Expense.data.desc()) \
            .offset(skip) \
            .limit(limit) \
            .all()
    
    def filter(self, user_id: int, start_date = None, end_date=None, category_id=None):
        query = self.db.query(Expense).filter(Expense.user_id == user_id)

        if start_date:
            query = query.filter(Expense.data >= start_date)
        if end_date:
            query = query.filter(Expense.date <= end_date)
        if category_id:
            query = query.filter(Expense.category_id == category_id)
        return query.all()

    def category_summary(self, user_id: int):
        return (
            self.db.query(
                Expense.category_id,
                func.sum(Expense.amount).label("total")
            )
            .filter(Expense.user_id == user_id)
            .group_by(Expense.category_id)
            .all()
        )
    
    def daily_trend(self, user_id: int):
        return (
            self.db.query(
                func.date(Expense.date).label("date"),
                func.sum(Expense.amount).label("total")
            )
            .filter(Expense.user_id == user_id)
            .group_by(func.date(Expense.date))
            .order_by(func.date(Expense.date))
            .all()
        )

    
    def get_monthly_summary(self, user_id: int):
        summary = self.db.query(
            func.strftime("%Y-%m", Expense.date).label("month"),
            func.sum(Expense.amount).label("total")
        ).filter(Expense.user_id == user_id).group_by("month").all()
        
        return [{"month": month, "total": total} for month, total in summary]
    