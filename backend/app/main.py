from fastapi import FastAPI
from app.db.init_db import init_db
from app.api.v1 import auth
from app.api.v1 import auth, expenses, categories               

app = FastAPI()

@app.on_event("startup")
def startup_event():
    init_db()


app.include_router(auth.router)
app.include_router(expenses.router)
app.include_router(categories.router)


@app.get("/")
def root():
    return {"message": "Welcome to the Expense Tracker API!"}

