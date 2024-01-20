from fastapi import APIRouter
from .database import Database
from .models import User

router = APIRouter()
db = Database()

@router.get("/users")
def get_users():
    with db.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall() or []
        result = []
        for user in users:
            result.append({
                "id": user[0],
                "username": user[1],
                "email": user[2],
                "elo": user[3]             
            })
        return result

@router.post("/users")
def add_user(user: User):
    with db.get_connection() as conn:
        cursor = conn.cursor()
        sql = "INSERT INTO users (username, email, elo) VALUES (%s, %s, %s)"
        cursor.execute(sql, (user.username, user.email, user.elo))
        conn.commit()
        return {"message": "User added successfully"}

@router.get("/users/id/{id}")
def get_user_by_id(id: int):
    with db.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
        user = cursor.fetchone()
        user_data = {
            "id": user[0],
            "username": user[1],
            "email": user[2],
            "elo": user[3]             
        }
        return user_data

@router.get("/users/email/{email}")
def get_user_by_email(email: str):
    try:
        with db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()
            if user is not None:
                user_data = {
                    "id": user[0],
                    "username": user[1],
                    "email": user[2],
                    "elo": user[3]             
                }
                return user_data
            else:
                return []
    except Exception as e:
        print(str(e))
    
@router.delete("/users/del/{id}")
def delete_user(id: int):
    with db.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (id,))
        conn.commit()