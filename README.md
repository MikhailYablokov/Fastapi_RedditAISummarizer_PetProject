# Reddit Summarizer
Асинхронный сервис на FastAPI для парсинга Reddit и суммаризации через Groq API.

## Установка
1. `pip install -r requirements.txt`
2. Создай `.env` с `GROQ_API_KEY` (получи на https://console.groq.com).
3. Запусти: `uvicorn app.main:app --reload`

## Использование
POST /api/v1/summarize
{
    "url": "https://www.reddit.com/r/example/comments/post_id/"
}