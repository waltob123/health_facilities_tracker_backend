from fastapi import Depends
from sqlalchemy.orm import Session

from app.auth.factories.permission_factory import PermissionRepositoryFactory, PermissionServiceFactory
from app.auth.services.permission_service import PermissionService
from app.core.dependencies.database_dependency import db_session_dependency


def create_permission_service(*, db_session: Session = Depends(db_session_dependency)) -> PermissionService:
    """Dependency to create a new permission service.

    Args:
        db_session (Session): The database session needed for the permission service.

    Returns:
        PermissionService: The created permission service.
    """
    permission_repository = PermissionRepositoryFactory.create(db_session=db_session)
    return PermissionServiceFactory.create(permission_repository=permission_repository)
