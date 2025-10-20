from sqlalchemy.orm import Session

from app.core.factories.base_repository_factory import BaseRepositoryFactory
from app.locations.models import Region
from app.locations.repositories.region_repository import RegionRepository
from app.locations.services.region_service import RegionService


class RegionRepositoryFactory(BaseRepositoryFactory[Region, RegionRepository]):
    """A factory for creating region repositories."""

    @classmethod
    def create(cls, *, db_session: Session) -> RegionRepository:
        """Create a new region repository.

        Args:
            db_session (Session): The database session for the repository.

        Returns:
            RegionRepository: The created region repository.
        """
        return cls._default_create(db_session=db_session, model=Region, repository_class=RegionRepository)


class RegionServiceFactory:
    """A factory for creating region services."""

    @classmethod
    def create(cls, *, region_repository: RegionRepository) -> RegionService:
        """Create a new region service.

        Args:
            region_repository (RegionRepository): The region repository for data.

        Returns:
            RegionService: The created region service.
        """
        return RegionService(region_repository=region_repository)
