from fastapi import Depends

from app.schemas import TokenDataSchema
from app.services import AuthService, get_auth_service
from app.utils.security import Security


async def get_current_user(
    token: dict = Depends(Security.verify_token),
    auth_service: AuthService = Depends(get_auth_service),
) -> TokenDataSchema:
    """
    Dependency that returns the current authenticated user.
    """
    return await auth_service.get_current_user(token)
