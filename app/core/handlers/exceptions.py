from fastapi import HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.core.schemas.base_entity_response_schema import ResponseSchema
from app.core.utils.constants import HTTPResponseStatus


async def http_exception_handler(request: Request, exception: HTTPException) -> JSONResponse:
    """Custom exception handler for HTTP exceptions.

    Args:
        request (Request): The request object.
        exception (HTTPException): the HTTPException object.

    Returns:
        JSONResponse: The JSON response with the error message.
    """
    return ResponseSchema(
        request=request,
        status=HTTPResponseStatus.ERROR.value,
        status_code=exception.status_code,  # type: ignore
        message=exception.detail,  # type: ignore
    ).to_json_response()


async def validation_exception_handler(request: Request, exception: RequestValidationError) -> JSONResponse:
    """Custom exception handler for RequestValidationError.

    Args:
        request (Request): The request object.
        exception (RequestValidationError): The RequestValidationError object.

    Returns:
        JSONResponse: The JSON response with the error message.
    """
    # Parse the validation errors to get missing attributes and invalid data
    missing_attrs = []
    invalid_data = []

    # Combine all error messages into a single string
    errors = ""

    # Get the types of errors
    _types = [error["type"] for error in exception.errors()]

    # Iterate through the error types and categorize them
    for type_ in range(len(_types)):
        # Check if the error type is "missing" or "value_error"
        if _types[type_] == "missing":
            missing_attrs.append(exception.errors()[type_]["loc"][1])
        if _types[type_] == "value_error":
            invalid_data.append(exception.errors()[type_]["msg"])

    # Create the error message
    if missing_attrs:
        errors = errors + f"Fields required: {missing_attrs}"

    if invalid_data:
        errors = errors + f"\nInvalid data: {invalid_data}"

    return ResponseSchema(
        request=request,
        status=HTTPResponseStatus.ERROR.value,
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        message=errors,  # type: ignore
    ).to_json_response()


async def value_error_exception_handler(request: Request, exception: ValueError) -> JSONResponse:
    """Custom exception handler for ValueError.

    Args:
        request (Request): The request object.
        exception (ValueError): The ValueError object.

    Returns:
        JSONResponse: The JSON response with the error message.
    """
    return ResponseSchema(
        request=request,
        status=HTTPResponseStatus.ERROR.value,
        status_code=status.HTTP_400_BAD_REQUEST,
        message=str(exception),  # type: ignore
    ).to_json_response()
