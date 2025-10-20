from app.core.schemas.base_read_schema import BaseReadSchema
from app.locations.schemas.request.region import BaseRegionSchema


class ReadRegionSchema(BaseReadSchema, BaseRegionSchema):
    """Schema for region responses."""
