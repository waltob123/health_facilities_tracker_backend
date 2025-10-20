from typing import Annotated, Optional

from fastapi import APIRouter, Depends, Path, Query, Request, status

from app.core.schemas.base_entity_response_schema import ResponseSchema
from app.core.utils.constants import HTTPResponseStatus
from app.core.utils.messages import SuccessMessages
from app.locations.dependencies.sub_district_service_dependency import create_sub_district_service
from app.locations.docs.sub_districts_docs import (
    create_sub_district_docs,
    delete_sub_district_docs,
    get_all_sub_districts_docs,
    get_sub_district_by_id_docs,
    restore_sub_district_docs,
    update_sub_district_docs,
)
from app.locations.models import SubDistrict
from app.locations.schemas.request.sub_district import CreateSubDistrictSchema, UpdateSubDistrictSchema
from app.locations.schemas.response.sub_district import ReadSubDistrictSchema
from app.locations.services.sub_district_service import SubDistrictService

sub_district_router = APIRouter(prefix="/sub_districts", tags=["SubDistrict"])


@sub_district_router.post(path="", status_code=status.HTTP_201_CREATED, description=create_sub_district_docs)
def create_sub_district(
    request: Request,
    sub_district_data: CreateSubDistrictSchema,
    sub_district_service: Annotated[SubDistrictService, Depends(create_sub_district_service)],
) -> ResponseSchema:
    """Method for handling creating a new sub_district.

    Args:
        request (Request): The request object.
        sub_district_data (CreateSubDistrictSchema): The data needed to create the sub_district.
        sub_district_service (SubDistrictService): The sub_district service to use.

    Returns:
        ResponseSchema: The response data.
    """
    sub_district = sub_district_service.create(sub_district_data=sub_district_data)

    response_data = ResponseSchema(
        status=HTTPResponseStatus.SUCCESS.value,
        status_code=status.HTTP_200_OK,
        message=SuccessMessages.retrieved_successfully(object_type=SubDistrict),  # type: ignore
        data=ReadSubDistrictSchema(**sub_district.to_dict()),  # type: ignore
        request=request,
    )

    return response_data


@sub_district_router.get(path="", status_code=status.HTTP_200_OK, description=get_all_sub_districts_docs)
def get_all_sub_districts(
    request: Request,
    sub_district_service: Annotated[SubDistrictService, Depends(create_sub_district_service)],
    filters: Annotated[Optional[str], Query(..., description="Filters query parameter")] = None,
    sort: Annotated[Optional[str], Query(..., description="Sort query parameter")] = None,
    pagination: Annotated[Optional[str], Query(..., description="Pagination query parameter")] = None,
) -> ResponseSchema:
    """Method for handling get all sub_districts request.

    Args:
        request (Request): The request object.
        filters (str): The filters query parameter
        sort (str): The sort query parameter
        pagination (str): The pagination query parameter
        sub_district_service (SubDistrictService): The sub_district service to use.

    Returns:
        ResponseSchema: The response data.
    """
    extras: dict = {}
    sub_districts = sub_district_service.get_all(pagination=pagination, filters=filters, sort=sort)
    extras.update({"pagination": sub_district_service.get_pagination_extras(request=request)})
    extras["pagination"].update({"total_retrieved": len(sub_districts)})

    response_data = ResponseSchema(
        status=HTTPResponseStatus.SUCCESS.value,
        status_code=status.HTTP_200_OK,
        message=SuccessMessages.retrieved_successfully(object_type=SubDistrict),  # type: ignore
        data=list(map(lambda sub_district: ReadSubDistrictSchema(**sub_district.to_dict()), sub_districts)),  # type: ignore
        extras=extras,
        request=request,
    )

    return response_data


@sub_district_router.get(
    path="/{sub_district_id}", status_code=status.HTTP_200_OK, description=get_sub_district_by_id_docs
)
def get_sub_district_by_id(
    request: Request,
    sub_district_id: Annotated[str, Path(..., description="The id of the sub_district to get.")],
    sub_district_service: Annotated[SubDistrictService, Depends(create_sub_district_service)],
) -> ResponseSchema:
    """Method for handling get a sub_district by id request.

    Args:
        request (Request): The request object.
        sub_district_id (str): The id of the sub_district to retrieve.
        sub_district_service (SubDistrictService): The sub_district service to use.

    Returns:
        ResponseSchema: The response data.
    """
    sub_district = sub_district_service.get_by_id(entity_id=sub_district_id)

    response_data = ResponseSchema(
        status=HTTPResponseStatus.SUCCESS.value,
        status_code=status.HTTP_200_OK,
        message=SuccessMessages.retrieved_successfully(object_type=SubDistrict),  # type: ignore
        data=ReadSubDistrictSchema(**sub_district.to_dict()),  # type: ignore
        request=request,
    )

    return response_data


@sub_district_router.put(
    path="/{sub_district_id}", status_code=status.HTTP_200_OK, description=update_sub_district_docs
)
def update_sub_district(
    request: Request,
    sub_district_id: Annotated[str, Path(..., description="The id of the sub_district to get.")],
    data_to_update: UpdateSubDistrictSchema,
    sub_district_service: Annotated[SubDistrictService, Depends(create_sub_district_service)],
) -> ResponseSchema:
    """Method for handling update a sub_district by id request.

    Args:
        request (Request): The request object.
        sub_district_id (str): The id of the sub_district to update.
        data_to_update (UpdateSubDistrictSchema): The data to update sub_district with.
        sub_district_service (SubDistrictService): The sub_district service to use.

    Returns:
        ResponseSchema: The response data.
    """
    sub_district = sub_district_service.update(sub_district_id=sub_district_id, data_to_update=data_to_update)

    response_data = ResponseSchema(
        status=HTTPResponseStatus.SUCCESS.value,
        status_code=status.HTTP_200_OK,
        message=SuccessMessages.updated_successfully(object_type=SubDistrict),  # type: ignore
        data=ReadSubDistrictSchema(**sub_district.to_dict()),  # type: ignore
        request=request,
    )

    return response_data


@sub_district_router.delete(
    path="/{sub_district_id}", status_code=status.HTTP_200_OK, description=delete_sub_district_docs
)
def delete_sub_district(
    request: Request,
    sub_district_id: Annotated[str, Path(..., description="The id of the sub_district to get.")],
    sub_district_service: Annotated[SubDistrictService, Depends(create_sub_district_service)],
) -> ResponseSchema:
    """Method for handling delete a sub_district by id request.

    Args:
        request (Request): The request object.
        sub_district_id (str): The id of the sub_district to delete.
        sub_district_service (SubDistrictService): The sub_district service to use.

    Returns:
        ResponseSchema: The response data.
    """
    sub_district = sub_district_service.delete(entity_id=sub_district_id)

    response_data = ResponseSchema(
        status=HTTPResponseStatus.SUCCESS.value,
        status_code=status.HTTP_200_OK,
        message=SuccessMessages.deleted_successfully(object_type=SubDistrict),  # type: ignore
        data=ReadSubDistrictSchema(**sub_district.to_dict()),  # type: ignore
        request=request,
    )

    return response_data


@sub_district_router.patch(
    path="/{sub_district_id}/restore", status_code=status.HTTP_200_OK, description=restore_sub_district_docs
)
def restore_sub_district(
    request: Request,
    sub_district_id: Annotated[str, Path(..., description="The id of the sub_district to get.")],
    sub_district_service: Annotated[SubDistrictService, Depends(create_sub_district_service)],
) -> ResponseSchema:
    """Method for handling restore a sub_district by id request.

    Args:
        request (Request): The request object.
        sub_district_id (str): The id of the sub_district to restore.
        sub_district_service (SubDistrictService): The sub_district service to use.

    Returns:
        ResponseSchema: The response data.
    """
    sub_district = sub_district_service.restore(entity_id=sub_district_id)

    response_data = ResponseSchema(
        status=HTTPResponseStatus.SUCCESS.value,
        status_code=status.HTTP_200_OK,
        message=SuccessMessages.restored_successfully(object_type=SubDistrict),  # type: ignore
        data=ReadSubDistrictSchema(**sub_district.to_dict()),  # type: ignore
        request=request,
    )

    return response_data
