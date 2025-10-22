from typing import Optional

from pydantic import BaseModel, EmailStr, Field, field_validator

from app.core.custom_exceptions import InvalidEmailError, InvalidPasswordError
from app.core.utils.messages import ErrorMessages
from app.core.utils.validators import is_valid_email, is_valid_password
from app.users.schemas.request.user_profile import CreateUserProfileRequestSchema


class BaseUserSchema(BaseModel):
    """The base schema for user request and responses."""

    email: EmailStr
    role_ids: Optional[list[str]] = Field(default=[])

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: EmailStr) -> EmailStr:
        """Check if the email is a valid email.

        Args:
            value (EmailStr): The email to validate.

        Returns:
            EmailStr: The validated email.
        """
        if not is_valid_email(email=str(value)):
            raise InvalidEmailError(ErrorMessages.INVALID_EMAIL.value)
        return value


class CreateUserRequestSchema(BaseUserSchema):
    """The schema for create user request."""

    password: str
    user_profile: CreateUserProfileRequestSchema

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str:
        """Check if the password is a valid password.

        Args:
            value (str): The password to validate

        Returns:
            str: The validate password.
        """
        if not is_valid_password(password=value):
            raise InvalidPasswordError(ErrorMessages.INVALID_PASSWORD.value)
        return value


class CreateUserSchema(CreateUserRequestSchema):
    """The schema for creating a user."""

    password_hash: Optional[str] = None


UpdateUserSchema = CreateUserRequestSchema
