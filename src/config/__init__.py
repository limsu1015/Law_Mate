import os
from enum import StrEnum

from pydantic.v1 import BaseSettings


class ServerEnv(StrEnum):
    LOCAL = "local"
    DEV = "dev"
    PROD = "prod"


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str
    PROJECT_DESCRIPTION: str
    ASYNC_DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()
