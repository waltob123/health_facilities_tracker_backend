from app.auth.schemas.request.role import CreateRoleSchema
from app.core.schemas.base_read_schema import BaseReadSchema


class ReadRoleSchema(BaseReadSchema, CreateRoleSchema):
    """Response schema for roles."""
