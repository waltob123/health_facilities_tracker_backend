from pydantic_settings import BaseSettings, SettingsConfigDict

from app.core.utils.constants import BASE_DIR


class ProjectConfig(BaseSettings):
    """Project configuration settings."""

    PROJECT_NAME: str = "Health Facilities Tracker"
    PROJECT_VERSION: str = "0.1.0"
    PROJECT_ENV: str = "DEV"
    PROJECT_PLATFORM: str = "Local"
    FRONTEND_URL: str = "http://127.0.0.1:3000"

    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env", env_file_encoding="utf-8", extra="ignore")


project_config = ProjectConfig()  # type: ignore
