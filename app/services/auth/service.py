from fastapi import Depends

from app.core.exceptions import EmailAlreadyExistsException
from app.models.auth import User
from app.schemas.auth.schemas import (
    CreateUserSchema,
    LoginSchema,
    TokenDataSchema,
    TokenSchema,
)
from app.services.user.service import UserService, get_user_service
from app.utils.security import Security


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    async def register_user(self, user_data: CreateUserSchema) -> User:
        existing_user = await self.user_service.get_user_by_email(
            email=user_data.email
        )
        if existing_user:
            raise EmailAlreadyExistsException(email=user_data.email)
        return await self.user_service.create_user(user=user_data)

    async def authenticate_user(self, user_data: LoginSchema) -> User | None:
        user = await self.user_service.get_user_by_email(email=user_data.email)
        if (
            user
            and user.hashed_password is not None
            and Security.verify_password(
                user_data.password, user.hashed_password
            )
        ):
            return user
        return None

    async def create_token(self, user: User) -> TokenSchema:
        token_data = {"sub": user.email}
        access_token = Security.create_access_token(data=token_data)
        return TokenSchema(access_token=access_token, token_type="bearer")

    async def get_current_user(
        self, token: dict = Depends(Security.verify_token)
    ) -> TokenDataSchema:
        payload = token
        email: str | None = payload.get("sub", None)
        return TokenDataSchema(email=email)


def get_auth_service(
    user_service: UserService = Depends(get_user_service),
) -> AuthService:
    return AuthService(user_service=user_service)
