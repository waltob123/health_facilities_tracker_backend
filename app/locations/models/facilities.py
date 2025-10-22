from typing import Any

from sqlalchemy import Column, ForeignKey, Numeric, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.core.mixins.base import (
    AuditCreateMixin,
    AuditUpdateMixin,
    IdentityMixin,
    SoftDeleteMixin,
)
from app.database.base import Base

# from app.users.models import UserProfile  # noqa: F401


class Facility(Base, IdentityMixin, AuditCreateMixin, AuditUpdateMixin, SoftDeleteMixin):
    """SQLAlchemy model for the 'facilities' table."""

    __tablename__ = "facilities"

    name = Column(String(100), nullable=False)
    facility_type = Column(String(100), nullable=False)
    ownership = Column(String(100), nullable=False)
    sub_district_id = Column(
        String(36),
        ForeignKey("sub_districts.id", onupdate="CASCADE"),
        nullable=False,
    )
    latitude = Column(Numeric(10, 8), nullable=True)
    longitude = Column(Numeric(12, 9), nullable=True)
    altitude = Column(Numeric(14, 9), nullable=True)

    __table_args__ = (UniqueConstraint("sub_district_id", "name", name="unq_sub_district_facility"),)

    # Relationships
    sub_district = relationship("SubDistrict", back_populates="facilities")
    user_profiles = relationship("UserProfile", back_populates="facility")

    def to_dict(self) -> dict[str, Any]:
        """Convert the Facility instance to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "facility_type": self.facility_type,
            "ownership": self.ownership,
            "sub_district_id": self.sub_district_id,
            "sub_district_name": self.sub_district.name,
            "district_name": self.sub_district.district.name,
            "district_id": self.sub_district.district.id,
            "region_name": self.sub_district.district.region.name,
            "region_id": self.sub_district.district.region.id,
            "longitude": self.longitude if self.longitude else None,
            "latitude": self.latitude if self.latitude else None,
            "altitude": self.altitude if self.altitude else None,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "is_deleted": self.is_deleted,
            "deleted_at": self.deleted_at if self.deleted_at else None,
        }
