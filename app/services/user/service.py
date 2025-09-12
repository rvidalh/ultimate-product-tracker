from fastapi import Depends

from app.models.auth import User
from app.repositories.auth import AuthProtocol, get_auth_repository
from app.schemas import CreateUserSchema
from app.utils.security import Security


class UserService:
    def __init__(self, auth_repo: AuthProtocol):
        self.auth_repo = auth_repo

    async def create_user(self, user: CreateUserSchema) -> User:
        user_data = user.model_dump()
        user_data["password"] = Security.hash_password(user_data["password"])
        return await self.auth_repo.create(User(**user_data))

    async def get_user_by_email(self, email: str) -> User | None:
        return await self.auth_repo.get_by_email(email)

    async def get_user_by_id(self, user_id: int) -> User | None:
        return await self.auth_repo.get_by_id(user_id)


async def get_user_service(
    auth_repo: AuthProtocol = Depends(get_auth_repository),
) -> UserService:
    return UserService(auth_repo=auth_repo)
