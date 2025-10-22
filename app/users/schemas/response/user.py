from datetime import datetime
from typing import Optional, Union

from pydantic import field_validator

from app.core.schemas.base_read_schema import BaseReadSchema
from app.users.schemas.request.user import BaseUserSchema


class ReadUserSchema(BaseReadSchema, BaseUserSchema):
    """Schema for user responses."""

    email: str
    first_time_login: bool
    is_logout: bool
    last_login: Optional[datetime]
    is_verified: bool
    is_suspended: bool

    @field_validator("last_login")
    @classmethod
    def datetime_is_valid(cls, dt: Union[datetime, None]) -> Union[datetime, None]:
        """Validate that the given datetime is valid

        Args:
            dt (datetime): The datetime to validate

        Returns:
            datetime: The validated datetime
        """
        if dt is not None and isinstance(dt, datetime):
            return dt
        if dt is None:
            return None
