from app.core.schemas.base_read_schema import BaseReadSchema
from app.locations.schemas.request.facility import BaseFacilitySchema


class ReadFacilitySchema(BaseReadSchema, BaseFacilitySchema):
    """Schema for facility responses."""

    region_id: str
    district_id: str
    sub_district_id: str
    region_name: str
    district_name: str
    sub_district_name: str
