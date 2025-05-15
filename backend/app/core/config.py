import os

PROJECT_NAME = "QR_Fastapi"

# SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
SQLALCHEMY_DATABASE_URI: str = "sqlite:///:memory:"

API_V1_STR = "/api/v1"

from pydantic import BaseSettings


class Settings(BaseSettings):
    # existing settings…
    QR_SIZE: int = 300
    QR_BORDER: int = 4
    QR_FORMAT: str = "PNG"

    SQLALCHEMY_DATABASE_URI: str = "sqlite:///:memory:"

    class Config:
        env_file = ".env"


def get_settings() -> Settings:
    return Settings()
