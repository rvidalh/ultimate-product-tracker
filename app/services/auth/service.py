from fastapi import Depends

from app.core.exceptions import EmailAlreadyExistsException
from app.models.auth import User
from app.schemas.auth.schemas import CreateUserSchema
from app.services.user.service import UserService, get_user_service


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    async def register_user(self, user_data: CreateUserSchema) -> User:
        # Example method to register a user
        existing_user = await self.user_service.get_user_by_email(
            email=user_data.email
        )
        if existing_user:
            raise EmailAlreadyExistsException(email=user_data.email)
        return await self.user_service.create_user(user=user_data)


def get_auth_service(
    user_service: UserService = Depends(get_user_service),
) -> AuthService:
    return AuthService(user_service=user_service)
