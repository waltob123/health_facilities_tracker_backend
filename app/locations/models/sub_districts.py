from typing import Any

from sqlalchemy import Column, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.core.mixins.base import (
    AuditCreateMixin,
    AuditUpdateMixin,
    IdentityMixin,
    SoftDeleteMixin,
)
from app.database.base import Base


class SubDistrict(Base, IdentityMixin, AuditCreateMixin, AuditUpdateMixin, SoftDeleteMixin):
    """SQLAlchemy model for the 'sub_districts' table."""

    __tablename__ = "sub_districts"

    name = Column(String(100), nullable=False)
    district_id = Column(
        String(100),
        ForeignKey("districts.id", onupdate="CASCADE"),
        nullable=False,
    )

    __table_args__ = (UniqueConstraint("district_id", "name", name="unq_sub_district_district"),)

    # Relationships
    district = relationship("District", back_populates="sub_districts")
    facilities = relationship("Facility", back_populates="sub_district")

    def to_dict(self) -> dict[str, Any]:
        """Convert the SubDistrict instance to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "region_name": self.district.region.name,
            "region_id": self.district.region.id,
            "district_name": self.district.name,
            "district_id": self.district.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "is_deleted": self.is_deleted,
            "deleted_at": self.deleted_at if self.deleted_at else None,
        }
