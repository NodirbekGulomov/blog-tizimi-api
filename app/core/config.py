from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg://postgres:admin@localhost:5432/blog_db"
    JWT_SECRET_KEY: str = "JWT_SECRET_KEY"
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int = 15

    model_config = {"env_file": BASE_DIR / ".env"}


settings = Settings()
