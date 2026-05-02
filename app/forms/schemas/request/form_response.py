from typing import Any, Optional

from pydantic import BaseModel


class CreateFormResponseRequestSchema(BaseModel):
    """Schema for creating a new form response (submission)."""

    form_id: str
    submitted_by: Optional[str] = None
    answers: dict[str, Any]
