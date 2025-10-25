from typing import Annotated

from fastapi import APIRouter, Body, Depends, Request, status

from app.auth.dependencies.auth_service_dependency import create_auth_service
from app.auth.docs.auth_docs import register_user_docs
from app.auth.services.auth_service import AuthService
from app.core.schemas.base_entity_response_schema import ResponseSchema
from app.core.utils.constants import HTTPResponseStatus
from app.core.utils.messages import SuccessMessages
from app.users.models import User
from app.users.schemas.request.user import CreateUserRequestSchema
from app.users.schemas.response.user import ReadUserSchema

auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post(path="/register", status_code=status.HTTP_201_CREATED, description=register_user_docs)
async def register_user(
    request: Request,
    auth_service: Annotated[AuthService, Depends(create_auth_service)],
    user_data: Annotated[
        CreateUserRequestSchema, Body(..., description="Schema for the data when registering a user.")
    ],
) -> ResponseSchema:
    """Method for handling get all auths request.

    Args:
        request (Request): The request object.
        auth_service (AuthService): The auth service to use.
        user_data (CreateUserRequestSchema): The data for registering the user.

    Returns:
        ResponseSchema: The response data.
    """
    new_user = await auth_service.register_user(user_data=user_data)
    response_data = ResponseSchema(
        status=HTTPResponseStatus.SUCCESS.value,
        status_code=status.HTTP_201_CREATED,
        message=SuccessMessages.created_successfully(  # type: ignore
            object_type=User, extra_info="Check your email to verify your account."
        ),
        data=ReadUserSchema(**new_user.to_dict()),  # type: ignore
        request=request,
    )

    return response_data
