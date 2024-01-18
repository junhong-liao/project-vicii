from fastapi import FastAPI
import mysql.connector
from pydantic import BaseModel

dbapp = FastAPI()

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dbuserdbuser"
)

# if not db, create
cursor = db.cursor()
cursor.execute("SHOW DATABASES")
databases = [database[0] for database in cursor]

if "vicii_db" not in databases:
    cursor.execute("CREATE DATABASE vicii_db")

# connect to db
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dbuserdbuser",
    database="vicii_db"
)

cursor = db.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(16),
        email VARCHAR(255),
        elo INT
    )
""")

class User(BaseModel):
    username: str
    email: str
    elo: int=1000

# retrieves all users
@dbapp.get("/users")
def get_users():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    return {"users": result}

# retrieves a specific user by id
@dbapp.get("/get-user/{id}")
def get_user(id: int):
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {id}")
    result = cursor.fetchone()
    return {"employee": result}

# inserts a new user
# @dbapp.post("/users")
# def add_user(name: str, email: str, elo: int=1000):
#     cursor = db.cursor()
#     sql = "INSERT INTO users (name, email, elo) VALUES (%s, %s, %d)"
#     val = (name, email, elo)
#     cursor.execute(sql, val)
#     db.commit()
#     return {"message": "User added successfully"}

@dbapp.post("/users")
def add_user(user: User):
    cursor = db.cursor()
    sql = "INSERT INTO users (username, email, elo) VALUES (%s, %s, %s)"
    val = (user.username, user.email, user.elo)
    cursor.execute(sql, val)
    db.commit()
    return {"message": "User added successfully"}

# delete a specific user by ID
@dbapp.delete("/users/{id}")
def delete_employee(id: int):
    cursor = db.cursor()
    cursor.execute(f"DELETE FROM users WHERE id = {id}")
    db.commit()
    return 

# Test query:

"""
(env) junho@Junhongs-MacBook-Air project-vicii % curl -X POST -H "Content-Type: application/json" -d '{"name":"john", "email":"john@gmail.com", "elo":1000}' http://localhost:8000/users
{"detail":[{"type":"missing","loc":["body","username"],"msg":"Field required","input":{"name":"john","email":"john@gmail.com","elo":1000},"url":"https://errors.pydantic.dev/2.5/v/missing"}]}%                             
(env) junho@Junhongs-MacBook-Air project-vicii % 
"""




