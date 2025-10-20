from typing import Any, Literal, Optional, Union

from fastapi import Request
from pydantic import BaseModel, Field, field_validator
from starlette.responses import JSONResponse


class ResponseSchema(BaseModel):
    """Schema for error responses."""

    status: Literal["success", "error"]
    status_code: int = Field(..., ge=100, le=599)
    message: str = Field(..., min_length=1)
    data: Optional[Union[list[Any], Any]] = None
    extras: Optional[dict] = None

    def __init__(self, request: Request, **data):  # type: ignore
        """Initialize the ResponseHandler object.

        Args:
            request (Request): The request object.
            data (dict): The data to be used to initialize the ResponseHandler.
        """
        super().__init__(**data)

        # Setting default info for extras if not provided
        extras_default_info = {"method": request.method, "url": str(request.url)}

        if self.extras is None:
            self.extras = extras_default_info
        else:
            self.extras.update(extras_default_info)

    @field_validator("status")
    @classmethod
    def validate_status(cls, value: str) -> str:
        """Validate that the status is either 'success' or 'error'."""
        if value not in ["success", "error"]:
            raise ValueError("Status must be either 'success' or 'error'.")
        return value

    def to_json_response(self) -> JSONResponse:
        """Convert the schema to a JSON response."""
        return JSONResponse(
            status_code=self.status_code,
            content={
                "status": self.status,
                "status_code": self.status_code,
                "message": self.message,
                "data": self.data,
                "extras": self.extras,
            },
        )
