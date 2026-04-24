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