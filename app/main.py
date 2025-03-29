#app/main.py
from fastapi import FastAPI
from app.api.v1.endpoints import summarize

# app/main.py
app = FastAPI(
    title="Reddit Summarizer",
    description="API for summarizing Reddit posts using AI.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(summarize.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to Reddit Summarizer"}