from app.core.schemas.base_read_schema import BaseReadSchema
from app.locations.schemas.request.district import CreateDistrictSchema


class ReadDistrictSchema(BaseReadSchema, CreateDistrictSchema):
    """Schema for district responses."""

    region_name: str
