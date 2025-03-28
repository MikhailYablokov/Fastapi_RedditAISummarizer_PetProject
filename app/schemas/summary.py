#app/schemas/summary.py
from pydantic import BaseModel, HttpUrl

class SummaryRequest(BaseModel):
    url: HttpUrl  # URL страницы Reddit

class SummaryResponse(BaseModel):
    summary: str  # Итоговая суммаризация