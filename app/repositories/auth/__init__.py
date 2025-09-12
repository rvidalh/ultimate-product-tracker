from app.repositories.auth.protocols import AuthProtocol
from app.repositories.auth.repositories import get_auth_repository

__all__ = ["get_auth_repository", "AuthProtocol"]
