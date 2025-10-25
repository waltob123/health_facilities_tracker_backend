from typing import Optional

from fastapi import HTTPException, status

from app.core.base_service import BaseService
from app.core.custom_exceptions import ObjectAlreadyExistsException
from app.locations.models import Facility, SubDistrict
from app.locations.repositories.facility_repository import FacilityRepository
from app.locations.schemas.request.facility import CreateFacilitySchema, UpdateFacilitySchema
from app.locations.utils.allowed_filters_sort import (
    allowed_facility_filters,
    allowed_facility_sorts,
    facility_filters_with_joins,
    facility_filters_without_joins,
)


class FacilityService(BaseService[Facility]):
    """The service class for 'facility'."""

    def __init__(
        self, *, facility_repository: FacilityRepository, sub_district_service: BaseService[SubDistrict]
    ) -> None:
        """Initializer for 'facility' service.

        Args:
            facility_repository (FacilityRepository): The facility repository.
            sub_district_service (BaseService[SubDistrict]): The sub_district service.
        """
        self.facility_repository = facility_repository
        self.sub_district_service = sub_district_service
        super().__init__(main_repository=facility_repository)

    def get_all(
        self, *, pagination: Optional[str] = None, filters: Optional[str] = None, sort: Optional[str] = None
    ) -> list[Facility]:
        """Get all facility entities.

        Args:
            pagination (dict[str, int]): Pagination parameters.
            filters (dict[str, Any]): Filter parameters.
            sort (dict[str, str]): Sort parameters.

        Returns:
            list[Facility]: A list of all entity instances
        """
        return self._default_get_all(
            filters_with_joins=facility_filters_with_joins,
            filters_without_joins=facility_filters_without_joins,
            pagination=pagination,
            filters=filters,
            sort=sort,
            allowed_filters=allowed_facility_filters,
            allowed_sorts=allowed_facility_sorts,
        )

    def create(self, *, facility_data: CreateFacilitySchema) -> Facility:
        """Create a new facility.

        Args:
            facility_data (CreateFacilitySchema): The facility data to create.

        Returns:
            Facility: The newly created facility.
        """
        # check if sub_district exists.
        _ = self.sub_district_service.get_by_id(entity_id=facility_data.sub_district_id)

        return self._default_create(entity_schema=facility_data)

    def update(self, *, facility_id: str, data_to_update: UpdateFacilitySchema) -> Facility:
        """Update a facility.

        Args:
            facility_id (str): The id of the facility to update.
            data_to_update (UpdateFacilitySchema): The data to update the facility with.

        Returns:
            Facility: The updated facility.
        """
        # check if facility exists.
        facility = self.get_by_id(entity_id=facility_id)
        _ = self.sub_district_service.get_by_id(entity_id=data_to_update.sub_district_id)

        try:
            updated_role = self.facility_repository.update(entity=facility, update_data=data_to_update.model_dump())
        except ObjectAlreadyExistsException as e:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e)) from e

        return updated_role
