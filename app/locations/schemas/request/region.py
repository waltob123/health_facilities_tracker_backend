from pydantic import BaseModel


class BaseRegionSchema(BaseModel):
    """Base schema for region request and response."""

    name: str


CreateRegionSchema = BaseRegionSchema

UpdateRegionSchema = BaseRegionSchema
