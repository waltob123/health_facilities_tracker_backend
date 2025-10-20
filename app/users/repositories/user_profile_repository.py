from sqlalchemy.orm import Session

from app.core.base_repository import BaseReadRepository, BaseWriteRepository, T
from app.users.models import UserProfile


class UserProfileRepository(BaseReadRepository[UserProfile], BaseWriteRepository[UserProfile]):
    """Repository for managing UserProfile entities."""

    def __init__(self, *, db_session: Session, model: type[UserProfile] = UserProfile) -> None:
        """Initialize the UserProfileRepository with a database session and model.

        Args:
            db_session (Session): The SQLAlchemy database session.
            model (UserProfile): The UserProfile model class.
        """
        self.db_session = db_session
        self.model = model
        super().__init__(db_session=db_session, model=model)

    def create(self, **kwargs) -> T:  # type: ignore
        """Create a new UserProfile entity."""
        return self.model()

    def update(self, *, entity: T, **kwargs) -> T:  # type: ignore
        """Update an existing UserProfile entity."""
        return entity
