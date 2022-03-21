# -*- coding: utf-8 -*-

"""
Schemas for users.
"""

# pylint: disable=missing-class-docstring


from typing import Optional

from pydantic import (  # pylint: disable=no-name-in-module
    BaseModel,
    EmailStr,
)


class UserBase(BaseModel):
    """
    Schema with shared properties.
    """
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_proctor: bool = False
    is_superuser: bool = False
    full_name: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    """
    Schema used to validate data while creating a User.
    """
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    """
    Schema used to validate data while updating a User.
    """
    password: Optional[str] = None


# Properties shared by models stored in DB
class UserInDBBase(UserBase):
    """
    Schema for validating User data in database record.
    """
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    """
    Schema for data returned to client.
    """


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    """
    Schema for properties stored in database.
    """
    hashed_password: str


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
