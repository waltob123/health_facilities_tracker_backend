from typing import Optional

from pydantic import BaseModel, field_validator

from app.locations.utils.constants import FacilityOwnership, FacilityType


class BaseFacilitySchema(BaseModel):
    """Base schema for facility request and response."""

    name: str
    sub_district_id: str
    facility_type: str
    ownership: str
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    altitude: Optional[float] = None

    @field_validator("facility_type")
    @classmethod
    def validate_facility_type(cls, value: str) -> str:
        """Check if the facility type is valid.

        Args:
            value (str): The facility type to check

        Returns:
            str: The validated facility type.
        """
        if FacilityType.__contains__(value.lower()):
            return value.lower()
        raise ValueError("Invalid facility type.")

    @field_validator("ownership")
    @classmethod
    def validate_ownership(cls, value: str) -> str:
        """Check if the facility ownership is valid.

        Args:
            value (str): The facility ownership to check.

        Returns:
            str: The validated facility ownership.
        """
        if FacilityOwnership.__contains__(value.lower()):
            return value.lower()
        raise ValueError("Invalid facility ownership.")


CreateFacilitySchema = BaseFacilitySchema

UpdateFacilitySchema = CreateFacilitySchema
