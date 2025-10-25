from fastapi import Depends
from sqlalchemy.orm import Session

from app.auth.factories.auth_factory import AuthServiceFactory
from app.auth.services.auth_service import AuthService
from app.core.dependencies.database_dependency import db_session_dependency
from app.users.factories.user_factory import UserRepositoryFactory


def create_auth_service(*, db_session: Session = Depends(db_session_dependency)) -> AuthService:
    """Dependency to create a new auth service.

    Args:
        db_session (Session): The database session needed for the user repository.

    Returns:
        UserService: The created user  service.
    """
    user_repository = UserRepositoryFactory.create(db_session=db_session)
    return AuthServiceFactory.create(user_repository=user_repository)
