from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.dependencies.database_dependency import db_session_dependency
from app.users.factories.user_factory import UserRepositoryFactory, UserServiceFactory
from app.users.services.user_service import UserService


def create_user_service(*, db_session: Session = Depends(db_session_dependency)) -> UserService:
    """Dependency to create a new user service.

    Args:
        db_session (Session): The database session needed for the user service.

    Returns:
        UserService: The created user service.
    """
    user_repository = UserRepositoryFactory.create(db_session=db_session)
    return UserServiceFactory.create(user_repository=user_repository)
