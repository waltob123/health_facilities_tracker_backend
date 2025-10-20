from typing import Any, Optional, Type, Union

from sqlalchemy.orm import Session, joinedload

from app.core.base_repository import BaseReadRepository, BaseWriteRepository
from app.locations.models import District, Facility, Region, SubDistrict
from app.locations.schemas.request.facility import CreateFacilitySchema


class FacilityRepository(BaseReadRepository[Facility], BaseWriteRepository[Facility]):
    """Repository for managing Facility entities."""

    def __init__(self, *, db_session: Session, model: type[Facility] = Facility) -> None:
        """Initialize the FacilityRepository with a database session and model.

        Args:
            db_session (Session): The SQLAlchemy database session.
            model (User): The Facility model class.
        """
        self.db_session = db_session
        self.model = model
        super().__init__(db_session=db_session, model=model)

    def create(self, *, data: CreateFacilitySchema) -> Facility:
        """The method to create a new facility entity.

        Args:
            data (CreateFacilitySchema): The facility data needed to create the entity.

        Returns:
            Facility: The newly created facility.
        """
        return self._default_create(data=data.model_dump())

    def get_all(
        self,
        *,
        filters_without_joins: list[str],
        filters_with_joins: Optional[list] = None,
        pagination: Optional[dict[str, int]] = None,
        filters: Optional[dict[str, Any]] = None,
        sort: Optional[dict[str, str]] = None,
    ) -> Union[list[Facility], list[Type[Facility]]]:
        """Get all entities.

        Args:
            filters_without_joins (list): Filters without no joins
            filters_with_joins (list): Filters with joins
            pagination (dict[str, int]): Pagination parameters.
            filters (dict[str, Any]): Filter parameters.
            sort (dict[str, str]): Sort parameters.

        Returns:
            list[Facility]: A list of all entity instances.
        """
        query = self.db_session.query(Facility)
        query = query.options(
            joinedload(Facility.sub_district).joinedload(SubDistrict.district).joinedload(District.region)
        )

        if filters:
            if filters.get("region_name"):
                query = query.join(SubDistrict).join(District).join(Region)
                filters["region_name"].update({"field_name": "name", "model": Region})

            if filters.get("district_name"):
                query = query.join(SubDistrict).join(District)
                filters["district_name"].update({"field_name": "name", "model": District})

            if filters.get("sub_district_name"):
                query = query.join(SubDistrict)
                filters["sub_district_name"].update({"field_name": "name", "model": SubDistrict})

        return self._default_get_all(
            filters_without_joins=filters_without_joins,
            filters_with_joins=filters_with_joins,
            pagination=pagination,
            filters=filters,
            sort=sort,
            query=query,
        )
