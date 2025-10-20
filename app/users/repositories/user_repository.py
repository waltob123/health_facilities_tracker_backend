from sqlalchemy.orm import Session

from app.core.base_repository import BaseReadRepository, BaseWriteRepository, T
from app.users.models import User


class UserRepository(BaseReadRepository[User], BaseWriteRepository[User]):
    """Repository for managing User entities."""

    def __init__(self, *, db_session: Session, model: type[User] = User) -> None:
        """Initialize the UserRepository with a database session and model.

        Args:
            db_session (Session): The SQLAlchemy database session.
            model (User): The User model class.
        """
        self.db_session = db_session
        self.model = model
        super().__init__(db_session=db_session, model=model)

    def create(self, **kwargs) -> T:  # type: ignore
        """Create a new User entity."""
        return self.model()

    def update(self, *, entity: T, **kwargs) -> T:  # type: ignore
        """Update an existing User entity."""
        return entity
