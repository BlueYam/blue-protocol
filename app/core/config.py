from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env", env_file_encoding="utf-8", extra="ignore"
    )

    PROJECT_NAME: str = "BLUE PROTOCOL"
    PROJECT_VERSION: str = "1.0.0"

    SECRET_KEY: str = ""
    ALGORITHM: str = "HS256"

    DB_NAME: str = ""
    DB_URL: str = f"sqlite+aiosqlite:///{BASE_DIR / DB_NAME}"


CONFIG = Settings()