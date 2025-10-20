from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.dependencies.database_dependency import db_session_dependency
from app.locations.factories.sub_district_factory import SubDistrictRepositoryFactory, SubDistrictServiceFactory
from app.locations.services.sub_district_service import SubDistrictService


def create_sub_district_service(*, db_session: Session = Depends(db_session_dependency)) -> SubDistrictService:
    """Dependency to create a new sub_district service.

    Args:
        db_session (Session): The database session needed for the sub_district service.

    Returns:
        SubDistrictService: The created sub_district service.
    """
    sub_district_repository = SubDistrictRepositoryFactory.create(db_session=db_session)
    return SubDistrictServiceFactory.create(sub_district_repository=sub_district_repository)
