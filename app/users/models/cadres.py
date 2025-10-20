from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.core.mixins.base import AuditCreateMixin, AuditUpdateMixin, IdentityMixin, SoftDeleteMixin
from app.database.base import Base


class Cadre(Base, IdentityMixin, AuditCreateMixin, AuditUpdateMixin, SoftDeleteMixin):
    """SQLAlchemy model for the 'cadres' table."""

    __tablename__ = "cadres"

    name = Column(String(100), unique=True, nullable=False)

    # Relationships
    user_profiles = relationship("UserProfile", back_populates="cadre")

    def to_dict(self) -> dict:
        """Convert Cadre model to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "is_deleted": self.is_deleted,
            "deleted_at": self.deleted_at if self.deleted_at else None,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
