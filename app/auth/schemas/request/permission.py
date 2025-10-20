from pydantic import BaseModel


class BasePermissionSchema(BaseModel):
    """Base schema for permission."""

    name: str


CreatePermissionSchema = BasePermissionSchema
