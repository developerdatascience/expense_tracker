from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_user
from app.services.category_service import CategoryService

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/")
def create_category(name: str, db: Session = Depends(get_db), user=Depends(get_current_user)):
    service = CategoryService(db)
    return service.create_category(user_id=user.id, name=name)

@router.get("/")
def list_categories(db: Session = Depends(get_db), user = Depends(get_current_user)):
    service = CategoryService(db)
    return service.list_categories(user_id=user.id)

@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    service = CategoryService(db)
    return service.delete_category(category_id=category_id, user_id=user.id)
