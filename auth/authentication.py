from fastapi import APIRouter
from starlette.requests import Request
from fastapi_sso.sso.google import GoogleSSO
from dotenv import load_dotenv
import os

router = APIRouter()
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID", None)
CLIENT_SECRET = os.getenv("CLIENT_SECRET", None)

# client id, client secret, callback url
google_sso = GoogleSSO(CLIENT_ID, CLIENT_SECRET, "http://localhost:8000/google/callback")

@router.get("/google/login")
async def google_login():
    with google_sso:
        return await google_sso.get_login_redirect()


@router.get("/google/callback")
async def google_callback(request: Request):
    try:
        with google_sso:
            user = await google_sso.verify_and_process(request)
        return user
    except Exception as e:
        print(e)