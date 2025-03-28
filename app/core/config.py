from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GROQ_API_KEY: str  # Ключ для Groq API
    REDDIT_BASE_URL: str = "https://www.reddit.com"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()