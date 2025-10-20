from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel, field_validator

from app.core.utils.constants import ApplicationConstants
from app.core.utils.messages import ErrorMessages
from app.core.utils.validators import is_valid_uuid


class BaseReadSchema(BaseModel):
    """Base read schema for entities."""

    id: str
    created_at: datetime
    updated_at: Optional[datetime]

    @field_validator("id")
    @classmethod
    def id_is_valid_uuid(cls, value: str) -> str:
        """Validate that the given id is a valid

        Args:
            value (str): The id to validate

        Returns:
            bool: True if the id is valid, False otherwise

        Raises:
            ValueError: If the id is not a valid uuid
        """
        if is_valid_uuid(uuid_to_test=value):
            return value
        raise ValueError(ErrorMessages.INVALID_ID.value)

    @field_validator("created_at", "updated_at")
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

    class ConfigDict:
        """Configuration class for base schema."""

        from_attributes = True
        json_encoders = {
            datetime: lambda dt: dt.strftime(ApplicationConstants.DATE_FORMAT.value),
        }
