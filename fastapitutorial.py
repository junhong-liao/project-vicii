from fastapi import FastAPI, Depends, HTTPException
from authlib.integrations.starlette_client import OAuth

# this is where you name your 'app'
# uvicorn <filename>:<appname> --reload
app = FastAPI()

@app.get("/test")
def test():
    return {"message": "Hello world!"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

"""
Use curl with quotes to not mess anything up
"""
@app.get("/query-params/")
def query_params(start: int=0, end: int=99):
    return {"start": start, "end": end}