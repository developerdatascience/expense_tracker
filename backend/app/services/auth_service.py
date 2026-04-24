from app.repositories.user_repo import UserRepository
from app.core.security import SecurityService

class AuthService:
    def __init__(self, db):
        self.user_repo = UserRepository(db)
    
    def register_user(self, user_data):
        existing_user = self.user_repo.get_email(user_data.email)
        if existing_user:
            raise ValueError("Email already registered")
        
        hashed_password = SecurityService.hash_password(user_data.password)

        user = self.user_repo.create({
            "email": user_data.email,
            "username": user_data.username,
            "hashed_password": hashed_password
            })
        
        return user

    def login(self, login_data):
        user = self.user_repo.get_email(login_data.email)

        if not user:
            raise Exception("Invalid email or password")
        
        if not SecurityService.verify_password(login_data.password, user.hashed_password):
            raise Exception("Invalid email or password")
        
        token = SecurityService.create_access_token({"sub": str(user.id)})
        return token