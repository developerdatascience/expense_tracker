from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from datetime import datetime
from app.db.base import Base

class Bill(Base):
    __tablename__ = "bills"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)

    due_date = Column(DateTime, nullable=False)
    recurrence = Column(String, default="monthly") # monthly, weekly, yearly

    user_id = Column(Integer, ForeignKey("users.id"))

    last_paid = Column(DateTime, nullable=True)
