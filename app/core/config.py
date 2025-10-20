from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # DATABASE_URL: str = 'sqlite:///./database.db' # * SQLite
    DATABASE_URL: str = 'postgresql+psycopg://postgres:qweasd123@localhost:5432/fastapi'  # * PostgreSQL


settings = Settings()
