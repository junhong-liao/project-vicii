from fastapi import FastAPI

from db.operations import router as db_router
from db.database import Database
# from auth import authentication 


app = FastAPI(title="Vicii v1.0")

db = Database()
db.initialize_db()

app.include_router(db_router, prefix="/db")
# app.include_router(auth_router, prefix="/auth")
