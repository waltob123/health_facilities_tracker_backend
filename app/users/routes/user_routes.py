from typing import Annotated, Optional

from fastapi import APIRouter, Depends, Path, Query, Request, status

from app.core.schemas.base_entity_response_schema import ResponseSchema
from app.core.utils.constants import HTTPResponseStatus
from app.core.utils.messages import SuccessMessages
from app.users.dependencies.user_service_dependency import create_user_service
from app.users.docs.users_docs import (
    delete_user_docs,
    get_all_users_docs,
    get_user_by_id_docs,
    restore_user_docs,
    update_user_docs,
)
from app.users.models import User
from app.users.schemas.request.user_profile import UpdateUserProfileRequestSchema
from app.users.schemas.response.user import ReadUserSchema
from app.users.services.user_service import UserService

user_router = APIRouter(prefix="/users", tags=["User"])


@user_router.get(path="", status_code=status.HTTP_200_OK, description=get_all_users_docs)
def get_all_users(
    request: Request,
    user_service: Annotated[UserService, Depends(create_user_service)],
    filters: Annotated[Optional[str], Query(..., description="Filters query parameter")] = None,
    sort: Annotated[Optional[str], Query(..., description="Sort query parameter")] = None,
    pagination: Annotated[Optional[str], Query(..., description="Pagination query parameter")] = None,
) -> ResponseSchema:
    """Method for handling get all users request.

    Args:
        request (Request): The request object.
        filters (str): The filters query parameter
        sort (str): The sort query parameter
        pagination (str): The pagination query parameter
        user_service (UserService): The user service to use.

    Returns:
        ResponseSchema: The response data.
    """
    extras: dict = {}
    users = user_service.get_all(pagination=pagination, filters=filters, sort=sort)
    extras.update({"pagination": user_service.get_pagination_extras(request=request)})
    extras["pagination"].update({"total_retrieved": len(users)})

    response_data = ResponseSchema(
        status=HTTPResponseStatus.SUCCESS.value,
        status_code=status.HTTP_200_OK,
        message=SuccessMessages.retrieved_successfully(object_type=User),  # type: ignore
        data=list(map(lambda user: ReadUserSchema(**user.to_dict()), users)),  # type: ignore
        extras=extras,
        request=request,
    )

    return response_data


@user_router.get(path="/{user_id}", status_code=status.HTTP_200_OK, description=get_user_by_id_docs)
def get_user_by_id(
    request: Request,
    user_id: Annotated[str, Path(..., description="The id of the user to get.")],
    user_service: Annotated[UserService, Depends(create_user_service)],
) -> ResponseSchema:
    """Method for handling get a user by id request.

    Args:
        request (Request): The request object.
        user_id (str): The id of the user to retrieve.
        user_service (UserService): The user service to use.

    Returns:
        ResponseSchema: The response data.
    """
    user = user_service.get_by_id(entity_id=user_id)

    response_data = ResponseSchema(
        status=HTTPResponseStatus.SUCCESS.value,
        status_code=status.HTTP_200_OK,
        message=SuccessMessages.retrieved_successfully(object_type=User),  # type: ignore
        data=ReadUserSchema(**user.to_dict()),  # type: ignore
        request=request,
    )

    return response_data


@user_router.put(path="/{user_id}", status_code=status.HTTP_200_OK, description=update_user_docs)
def update_user(
    request: Request,
    user_id: Annotated[str, Path(..., description="The id of the user to get.")],
    data_to_update: UpdateUserProfileRequestSchema,
    user_service: Annotated[UserService, Depends(create_user_service)],
) -> ResponseSchema:
    """Method for handling update a user by id request.

    Args:
        request (Request): The request object.
        user_id (str): The id of the user to update.
        data_to_update (UpdateUserProfileRequestSchema): The data to update user with.
        user_service (UserService): The user service to use.

    Returns:
        ResponseSchema: The response data.
    """
    user = user_service.update(user_id=user_id, data_to_update=data_to_update)

    response_data = ResponseSchema(
        status=HTTPResponseStatus.SUCCESS.value,
        status_code=status.HTTP_200_OK,
        message=SuccessMessages.updated_successfully(object_type=User),  # type: ignore
        data=ReadUserSchema(**user.to_dict()),  # type: ignore
        request=request,
    )

    return response_data


@user_router.delete(path="/{user_id}", status_code=status.HTTP_200_OK, description=delete_user_docs)
def delete_user(
    request: Request,
    user_id: Annotated[str, Path(..., description="The id of the user to get.")],
    user_service: Annotated[UserService, Depends(create_user_service)],
) -> ResponseSchema:
    """Method for handling delete a user by id request.

    Args:
        request (Request): The request object.
        user_id (str): The id of the user to delete.
        user_service (UserService): The user service to use.

    Returns:
        ResponseSchema: The response data.
    """
    user = user_service.delete(entity_id=user_id)

    response_data = ResponseSchema(
        status=HTTPResponseStatus.SUCCESS.value,
        status_code=status.HTTP_200_OK,
        message=SuccessMessages.deleted_successfully(object_type=User),  # type: ignore
        data=ReadUserSchema(**user.to_dict()),  # type: ignore
        request=request,
    )

    return response_data


@user_router.patch(path="/{user_id}/restore", status_code=status.HTTP_200_OK, description=restore_user_docs)
def restore_user(
    request: Request,
    user_id: Annotated[str, Path(..., description="The id of the user to get.")],
    user_service: Annotated[UserService, Depends(create_user_service)],
) -> ResponseSchema:
    """Method for handling restore a user by id request.

    Args:
        request (Request): The request object.
        user_id (str): The id of the user to restore.
        user_service (UserService): The user service to use.

    Returns:
        ResponseSchema: The response data.
    """
    user = user_service.restore(entity_id=user_id)

    response_data = ResponseSchema(
        status=HTTPResponseStatus.SUCCESS.value,
        status_code=status.HTTP_200_OK,
        message=SuccessMessages.restored_successfully(object_type=User),  # type: ignore
        data=ReadUserSchema(**user.to_dict()),  # type: ignore
        request=request,
    )

    return response_data
