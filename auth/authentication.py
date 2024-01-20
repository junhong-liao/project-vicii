from fastapi import APIRouter
from starlette.requests import Request
from fastapi_sso.sso.google import GoogleSSO
from dotenv import load_dotenv
from db.models import User
from db.database import Database
from db.operations import get_user_by_email, add_user
import requests
import os


router = APIRouter()
load_dotenv()

API_BASE_URL = "http://localhost:8000/auth"

CLIENT_ID = os.getenv("CLIENT_ID", None)
CLIENT_SECRET = os.getenv("CLIENT_SECRET", None)

# client id, client secret, callback url
google_sso = GoogleSSO(CLIENT_ID, CLIENT_SECRET, f"{API_BASE_URL}/google/callback")

@router.get("/google/login")
async def google_login():
    with google_sso:
        return await google_sso.get_login_redirect()
    

@router.get("/google/callback")
async def google_callback(request: Request):
    try:
        with google_sso:
            user_info = await google_sso.verify_and_process(request)
            first_name, user_email = user_info.first_name, user_info.email
            print(f"USER EMAIL: {user_email}")
            # not using microservices architecture at the moment
            # call db method directly
            user_data = get_user_by_email(user_email)
            if len(user_data) == 0:
                user = User(
                    username=first_name,
                    email=user_email,
                    elo=1000
                )
                print("NOT ADDED YET")
                add_user(user)
                print("ADDED CONFIRMED")
            # redirect to homepage... curr. return value for testing
            return user_info
    except Exception as e:
        print(e)


# v0.1 for testing purposes
# @router.get("/google/callback")
# async def google_callback(request: Request):
#     try:
#         with google_sso:
#             user_info = await google_sso.verify_and_process(request)
#     except Exception as e:
#         print(str(e))
#     finally:
#         return user_info
        

# v1.1 for testing purposes
# @router.get("/google/callback")
# async def google_callback(request: Request):
#     try:
#         with google_sso:
#             user_info = await google_sso.verify_and_process(request)
#             # user_email = user_info["email"]
#             if isinstance(user_info, dict):
#                 user_email = user_info["email"]
        
#             # explain/ first check if the user exists
#             response = requests.get(f"http://localhost:8000/db/users/email/{user_email}")
#             # feature/ consider moving user creation to another endpoint
#             if len(response) == 0:
#                 user_data = {
#                     "username": user_info["first_name"],
#                     "email": user_email,
#                     # base elo = 1000
#                     "elo": 1000
#                 }
#                 response = requests.post(f"http://localhost:8000/db/users", user_data)
#                 print(response)
#     except Exception as e:
#         print(e)
#     finally:
#         return user_info