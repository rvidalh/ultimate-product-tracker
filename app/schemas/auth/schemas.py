from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class CreateUserSchema(BaseModel):
    """Schema for creating a new user"""

    email: EmailStr
    username: Optional[str] = None
    hashed_password: str = Field(alias="password")
    full_name: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class UserSchema(BaseModel):
    """Schema for user responses"""

    id: int
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime | None = None
    last_login: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class LoginSchema(BaseModel):
    """Schema for user login"""

    email: EmailStr
    password: str


class TokenSchema(BaseModel):
    """Schema for authentication tokens"""

    access_token: str
    token_type: str


class TokenDataSchema(BaseModel):
    """Schema for token data"""

    email: Optional[str] = None
