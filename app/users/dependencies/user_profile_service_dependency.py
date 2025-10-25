from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.dependencies.database_dependency import db_session_dependency
from app.users.factories.user_profile_factory import UserProfileRepositoryFactory, UserProfileServiceFactory
from app.users.services.user_profile_service import UserProfileService


def create_user_profile_service(*, db_session: Session = Depends(db_session_dependency)) -> UserProfileService:
    """Dependency to create a new user profile service.

    Args:
        db_session (Session): The database session needed for the user profile service.

    Returns:
        UserService: The created user profile service.
    """
    user_profile_repository = UserProfileRepositoryFactory.create(db_session=db_session)
    return UserProfileServiceFactory.create(user_profile_repository=user_profile_repository)
