from typing import Optional

from fastapi import HTTPException, status

from app.core.base_service import BaseService
from app.core.custom_exceptions import ObjectAlreadyExistsException
from app.locations.models import SubDistrict
from app.locations.repositories.sub_district_repository import SubDistrictRepository
from app.locations.schemas.request.sub_district import CreateSubDistrictSchema, UpdateSubDistrictSchema
from app.locations.utils.allowed_filters_sort import (
    allowed_sub_district_filters,
    allowed_sub_district_sorts,
    sub_district_filters_with_joins,
    sub_district_filters_without_joins,
)


class SubDistrictService(BaseService[SubDistrict]):
    """The service class for 'sub_district'."""

    def __init__(self, *, sub_district_repository: SubDistrictRepository, district_service: BaseService) -> None:
        """Initializer for 'sub_district' service.

        Args:
            sub_district_repository (SubDistrictRepository): The sub_district repository.
            district_service (BaseService): The district service.
        """
        self.sub_district_repository = sub_district_repository
        self.district_service = district_service
        super().__init__(main_repository=sub_district_repository)

    def get_all(
        self, *, pagination: Optional[str] = None, filters: Optional[str] = None, sort: Optional[str] = None
    ) -> list[SubDistrict]:
        """Get all sub_district entities.

        Args:
            pagination (dict[str, int]): Pagination parameters.
            filters (dict[str, Any]): Filter parameters.
            sort (dict[str, str]): Sort parameters.

        Returns:
            list[SubDistrict]: A list of all entity instances
        """
        return self._default_get_all(
            filters_with_joins=sub_district_filters_with_joins,
            filters_without_joins=sub_district_filters_without_joins,
            pagination=pagination,
            filters=filters,
            sort=sort,
            allowed_filters=allowed_sub_district_filters,
            allowed_sorts=allowed_sub_district_sorts,
        )

    def create(self, *, sub_district_data: CreateSubDistrictSchema) -> SubDistrict:
        """Create a new sub_district.

        Args:
            sub_district_data (CreateSubDistrictSchema): The sub_district data to create.

        Returns:
            SubDistrict: The newly created sub_district.
        """
        # check if district exists.
        _ = self.district_service.get_by_id(entity_id=sub_district_data.district_id)

        return self._default_create(
            entity_schema=sub_district_data, unique_field_to_check="name", unique_field_value=sub_district_data.name
        )

    def update(self, *, sub_district_id: str, data_to_update: UpdateSubDistrictSchema) -> SubDistrict:
        """Update a sub_district.

        Args:
            sub_district_id (str): The id of the sub_district to update.
            data_to_update (UpdateSubDistrictSchema): The data to update the sub_district with.

        Returns:
            SubDistrict: The updated sub_district.
        """
        # check if sub_district exists.
        sub_district = self.get_by_id(entity_id=sub_district_id)
        _ = self.district_service.get_by_id(entity_id=data_to_update.district_id)

        try:
            updated_role = self.sub_district_repository.update(
                entity=sub_district, update_data=data_to_update.model_dump()
            )
        except ObjectAlreadyExistsException as e:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e)) from e

        return updated_role
