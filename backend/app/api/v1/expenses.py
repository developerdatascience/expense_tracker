from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.db.session import get_db
from app.api.deps import get_current_user
from app.services.expense_service import ExpenseService
from app.schemas.expense import ExpenseCreate

router = APIRouter(prefix="/expenses", tags=["Expenses"])


@router.post("/")
def add_expense(
        expense: ExpenseCreate,
        db: Session = Depends(get_db),
        user = Depends(get_current_user)
    ):
    service = ExpenseService(db=db)
    return service.add_expense(user_id=user.id, expense_data=expense.model_dump())

@router.get("/")
def list_expenses(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    service = ExpenseService(db=db)
    return service.list_expenses(user.id, skip, limit)


@router.get("/filter")
def filter_expenses(
    start_date: datetime, 
    end_date: datetime, 
    category_id: int=None, 
    db: Session = Depends(get_db), 
    user = Depends(get_current_user)
):
    service = ExpenseService(db=db)
    return service.filter_expenses(user_id=user.id, filters={"start_date": start_date, "end_date": end_date, "category_id": category_id})


@router.get("/summary/category")
def category_summary(db: Session = Depends(get_db), user = Depends(get_current_user)):
    service = ExpenseService(db=db)
    return service.get_category_summary(user.id)

@router.get("/summary/daily")
def daily_trend(db: Session = Depends(get_db), user = Depends(get_current_user)):
    service = ExpenseService(db=db)
    return service.get_daily_trend(user.id)


@router.get("/summary/monthly")
def monthly_trend(db: Session = Depends(get_db), user = Depends(get_current_user)):
    service = ExpenseService(db=db)
    return service.get_monthly_summary(user.id)