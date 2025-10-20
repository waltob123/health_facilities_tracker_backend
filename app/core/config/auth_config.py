from pydantic_settings import BaseSettings, SettingsConfigDict

from app.auth.utils.keygen import generate_secret_key
from app.core.utils.constants import BASE_DIR


class AuthConfig(BaseSettings):
    """Authentication configuration settings."""

    JWT_SECRET_KEY: str = generate_secret_key()
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_MINUTES: int

    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env", env_file_encoding="utf-8", extra="ignore")


auth_config = AuthConfig()  # type: ignore
