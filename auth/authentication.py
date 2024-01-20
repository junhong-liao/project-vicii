from fastapi import APIRouter
from starlette.requests import Request
from fastapi_sso.sso.google import GoogleSSO
from dotenv import load_dotenv
from db.models import User
from db.operations import get_user_by_email, add_user
import os

router = APIRouter()
load_dotenv()

API_BASE_URL = "http://localhost:8000/auth"
CLIENT_ID = os.getenv("CLIENT_ID", None)
CLIENT_SECRET = os.getenv("CLIENT_SECRET", None)

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
            user_data = get_user_by_email(user_email)
            if len(user_data) == 0:
                user = User(
                    username=first_name,
                    email=user_email,
                    elo=1000
                )
                add_user(user)
            # replace this with a redirect to user homepage...
            return user_info
    except Exception as e:
        print(e)