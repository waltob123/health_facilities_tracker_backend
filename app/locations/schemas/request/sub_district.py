from pydantic import BaseModel


class BaseSubDistrictSchema(BaseModel):
    """Base schema for sub_districts request and responses."""

    name: str
    district_id: str


CreateSubDistrictSchema = BaseSubDistrictSchema

UpdateSubDistrictSchema = CreateSubDistrictSchema
