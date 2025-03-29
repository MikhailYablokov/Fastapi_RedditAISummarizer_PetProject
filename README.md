
Reddit Summarizer 
---
Reddit Summarizer — это API на базе FastAPI, которое извлекает содержимое постов Reddit (заголовок, текст и комментарии) и создает их краткое содержание с помощью искусственного интеллекта от Together AI. Подходит для быстрого анализа обсуждений без чтения всего треда.

Требования  
- Python: 3.9 или выше  
- Git: для клонирования репозитория  
- Together API Key: зарегистрируйтесь на Together AI (https://together.ai) и получите API-ключ  

Установка:
---
1. Клонируйте репозиторий:  
   git clone https://github.com/MikhailYablokov/reddit-summarizer.git  
   cd reddit-summarizer  
2. Создайте и активируйте виртуальную среду:  
   python -m venv venv  
   source venv/bin/activate (для Windows: venv\Scripts\activate)  
3. Установите зависимости:  
   pip install -r requirements.txt  
4. Создайте файл .env и добавьте:  
   TOGETHER_API_KEY=<ваш api-ключ together.ai>  
   USER_AGENT=RedditSummarizer/1.0  
   MAX_TEXT_LENGTH=10000  
5. Запустите сервер:  
   uvicorn app.main:app --reload  
6. Откройте документацию или отправьте запрос:  
   localhost:8000/docs  
   или  
   localhost:8000/api/v1/summarize?url=<ваша ссылка на тред с reddit>  
7. Дождитесь ответа от нейросети  

Стек технологий:
---
- FastAPI: асинхронный веб-фреймворк для API  
- Python 3.9+: основной язык  
- Together AI: сервис ИИ для суммаризации  
- aiohttp: асинхронные HTTP-запросы  
- Pydantic: валидация данных  
- Uvicorn: сервер для FastAPI  
- python-dotenv: управление переменными окружения  

Пример использования:
---
- Запрос: curl "http://localhost:8000/api/v1/summarize?url=https://www.reddit.com/r/Python/comments/1jm3hml/funlog_why_dont_we_use_decorators_for_logging/"  
- Ответ: {"summary": "<Ответ>"}  

Структура проекта:
---
- app/main.py — точка входа  
- app/api/v1/endpoints/summarize.py — эндпоинт суммаризации  
- app/utils/ — утилиты для парсинга и ИИ  
- app/schemas/ — схемы данных  
- app/core/config.py — настройки

Устранение неполадок:
---
- Ошибка "TOGETHER_API_KEY not found": проверьте файл .env.  
- Ошибка 503: Reddit может быть недоступен, попробуйте позже.  
- Зависимости не устанавливаются: обновите pip (pip install --upgrade pip).  

---

English version
---
Reddit Summarizer is an API based on FastAPI that extracts content from Reddit posts (title, body, and comments) and generates a summary using artificial intelligence from Together AI. Perfect for quickly analyzing discussions without reading the entire thread.

Requirements:
---
- Python: 3.9 or higher  
- Git: for cloning the repository  
- Together API Key: sign up at Together AI (https://together.ai) and get an API key  

Installation:
---
1. Clone the repository:  
   git clone https://github.com/MikhailYablokov/reddit-summarizer.git  
   cd reddit-summarizer  
2. Create and activate a virtual environment:  
   python -m venv venv  
   source venv/bin/activate (for Windows: venv\Scripts\activate)  
3. Install dependencies:  
   pip install -r requirements.txt  
4. Create a .env file and add:  
   TOGETHER_API_KEY=<your together.ai api key>  
   USER_AGENT=RedditSummarizer/1.0  
   MAX_TEXT_LENGTH=10000  
5. Run the server:  
   uvicorn app.main:app --reload  
6. Open the documentation or send a request:  
   localhost:8000/docs  
   or  
   localhost:8000/api/v1/summarize?url=<your reddit thread link>  
7. Wait for the neural network response  

Tech Stack:
---
- FastAPI: asynchronous web framework for API  
- Python 3.9+: main programming language  
- Together AI: AI service for summarization  
- aiohttp: asynchronous HTTP requests  
- Pydantic: data validation  
- Uvicorn: ASGI server for FastAPI  
- python-dotenv: environment variable management  

Usage Example:
---
Request: curl "http://localhost:8000/api/v1/summarize?url=https://www.reddit.com/r/Python/comments/1jm3hml/funlog_why_dont_we_use_decorators_for_logging/"  
Response: {"summary": "<response>"}  

Project Structure:
---
- app/main.py — entry point  
- app/api/v1/endpoints/summarize.py — summarization endpoint  
- app/utils/ — utilities for parsing and AI  
- app/schemas/ — data schemas  
- app/core/config.py — configuration

Troubleshooting:
---
- "TOGETHER_API_KEY not found" error: check the .env file.  
- 503 error: Reddit may be unavailable, try again later.  
- Dependencies not installing: update pip (pip install --upgrade pip).