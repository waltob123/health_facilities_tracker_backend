from app.core.schemas.base_read_schema import BaseReadSchema
from app.locations.schemas.request.sub_district import BaseSubDistrictSchema


class ReadSubDistrictSchema(BaseReadSchema, BaseSubDistrictSchema):
    """Schema for sub_district responses."""

    district_name: str
    region_id: str
    region_name: str
