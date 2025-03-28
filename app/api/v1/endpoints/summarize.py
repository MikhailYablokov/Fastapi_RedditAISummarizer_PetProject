from fastapi import APIRouter, HTTPException
from app.schemas.summary import SummaryRequest, SummaryResponse
from app.utils.reddit_parser import parse_reddit
from app.utils.ai_summarizer import summarize_text

router = APIRouter()

@router.post("/summarize", response_model=SummaryResponse)
async def summarize_reddit(request: SummaryRequest):
    try:
        content = await parse_reddit(request.url)
        summary = await summarize_text(content)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))