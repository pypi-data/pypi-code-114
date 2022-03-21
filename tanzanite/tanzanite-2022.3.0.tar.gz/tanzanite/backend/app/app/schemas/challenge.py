# -*- coding: utf-8 -*-

"""
Schemas for challenges.
"""

# Standard imports
from datetime import datetime
from typing import Optional


# External imports
from pydantic import (  # pylint: disable=no-name-in-module
    BaseModel,
)


class ChallengeBase(BaseModel):
    """
    Schema with shared properties.
    """
    title: Optional[str] = None
    author: Optional[str] = None
    url: Optional[str] = None
    description: Optional[str] = None
    date_posted: Optional[str] = datetime.today()


# Properties to receive on challenge creation
class ChallengeCreate(ChallengeBase):
    """Schema used to validate data while creating a Challenge."""
    title: str
    author: str
    description: str
    date_posted: str


# Properties to receive on challenge update
class ChallengeUpdate(ChallengeBase):
    """
    Schema used to validate data while updating a Challenge.
    """
    title: Optional[str] = None
    author: Optional[str] = None
    owner_id: Optional[int] = None
    url: Optional[str] = None
    description: Optional[str] = None


# Properties shared by models stored in DB
class ChallengeInDBBase(ChallengeBase):
    """
    Schema for validating Challenge data in database record.
    """
    id: Optional[int] = None
    owner_id: Optional[int] = None

    class Config:
        """Config class"""
        orm_mode = True


# Additional properties to return via API
class Challenge(ChallengeInDBBase):
    """
    Schema for data returned to client.
    """


# Additional properties stored in DB
class ChallengeInDB(ChallengeInDBBase):
    """
    Schema for properties stored in database.
    """


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
