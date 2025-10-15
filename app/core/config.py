from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = 'sqlite:///./database.db'
    
settings = Settings()