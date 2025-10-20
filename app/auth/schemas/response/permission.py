from app.auth.schemas.request.permission import BasePermissionSchema
from app.core.schemas.base_read_schema import BaseReadSchema


class ReadPermissionSchema(BaseReadSchema, BasePermissionSchema):
    """Schema for permission responses."""
