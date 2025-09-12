from typing import Protocol

from app.models.auth import User


class AuthProtocol(Protocol):
    async def get_by_id(self, user_id: int) -> User | None:
        """Retrieve a user by their ID from the database."""
        raise NotImplementedError

    async def get_by_email(self, email: str) -> User | None:
        """Retrieve a user by their email from the database."""
        raise NotImplementedError

    async def create(self, user: User) -> User:
        """Create a new user in the database."""
        raise NotImplementedError

    async def update(self, user: User) -> User:
        """Update an existing user in the database."""
        raise NotImplementedError

    async def delete(self, user_id: int) -> None:
        """Delete a user from the database."""
        raise NotImplementedError
