#app/api/v1/endpoints/summarize.py
from fastapi import APIRouter, HTTPException, Query
from app.utils.reddit_parser import parse_reddit
from app.utils.ai_summarizer import summarize_text
from app.schemas.summary import SummaryResponse

router = APIRouter()

@router.get("/summarize", response_model=SummaryResponse)
async def summarize_reddit(
    url: str = Query(..., description="Reddit post URL", example="https://reddit.com/r/example/comments/abc123"),
    prompt: str = Query(default="Summarize this: ", description="Custom prompt for summarization", example="Give me a brief overview of: ")
):
    try:
        content = await parse_reddit(url)
        summary = await summarize_text(content, prompt=prompt)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))