from pydantic import BaseModel


class BaseDistrictSchema(BaseModel):
    """Base Schema for district requests and responses."""

    name: str


class CreateDistrictSchema(BaseDistrictSchema):
    """Schema for creating a district."""

    region_id: str


UpdateDistrictSchema = CreateDistrictSchema
