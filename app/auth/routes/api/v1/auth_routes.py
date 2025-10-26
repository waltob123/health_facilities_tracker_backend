from typing import Annotated

from fastapi import APIRouter, Body, Depends, Request, status

from app.auth.dependencies.auth_service_dependency import create_auth_service
from app.auth.docs.auth_docs import register_user_docs, resend_account_verification_link_docs, verify_account_docs
from app.auth.schemas.request.auth import AccountVerificationTokenSchema, EmailSchema
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
    """Method for handling registering a user request.

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


@auth_router.post(path="/verify-account", status_code=status.HTTP_200_OK, description=verify_account_docs)
def verify_account(
    request: Request,
    auth_service: Annotated[AuthService, Depends(create_auth_service)],
    verify_token_data: Annotated[AccountVerificationTokenSchema, Body(..., description="Schema for the token data.")],
) -> ResponseSchema:
    """Method for handling verifying account request.

    Args:
        request (Request): The request object.
        auth_service (AuthService): The auth service to use.
        verify_token_data (AccountVerificationTokenSchema): The token data for verifying the account.

    Returns:
        ResponseSchema: The response data.
    """
    verified_user_response = auth_service.verify_account(token_data=verify_token_data)

    response_data = ResponseSchema(
        status=HTTPResponseStatus.SUCCESS.value,
        status_code=status.HTTP_201_CREATED,
        message=verified_user_response.message,  # type: ignore
        data=verified_user_response.model_dump(),  # type: ignore
        request=request,
    )

    return response_data


@auth_router.post(
    path="/resend-account-verification-link",
    status_code=status.HTTP_200_OK,
    description=resend_account_verification_link_docs,
)
async def resend_account_verification_link(
    request: Request,
    auth_service: Annotated[AuthService, Depends(create_auth_service)],
    resend_account_verification_request_data: Annotated[
        EmailSchema, Body(..., description="Schema for resend account verification.")
    ],
) -> ResponseSchema:
    """Method for handling resending account verification link request.

    Args:
        request (Request): The request object.
        auth_service (AuthService): The auth service to use.
        resend_account_verification_request_data (AccountVerificationTokenSchema): \
        The data for needed to resend the account verification link..

    Returns:
        ResponseSchema: The response data.
    """
    verified_user_response = await auth_service.resend_account_verification_email(
        resend_account_verification_email_data=resend_account_verification_request_data
    )

    response_data = ResponseSchema(
        status=HTTPResponseStatus.SUCCESS.value,
        status_code=status.HTTP_201_CREATED,
        message=verified_user_response,  # type: ignore
        data={},  # type: ignore
        request=request,
    )

    return response_data
