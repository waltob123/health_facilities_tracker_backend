from sqlalchemy.orm import Session

from app.core.factories.base_repository_factory import BaseRepositoryFactory
from app.locations.dependencies.region_service_dependency import create_region_service
from app.locations.models import District
from app.locations.repositories.district_repository import DistrictRepository
from app.locations.services.district_service import DistrictService


class DistrictRepositoryFactory(BaseRepositoryFactory[District, DistrictRepository]):
    """A factory for creating district repositories."""

    @classmethod
    def create(cls, *, db_session: Session) -> DistrictRepository:
        """Create a new district repository.

        Args:
            db_session (Session): The database session for the repository.

        Returns:
            DistrictRepository: The created district repository.
        """
        return cls._default_create(db_session=db_session, model=District, repository_class=DistrictRepository)


class DistrictServiceFactory:
    """A factory for creating district services."""

    @classmethod
    def create(cls, *, district_repository: DistrictRepository) -> DistrictService:
        """Create a new district service.

        Args:
            district_repository (DistrictRepository): The district repository for data.

        Returns:
            DistrictService: The created district service.
        """
        region_service = create_region_service(db_session=district_repository.db_session)
        return DistrictService(district_repository=district_repository, region_service=region_service)
