from typing import Optional

from fastapi import HTTPException


class AuthHTTPException(HTTPException):
    """A custom exception for authentication."""

    def __init__(
        self, *, status_code: int, message: str, data: Optional[dict] = None, headers: Optional[dict] = None
    ) -> None:
        """Initializer for the AuthHTTPException.

        Args:
            status_code (int): The status code.
            message (str): The message
            data (dict): The data
            headers (dict): the headers
        """
        self.status_code = status_code
        self.detail = {"message": message, "data": data}  # type: ignore
        self.headers = headers
        self.message = message
        self.data = data
        super().__init__(status_code=self.status_code, detail=self.detail, headers=self.headers)
