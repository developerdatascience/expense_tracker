from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_user
from app.services.budget_service import BudgetService

router = APIRouter(prefix="/budgets", tags=["Budgets"])


@router.post("/")
def set_budget(category_id: int, 
               amount: float,
               db: Session = Depends(get_db),
               user = Depends(get_current_user)):
    service = BudgetService(db)
    return service.set_budget(user.id, category_id, amount)

@router.get("/alerts")
def budget_alerts(db: Session = Depends(get_db), user=Depends(get_current_user)):
    service = BudgetService(db)
    return service.check_budget_beach(user.id)


