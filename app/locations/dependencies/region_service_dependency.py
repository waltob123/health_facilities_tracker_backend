from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.dependencies.database_dependency import db_session_dependency
from app.locations.factories.region_factory import RegionRepositoryFactory, RegionServiceFactory
from app.locations.services.region_service import RegionService


def create_region_service(*, db_session: Session = Depends(db_session_dependency)) -> RegionService:
    """Dependency to create a new region service.

    Args:
        db_session (Session): The database session needed for the region service.

    Returns:
        RegionService: The created region service.
    """
    region_repository = RegionRepositoryFactory.create(db_session=db_session)
    return RegionServiceFactory.create(region_repository=region_repository)
