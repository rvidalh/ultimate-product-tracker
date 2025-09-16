from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.base import get_db
from app.models.auth import Role, User, UserRole
from app.repositories.auth.protocols import AuthProtocol


class SqlAlchemyAuthRepository(AuthProtocol):

    def __init__(self, session: Session):
        self.session = session

    async def get_by_id(self, user_id: int) -> User | None:
        """
        Retrieve an active user by their ID.

        Args:
            user_id (int): The unique identifier of the user to retrieve.

        Returns:
            User | None: The User object if found and active, otherwise None.
        """
        return (
            self.session.query(User)
            .filter(User.id == user_id, User.is_active == True)  # noqa: E712
            .first()
        )

    async def get_by_email(self, email: str) -> User | None:
        """
        Retrieve an active user by their email address.

        Args:
            email (str): The email address of the user to retrieve.

        Returns:
            User | None: The User object if found and active, otherwise None.
        """
        return (
            self.session.query(User)
            .filter(User.email == email, User.is_active == True)  # noqa: E712
            .first()
        )

    async def create(self, user: User) -> User:
        """
        Create a new user in the database.

        Args:
            user (User): The user instance to be added to the database.

        Returns:
            User: The newly created user instance with
            updated fields (e.g., id).

        Raises:
            sqlalchemy.exc.SQLAlchemyError: If there is an error during the
            database operation.
        """
        try:
            user_role = (
                self.session.query(Role).filter(Role.name == "user").first()
            )
            if not user_role:
                raise ValueError("Default 'user' role not found in database")

            self.session.add(user)
            self.session.flush()

            user_role_association = UserRole(
                user_id=user.id, role_id=user_role.id
            )
            self.session.add(user_role_association)
            self.session.commit()
            self.session.refresh(user)
            return user
        except Exception as e:
            self.session.rollback()
            raise e

    async def update(self, user: User) -> User:
        """
        Update an existing user in the database.

        Args:
            user (User): The user instance to update in the database.

        Returns:
            User: The updated user instance.
        """
        self.session.merge(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    async def delete(self, user_id: int) -> None:
        """
        Deactivates a user by setting their 'is_active' attribute to False.

        Args:
            user_id (int): The unique identifier of the user to deactivate.

        Returns:
            None
        """
        user = self.session.get(User, user_id)
        if user:
            user.is_active = False
            self.session.commit()
            self.session.refresh(user)


async def get_auth_repository(db: Session = Depends(get_db)) -> AuthProtocol:
    return SqlAlchemyAuthRepository(session=db)
