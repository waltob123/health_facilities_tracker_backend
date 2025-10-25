from datetime import datetime, timedelta, timezone
from typing import Any, Optional

import jwt

from app.core.custom_exceptions import ExpiredTokenError, InvalidTokenError
from app.core.utils.messages import ErrorMessages


class TokenService:
    """A service for managing tokens."""

    def __init__(
        self,
        *,
        secret: str,
        algorithm: str,
    ) -> None:
        """Initialize a new token service

        Args:
            secret (str): The secret key used for signing the token
            algorithm (str): The algorithm used for signing the token
        """
        self.__secret = secret
        self.__algorithm = algorithm

    def create_token(self, *, payload: dict, expires_in_minutes: int = 15, token_type: Optional[str] = None) -> str:
        """Encode the payload and generate a JWT token

        Args:
            payload (dict): The payload to encode
            expires_in_minutes (int): The number of minutes until the token expires
            token_type (str): The type of token to create

        Returns:
            str: The encoded token
        """
        data_to_encode = payload.copy()

        token_expire = datetime.now(timezone.utc) + timedelta(minutes=expires_in_minutes)  # type: ignore

        data_to_encode.update({"exp": token_expire})

        if token_type:
            data_to_encode.update({"token_type": token_type})

        token = jwt.encode(data_to_encode, self.__secret, algorithm=self.__algorithm)

        return token

    def decode_token(self, *, token: str) -> Any:
        """Decode the JWT token and get the payload

        Args:
            token (str): The JWT token to decode

        Returns:
            dict: The decoded payload
        """
        try:
            payload = jwt.decode(token, self.__secret, algorithms=[self.__algorithm])
        except jwt.ExpiredSignatureError as e:
            raise ExpiredTokenError(ErrorMessages.EXPIRED_TOKEN.value) from e
        except jwt.InvalidTokenError as e:
            raise InvalidTokenError(ErrorMessages.INVALID_TOKEN.value) from e

        return payload
