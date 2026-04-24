from app.db.base import Base
from app.db.session import engine

from app.models import user, expense, bill, category, budget, notification

def init_db():
    Base.metadata.create_all(bind=engine)