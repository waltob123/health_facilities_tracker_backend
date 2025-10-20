from typing import Optional

from pydantic import BaseModel, Field


class BaseRoleSchema(BaseModel):
    """Base schema for role."""

    name: str


class CreateRoleSchema(BaseRoleSchema):
    """The schema for creating a new role."""

    permission_ids: Optional[list] = Field(default=[])


UpdateRoleSchema = CreateRoleSchema
