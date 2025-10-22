from typing import Any, Optional, Type, Union

from sqlalchemy.orm import Session, joinedload

from app.auth.models import Role
from app.core.base_repository import BaseReadRepository, BaseWriteRepository
from app.locations.models import Facility
from app.users.models import User, UserProfile
from app.users.schemas.request.user import CreateUserSchema


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

    def create(self, data: CreateUserSchema) -> User:  # type: ignore
        """Create a new User entity.

        Args:
            data (CreateUserSchema): The data needed to create the user

        Returns:
            User: The created user.
        """
        new_user = User(email=data.email, password_has=data.password_hash)  # type: ignore

        if data.role_ids:
            roles = self.db_session.query(Role).filter(Role.id.in_(data.role_ids)).all()
            new_user.roles = roles

        return self.save(object_to_save=new_user)

    def get_all(
        self,
        *,
        filters_without_joins: list[str],
        filters_with_joins: Optional[list] = None,
        pagination: Optional[dict[str, int]] = None,
        filters: Optional[dict[str, Any]] = None,
        sort: Optional[dict[str, str]] = None,
    ) -> Union[list[User], list[Type[User]]]:
        """Retrieve all users.

        Args:
            filters_without_joins (list): Filters without no joins
            filters_with_joins (list): Filters with joins
            pagination (dict[str, int]): Pagination parameters.
            filters (dict[str, Any]): Filter parameters.
            sort (dict[str, str]): Sort parameters.

        Returns:
            list[User]: A list of all entity instances.
        """
        query = self.db_session.query(User)
        query = query.options(joinedload(User.profile).joinedload(UserProfile.facility)).options(joinedload(User.roles))

        if filters:
            if filters.get("first_name") or filters.get("phone_number") or filters.get("country"):
                query = query.join(UserProfile)

            if filters.get("first_name"):
                filters["first_name"].update({"field_name": "first_name", "model": UserProfile})

            if filters.get("phone_number"):
                filters["phone_number"].update({"field_name": "phone_number", "model": UserProfile})

            if filters.get("country"):
                filters["country"].update({"field_name": "country", "model": UserProfile})

            if filters.get("facility_name"):
                query = query.join(UserProfile.facility)
                filters["facility_name"].update({"field_name": "name", "model": Facility})

        return self._default_get_all(
            filters_without_joins=filters_without_joins,
            filters_with_joins=filters_with_joins,
            pagination=pagination,
            filters=filters,
            sort=sort,
            query=query,
        )
