# pylint: disable=missing-module-docstring


from typing import TYPE_CHECKING

from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from tanzanite.backend.app.app.db.base_class import Base

if TYPE_CHECKING:
    from .challenge import Base  # noqa: F811


class User(Base):
    """User model."""
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_proctor = Column(Boolean(), default=False)
    is_superuser = Column(Boolean(), default=False)
    # TODO(dittrich): back populate 'participant'(?) instead of 'owner'
    challenges = relationship("Challenge", back_populates="owner")
