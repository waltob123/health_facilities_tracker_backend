from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.dependencies.database_dependency import db_session_dependency
from app.locations.factories.facility_factory import FacilityRepositoryFactory, FacilityServiceFactory
from app.locations.services.facility_service import FacilityService


def create_facility_service(*, db_session: Session = Depends(db_session_dependency)) -> FacilityService:
    """Dependency to create a new facility service.

    Args:
        db_session (Session): The database session needed for the facility service.

    Returns:
        FacilityService: The created facility service.
    """
    facility_repository = FacilityRepositoryFactory.create(db_session=db_session)
    return FacilityServiceFactory.create(facility_repository=facility_repository)
