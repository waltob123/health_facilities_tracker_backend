from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.dependencies.database_dependency import db_session_dependency
from app.locations.factories.district_factory import DistrictRepositoryFactory, DistrictServiceFactory
from app.locations.services.district_service import DistrictService


def create_district_service(*, db_session: Session = Depends(db_session_dependency)) -> DistrictService:
    """Dependency to create a new district service.

    Args:
        db_session (Session): The database session needed for the district service.

    Returns:
        DistrictService: The created district service.
    """
    district_repository = DistrictRepositoryFactory.create(db_session=db_session)
    return DistrictServiceFactory.create(district_repository=district_repository)
