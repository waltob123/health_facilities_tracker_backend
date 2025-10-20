from sqlalchemy.orm import Session

from app.auth.models import Role
from app.auth.repositories.role_repository import RoleRepository
from app.auth.services.role_service import RoleService
from app.core.factories.base_repository_factory import BaseRepositoryFactory


class RoleRepositoryFactory(BaseRepositoryFactory[Role, RoleRepository]):
    """A factory for creating role repositories."""

    @classmethod
    def create(cls, *, db_session: Session) -> RoleRepository:
        """Create a new role repository.

        Args:
            db_session (Session): The database session for the repository.

        Returns:
            RoleRepository: The created role repository.
        """
        return cls._default_create(db_session=db_session, model=Role, repository_class=RoleRepository)


class RoleServiceFactory:
    """A factory for creating role services."""

    @classmethod
    def create(cls, *, role_repository: RoleRepository) -> RoleService:
        """Create a new role service.

        Args:
            role_repository (RoleRepository): The role repository for data.

        Returns:
            RoleService: The created role service.
        """
        return RoleService(role_repository=role_repository)
