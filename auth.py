from fastapi import FastAPI, Request, HTTPException
from authlib.integrations.starlette_client import OAuth
from dotenv import load_dotenv
from starlette.middleware.sessions import SessionMiddleware
import os

app = FastAPI()

# load environment variables using dotenv (onto virtual 'system', for os to access)
load_dotenv()

# pull secret key
SECRET_KEY = os.getenv("GOOGLE_CLIENT_SECRET")

# add middleware, set secret key
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

# OAuth setup
oauth = OAuth()
oauth.register(
    name='google',
    # I have to set these system variables
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url ='https://accounts.google.com/o/oauth2/v1',
    client_kwargs={
        'scope' : 'openid email profile'
    }
)

# redirect to Google OAuth
@app.get("/login")
async def login(request: Request):
    redirect_uri = request.url_for('auth')
    return await oauth.google.authorize_redirect(request, redirect_uri)

"""
async allows FastAPI to handle multiple requests concurrently
when waiting on IO-bound operations (db call), frees up event loop to handle other requests
However,if operation is bounded by CPU (very complex), async will not necessarily provide benefits...
"""

# OAuth callback route
@app.get("/auth")
async def auth(request: Request):
    try:
        token = await oauth.google.authorize_access_token(request)
        user = await oauth.google.parse_id_token(request, token)
        return {"user": user}
    except Exception as e:
        # 401 unauthorized, convert exception to str
        raise HTTPException(status_code=401, detail=str(e))

# endpoint for tests
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}