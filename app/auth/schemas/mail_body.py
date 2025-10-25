from pydantic import BaseModel


class MailTemplateBodySchema(BaseModel):
    """Schema for mail templates."""

    title: str
    first_name: str
    app_name: str
    current_year: int


class AccountVerificationTemplateBodySchema(MailTemplateBodySchema):
    """Schema for account verification template body."""

    verification_url: str
    code_expires_in_hours: int


class ResetPasswordTemplateBodySchema(MailTemplateBodySchema):
    """Schema for reset password template body."""

    verification_url: str
    code_expires_in_minutes: int
