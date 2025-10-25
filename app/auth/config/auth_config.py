from pydantic_settings import BaseSettings, SettingsConfigDict

from app.core.utils.constants import BASE_DIR


class AuthConfig(BaseSettings):
    """Authentication configuration settings."""

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRES_IN_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRES_IN_MINUTES: int
    VERIFICATION_LINK_EXPIRES_IN_MINUTES: int

    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env", env_file_encoding="utf-8", extra="ignore")


auth_config = AuthConfig()  # type: ignore
