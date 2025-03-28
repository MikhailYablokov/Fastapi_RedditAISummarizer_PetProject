#app/main.py
from fastapi import FastAPI
from app.api.v1.endpoints import summarize

app = FastAPI(title="Reddit Summarizer")

app.include_router(summarize.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to Reddit Summarizer"}