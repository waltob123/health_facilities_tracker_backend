from datetime import datetime, timezone
from typing import Optional

from fastapi import Request
from fastapi_mail.errors import ConnectionErrors

from app.auth.config.auth_config import auth_config
from app.auth.schemas.mail_body import AccountVerificationTemplateBodySchema
from app.auth.services.token_service import TokenService
from app.auth.utils.hash_password import PasswordHashManager
from app.core.base_service import BaseService
from app.core.config.project_config import project_config
from app.core.mail_service import MailServiceBuilder
from app.core.utils.constants import ApplicationConstants
from app.users.models import User
from app.users.repositories.user_repository import UserRepository
from app.users.schemas.request.user import CreateUserRequestSchema, CreateUserSchema
from app.users.schemas.request.user_profile import CreateUserProfileSchema


class AuthService(BaseService[User]):
    """The service class for 'user'."""

    def __init__(
        self,
        *,
        user_repository: UserRepository,
        user_profile_service: BaseService,
        facility_service: BaseService,
        role_service: BaseService,
        password_hash_manager: PasswordHashManager,
        mail_service: MailServiceBuilder,
        token_service: TokenService,
    ) -> None:
        """Initializer for 'user' service.

        Args:
            user_repository (UserRepository): The user repository.
            user_profile_service (BaseService): The user profile service.
            facility_service (BaseService): The facility service.
            role_service (BaseService): The role service.
            password_hash_manager (PasswordHashManager): The manager for hashing and verifying passwords.
            mail_service (MailServiceBuilder): The mailing service.
            token_service (TokenService): The token service.
        """
        self.user_repository = user_repository
        self.user_profile_service = user_profile_service
        self.facility_service = facility_service
        self.role_service = role_service
        self.password_hash_manager = password_hash_manager
        self.mail_service = mail_service
        self.token_service = token_service
        super().__init__(main_repository=user_repository)

    async def register_user(self, *, user_data: CreateUserRequestSchema) -> User:
        """Create a new user.

        Args:
            user_data (CreateUserSchema): The user data to create.

        Returns:
            User: The newly created user.
        """
        # check if roles exist.
        for role_id in user_data.role_ids:
            _ = self.role_service.get_by_id(entity_id=role_id)

        # check if facility exist.
        if user_data.user_profile.facility_id:
            _ = self.facility_service.get_by_id(entity_id=user_data.user_profile.facility_id)

        # user schema
        new_user_schema = CreateUserSchema(
            email=str(user_data.email),
            password_hash=self.password_hash_manager.hash_password(password=user_data.password),
            role_ids=user_data.role_ids,
        )

        # create user
        user = self._default_create(
            entity_schema=new_user_schema, unique_field_to_check="email", unique_field_value=str(new_user_schema.email)
        )

        # create user profile
        user_profile_schema = CreateUserProfileSchema(**user_data.user_profile.model_dump(), user_id=user.id)  # type: ignore
        user_profile = self.user_profile_service.create(user_profile_data=user_profile_schema)

        # create verification token
        verification_token = self.token_service.create_token(
            payload={"sub": user.id, "iss": ApplicationConstants.APP_NAME.value},
            expires_in_minutes=auth_config.VERIFICATION_LINK_EXPIRES_IN_MINUTES,
        )

        # create verification link
        verification_link = f"{project_config.FRONTEND_URL}/auth/verify-account?token={verification_token}"

        # send the email
        body = AccountVerificationTemplateBodySchema(
            app_name=ApplicationConstants.APP_NAME.value,
            first_name=user_profile.first_name,
            title="User Account Verification",
            code_expires_in_hours=24,
            current_year=datetime.now(tz=timezone.utc).year,
            verification_url=verification_link,
        ).model_dump()

        (
            self.mail_service.subject(subject="Account Creation")
            .recipients(recipients=[user.email])  # type: ignore
            .template(template_name="account_creation.html")
            .body(body=body)
        )

        try:
            await self.mail_service.send_mail()
        except ConnectionErrors:
            await self.mail_service.send_mail()

        return user

    # def change_user_role(self, *, user_id: str, role_data: UpdateUserRoleSchema) -> User:
    #     """Change a user's role."""

    def create(self, *args, **kwargs) -> User:  # type: ignore
        """Create a user"""
        raise NotImplementedError

    def update(self, *args, **kwargs) -> User:  # type: ignore
        """Update a user."""
        raise NotImplementedError

    def get_all(
        self, *, pagination: Optional[str] = None, filters: Optional[str] = None, sort: Optional[str] = None
    ) -> list[User]:
        """Get all entities"""
        raise NotImplementedError

    def delete(self, *, entity_id: str) -> User:
        """Delete an entity."""
        raise NotImplementedError

    def get_by_id(self, *, entity_id: str) -> User:
        """Get an entity by id."""
        raise NotImplementedError

    def get_total_pages(self, pagination: Optional[str]) -> int:
        """Get total pages."""
        raise NotImplementedError

    def get_pagination_extras(self, request: Request) -> dict:
        """Get pagination extras"""
        raise NotImplementedError

    def get_total_number(self) -> int:
        """Get total number"""
        raise NotImplementedError

    def restore(self, *, entity_id: str) -> User:
        """Restore entity"""
        raise NotImplementedError
