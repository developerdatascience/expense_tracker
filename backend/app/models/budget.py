from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True, index=True)

    amount = Column(Integer, nullable=False)

    category_id = Column(Integer, ForeignKey("categories.id"))
    user_id = Column(Integer, ForeignKey("users.id"))