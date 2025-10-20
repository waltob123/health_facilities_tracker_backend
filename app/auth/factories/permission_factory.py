from sqlalchemy.orm import Session

from app.auth.models import Permission
from app.auth.repositories.permission_repository import PermissionRepository
from app.auth.services.permission_service import PermissionService
from app.core.factories.base_repository_factory import BaseRepositoryFactory


class PermissionRepositoryFactory(BaseRepositoryFactory[Permission, PermissionRepository]):
    """A factory for creating permission repositories."""

    @classmethod
    def create(cls, *, db_session: Session) -> PermissionRepository:
        """Create a new permission repository.

        Args:
            db_session (Session): The database session for the repository.

        Returns:
            PermissionRepository: The created permission repository.
        """
        return cls._default_create(db_session=db_session, model=Permission, repository_class=PermissionRepository)


class PermissionServiceFactory:
    """A factory for creating permission services."""

    @classmethod
    def create(cls, *, permission_repository: PermissionRepository) -> PermissionService:
        """Create a new permission service.

        Args:
            permission_repository (PermissionRepository): The permission repository for data.

        Returns:
            PermissionService: The created permission service.
        """
        return PermissionService(permission_repository=permission_repository)
