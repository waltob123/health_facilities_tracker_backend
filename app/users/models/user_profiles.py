from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.core.mixins.base import AuditCreateMixin, AuditUpdateMixin, IdentityMixin, SoftDeleteMixin
from app.database.base import Base


class UserProfile(Base, IdentityMixin, AuditCreateMixin, AuditUpdateMixin, SoftDeleteMixin):
    """SQLAlchemy model for the 'user_profiles' table."""

    __tablename__ = "user_profiles"

    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    other_names = Column(String(50), nullable=True)
    phone_number = Column(String(15), nullable=False, unique=True)
    cadre_id = Column(String(36), ForeignKey("cadres.id", ondelete="SET NULL", onupdate="CASCADE"), nullable=True)
    facility_id = Column(
        String(36), ForeignKey("facilities.id", ondelete="SET NULL", onupdate="CASCADE"), nullable=True
    )

    # Relationships
    user = relationship("User", back_populates="profile")
    cadre = relationship("Cadre", back_populates="user_profiles")
    facility = relationship("Facility", back_populates="user_profiles")

    def to_dict(self) -> dict:
        """Convert UserProfile model to dictionary."""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "email": self.user.email,
            "is_verified": self.user.is_verified,
            "is_suspended": self.user.is_suspended,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "other_names": self.other_names,
            "phone_number": self.phone_number,
            "cadre_id": self.cadre_id,
            "cadre_name": self.cadre.name if self.cadre else None,
            "facility_id": self.facility_id,
            "facility_name": self.facility.name if self.facility else None,
            "is_deleted": self.is_deleted,
            "deleted_at": self.deleted_at if self.deleted_at else None,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
