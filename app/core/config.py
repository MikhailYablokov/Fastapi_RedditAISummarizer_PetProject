#app/core/config.py
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    TOGETHER_API_KEY: str
    USER_AGENT: str = "RedditSummarizer/1.0"
    MAX_TEXT_LENGTH: int = 10000

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()