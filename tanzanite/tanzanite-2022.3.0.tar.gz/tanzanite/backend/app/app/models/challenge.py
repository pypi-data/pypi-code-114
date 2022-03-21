# -*- coding: utf-8 -*-

"""
Challenge models.
"""

from typing import TYPE_CHECKING

from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from tanzanite.backend.app.app.db.base_class import Base

if TYPE_CHECKING:
    from .user import Base  # noqa: F811


# TODO(dittrich): Keep this in sync with `backend/app/alembic/versions/*.py`
class Challenge(Base):
    """Challenge model."""
    id = Column(Integer(), primary_key=True, index=True, nullable=False)
    title = Column(String(length=100), unique=True, index=True, nullable=False)
    author = Column(String(length=100), nullable=False)
    url = Column(String(length=256), nullable=False)
    description = Column(String(length=1024), nullable=False)
    date_posted = Column(String(length=10), nullable=True)
    is_active = Column(Boolean(), nullable=False, default=True)
    owner_id = Column(Integer(), ForeignKey("user.id"))
    owner = relationship("User", back_populates="challenges")


# vim: set ts=4 sw=4 tw=0 et :
