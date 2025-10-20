from fastapi import Depends
from sqlalchemy.orm import Session

from app.auth.factories.role_factory import RoleRepositoryFactory, RoleServiceFactory
from app.auth.services.role_service import RoleService
from app.core.dependencies.database_dependency import db_session_dependency


def create_role_service(*, db_session: Session = Depends(db_session_dependency)) -> RoleService:
    """Dependency to create a new role service.

    Args:
        db_session (Session): The database session needed for the role service.

    Returns:
        RoleService: The created role service.
    """
    role_repository = RoleRepositoryFactory.create(db_session=db_session)
    return RoleServiceFactory.create(role_repository=role_repository)
