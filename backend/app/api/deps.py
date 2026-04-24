from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.core.security import SecurityService
from app.models.user import User

security = HTTPBearer()

def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(security),
        db: Session = Depends(get_db)
    ) -> User:

    token = credentials.credentials
    payload = SecurityService.decode_access_token(token)

    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user_id = payload.get("sub")

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user
