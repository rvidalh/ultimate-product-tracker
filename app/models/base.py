from sqlalchemy import Column, DateTime, Integer, func

from app.db import Base


class TimestampMixin:
    """Mixin to add created_at and updated_at timestamps to models"""

    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, default=func.now(), onupdate=func.now(), nullable=False
    )


class BaseModel(Base):
    """Abstract base model with common fields"""

    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
