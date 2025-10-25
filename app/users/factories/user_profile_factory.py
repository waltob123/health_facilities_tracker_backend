from sqlalchemy.orm import Session

from app.core.factories.base_repository_factory import BaseRepositoryFactory
from app.users.models import UserProfile
from app.users.repositories.user_profile_repository import UserProfileRepository
from app.users.services.user_profile_service import UserProfileService


class UserProfileRepositoryFactory(BaseRepositoryFactory[UserProfile, UserProfileRepository]):
    """A factory for creating user profile repositories."""

    @classmethod
    def create(cls, *, db_session: Session) -> UserProfileRepository:
        """Create a new user profile repository.

        Args:
            db_session (Session): The database session for the repository.

        Returns:
            UserProfileRepository: The created user profile repository.
        """
        return cls._default_create(db_session=db_session, model=UserProfile, repository_class=UserProfileRepository)


class UserProfileServiceFactory:
    """A factory for creating user profile services."""

    @classmethod
    def create(cls, *, user_profile_repository: UserProfileRepository) -> UserProfileService:
        """Create a new user profile service.

        Args:
            user_profile_repository (UserProfileRepository): The user profile repository for data.

        Returns:
            UserProfileService: The created user profile service.
        """
        return UserProfileService(user_profile_repository=user_profile_repository)
