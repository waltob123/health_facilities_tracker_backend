from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError

from app.auth.routes.api.v1.permission_routes import permission_router
from app.auth.routes.api.v1.role_routes import role_router
from app.core.handlers.exceptions import (
    http_exception_handler,
    validation_exception_handler,
    value_error_exception_handler,
)
from app.core.routes.root import root_api_router
from app.core.utils.constants import ApplicationConstants
from app.locations.routes.api.v1.district_routes import district_router
from app.locations.routes.api.v1.facility_routes import facility_router
from app.locations.routes.api.v1.region_routes import region_router
from app.locations.routes.api.v1.sub_district_routes import sub_district_router

app = FastAPI(
    title=ApplicationConstants.APP_NAME.value,
    description=ApplicationConstants.DESCRIPTION.value,
    redirect_slashes=True,
    docs_url="/api/documentation",
    openapi_url="/api/openapi.json",
    redoc_url="/api/redoc",
)

app_v1 = FastAPI(
    title=ApplicationConstants.APP_NAME.value,
    description=ApplicationConstants.DESCRIPTION.value,
    redirect_slashes=True,
    docs_url="/documentation",
    openapi_url="/openapi.json",
    redoc_url="/redoc",
)

##################################################################################
#                                                                                #
#                     ADD YOUR EXCEPTION HANDLERS HERE                           #
#                                                                                #
##################################################################################
app_v1.add_exception_handler(HTTPException, http_exception_handler)  # type: ignore
app_v1.add_exception_handler(RequestValidationError, validation_exception_handler)  # type: ignore
app_v1.add_exception_handler(ValueError, value_error_exception_handler)  # type: ignore

##################################################################################
#                                                                                #
#                            ADD YOUR ROUTERS HERE                               #
#                                                                                #
##################################################################################
app_v1.include_router(root_api_router)
app_v1.include_router(role_router)
app_v1.include_router(permission_router)
app_v1.include_router(region_router)
app_v1.include_router(district_router)
app_v1.include_router(sub_district_router)
app_v1.include_router(facility_router)

##################################################################################
#                                                                                #
#                            ADD APP MOUNTS HERE                               #
#                                                                                #
##################################################################################
app.mount(ApplicationConstants.API_V1_STR.value, app_v1)
