from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ExpenseCreate(BaseModel):
    amount: float
    description: Optional[str]
    category_id: int
    date: Optional[datetime]
    payment_method: Optional[str]
    tags: Optional[str]