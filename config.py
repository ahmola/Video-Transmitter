from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+asyncmy://root:pass@localhost:3306/vfs?charset=utf8"

settings = Settings()