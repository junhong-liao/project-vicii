from fastapi import APIRouter
from starlette.requests import Request
from fastapi_sso.sso.google import GoogleSSO
from dotenv import load_dotenv
from db.database import Database
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

@router.get("/google/callback")
async def google_callback(request: Request):
    try:
        with google_sso:
            user_info = await google_sso.verify_and_process(request)
            user_email = user_info["email"]
            # explain/ first check if the user exists
            response = requests.get(f"{API_BASE_URL}/users/{user_email}")
            # feature/ consider moving user creation to another endpoint
            if not response:
                user_data = {
                    "username": user_info["name"],
                    "email": user_info["email"],
                    # base elo = 1000
                    "elo": 1000
                }
                response = requests.post(f"{API_BASE_URL}/db/users", user_data)
    except Exception as e:
        print(e)
    finally:
        return user_info