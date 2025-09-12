from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class CreateUserSchema(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None


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
