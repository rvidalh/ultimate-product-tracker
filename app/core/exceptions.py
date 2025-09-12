# exceptions/auth_exceptions.py
class AuthException(Exception):
    """Base auth exception"""

    pass


class EmailAlreadyExistsException(AuthException):
    """Raised when trying to register with existing email"""

    def __init__(self, email: str):
        self.email = email
        super().__init__(f"Email {email} already registered")
