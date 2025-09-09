"""
Core configuration settings for the Product Tracker application
"""

import os
from pathlib import Path

from pydantic import computed_field
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE_PATH = os.path.join(BASE_DIR, ".env")


class Settings(BaseSettings):
    """Application settings"""

    # Database
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str
    # redis_url: str

    # JWT Configuration
    # jwt_secret_key: str
    # jwt_algorithm: str
    # jwt_access_token_expire_minutes: int
    # jwt_refresh_token_expire_days: int

    # Environment
    app_name: str
    environment: str
    debug: bool
    host: str
    port: int

    # CORS
    # allowed_origins: list[str]

    class Config:
        env_file = ENV_FILE_PATH
        case_sensitive = False

    @computed_field
    @property
    def database_url(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"  # noqa E501


# Create settings instance
settings = Settings()  # type: ignore
