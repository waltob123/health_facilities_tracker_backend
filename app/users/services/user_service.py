from typing import Optional

from fastapi import HTTPException, status

from app.core.base_service import BaseService
from app.core.custom_exceptions import ObjectAlreadyExistsException
from app.users.models import User
from app.users.repositories.user_repository import UserRepository
from app.users.schemas.request.user_profile import UpdateUserProfileRequestSchema
from app.users.utils.allowed_filters_sort import (
    allowed_user_filters,
    allowed_user_sorts,
    user_filters_with_joins,
    user_filters_without_joins,
)


class UserService(BaseService[User]):
    """The service class for 'user'."""

    def __init__(
        self, *, user_repository: UserRepository, user_profile_service: BaseService, facility_service: BaseService
    ) -> None:
        """Initializer for 'user' service.

        Args:
            user_repository (UserRepository): The user repository.
            user_profile_service (BaseService): The user profile service.
            facility_service (BaseService): The facility service.
        """
        self.user_repository = user_repository
        self.user_profile_service = user_profile_service
        self.facility_service = facility_service
        super().__init__(main_repository=user_repository)

    def get_all(
        self, *, pagination: Optional[str] = None, filters: Optional[str] = None, sort: Optional[str] = None
    ) -> list[User]:
        """Get all user entities.

        Args:
            pagination (dict[str, int]): Pagination parameters.
            filters (dict[str, Any]): Filter parameters.
            sort (dict[str, str]): Sort parameters.

        Returns:
            list[User]: A list of all entity instances
        """
        return self._default_get_all(
            filters_with_joins=user_filters_with_joins,
            filters_without_joins=user_filters_without_joins,
            pagination=pagination,
            filters=filters,
            sort=sort,
            allowed_filters=allowed_user_filters,
            allowed_sorts=allowed_user_sorts,
        )

    def update(self, *, user_id: str, data_to_update: UpdateUserProfileRequestSchema) -> User:
        """Update a user.

        Args:
            user_id (str): The id of the user to update.
            data_to_update (UpdateUserSchema): The data to update the user with.

        Returns:
            User: The updated user.
        """
        # get user profile
        user_profile = self.user_profile_service.get_by_field(field_name="user_id", value=user_id)

        # check if facility exists
        if data_to_update.facility_id:
            _ = self.facility_service.get_by_id(entity_id=data_to_update.facility_id)

        try:
            _ = self.user_profile_service.update(entity=user_profile, update_data=data_to_update)
        except ObjectAlreadyExistsException as e:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e)) from e

        return self.get_by_id(entity_id=user_id)

    def create(self, *args, **kwargs) -> User:  # type: ignore
        """Create a new user."""
        raise NotImplementedError
