# app/api/v1/endpoints/summarize.py
import aiohttp
from fastapi import APIRouter, HTTPException, Query
from app.utils.reddit_parser import parse_reddit
from app.utils.ai_summarizer import summarize_text
from app.schemas.summary import SummaryResponse
import re
from urllib.parse import urlparse, urlunparse

router = APIRouter()


def validate_reddit_url(url: str) -> bool:
    pattern = r"^https?://(www\.)?reddit\.com/r/\w+/comments/\w+"
    return bool(re.match(pattern, url))


def clean_reddit_url(url: str) -> str:
    """Удаляет query-параметры из URL, оставляя только базовую часть."""
    parsed_url = urlparse(url)
    cleaned_url = urlunparse((
        parsed_url.scheme,  # http или https
        parsed_url.netloc,  # www.reddit.com
        parsed_url.path,  # /r/NooTopics/comments/1jjd0d9/nootropic_for_tranquility/
        "",  # params (не используется)
        "",  # query (обнуляем)
        ""  # fragment (обнуляем)
    ))
    return cleaned_url.rstrip("/")


@router.get("/summarize", response_model=SummaryResponse)
async def summarize_reddit(
        url: str = Query(..., description="Reddit post URL"),
        prompt: str = Query(default="Summarize this reddit post: ", description="Custom prompt for summarization")
):
    # Очищаем URL от query-параметров
    cleaned_url = clean_reddit_url(url)

    # Проверяем валидность очищенного URL
    if not validate_reddit_url(cleaned_url):
        raise HTTPException(status_code=400, detail="Invalid Reddit URL")

    try:
        content = await parse_reddit(cleaned_url)  # Передаем очищенный URL
        if not content:
            raise HTTPException(status_code=400, detail="No content extracted from the Reddit URL")
        summary = await summarize_text(content, prompt=prompt)
        return {"summary": summary}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(ve)}")
    except aiohttp.ClientError as ce:
        raise HTTPException(status_code=503, detail=f"Failed to fetch data: {str(ce)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")