from sqlalchemy.orm import Session
from app.models.category import Category


class CategoryRepository:

    def __init__(self, db: Session):
        self.db = db
    
    def create(self, data: dict):
        category = Category(**data)
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)
        return category
    
    def get_by_user(self, user_id: int):
        return self.db.query(Category).filter(Category.user_id == user_id).all()
    
    def delete(self, category_id: int, user_id: int):
        category = self.db.query(Category).filter(
            Category.id == category_id,
            Category.user_id == user_id
        ).first()
        
        if category:
            self.db.delete(category)
            self.db.commit()
        return True