from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_user
from app.services.notification_service import NotificationService

router = APIRouter(prefix="/notifications", tags=["Notifications"])


@router.get("/")
def get_notifications(db: Session = Depends(get_db),
                      user= Depends(get_current_user)):
    service = NotificationService(db)
    return service.get_all(user.id)