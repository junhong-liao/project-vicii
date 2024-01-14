from fastapi import FastAPI, Depends, HTTPException, Request
from authlib.integrations.starlette_client import OAuth
import os

app = FastAPI()
# OAuth setup
oa = OAuth()
oa.register(
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
"""
async allows FastAPI to handle multiple requests concurrently
when waiting on IO-bound operations (db call), frees up event loop to handle other requests
However,if operation is bounded by CPU (very complex), async will not necessarily provide benefits...
"""
@app.get("/login")
async def login(request: Request):
    redirect_uri = request.url_for('auth')
    
