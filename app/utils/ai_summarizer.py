#app/utils/ai_summarizer.py
import aiohttp
from app.core.config import settings

async def summarize_text(text: str, prompt: str = "Summarize this: ") -> str:
    url = "https://api.together.xyz/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {settings.TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "messages": [{"role": "user", "content": f"{prompt}{text}"}],
        "temperature": 0.5
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, headers=headers) as response:
            response_data = await response.json()
            return response_data["choices"][0]["message"]["content"]