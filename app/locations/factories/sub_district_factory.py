from sqlalchemy.orm import Session

from app.core.factories.base_repository_factory import BaseRepositoryFactory
from app.locations.dependencies.district_service_dependency import create_district_service
from app.locations.models import SubDistrict
from app.locations.repositories.sub_district_repository import SubDistrictRepository
from app.locations.services.sub_district_service import SubDistrictService


class SubDistrictRepositoryFactory(BaseRepositoryFactory[SubDistrict, SubDistrictRepository]):
    """A factory for creating sub_district repositories."""

    @classmethod
    def create(cls, *, db_session: Session) -> SubDistrictRepository:
        """Create a new sub_district repository.

        Args:
            db_session (Session): The database session for the repository.

        Returns:
            SubDistrictRepository: The created sub_district repository.
        """
        return cls._default_create(db_session=db_session, model=SubDistrict, repository_class=SubDistrictRepository)


class SubDistrictServiceFactory:
    """A factory for creating sub_district services."""

    @classmethod
    def create(cls, *, sub_district_repository: SubDistrictRepository) -> SubDistrictService:
        """Create a new sub_district service.

        Args:
            sub_district_repository (SubDistrictRepository): The sub_district repository for data.

        Returns:
            SubDistrictService: The created sub_district service.
        """
        district_service = create_district_service(db_session=sub_district_repository.db_session)
        return SubDistrictService(sub_district_repository=sub_district_repository, district_service=district_service)
