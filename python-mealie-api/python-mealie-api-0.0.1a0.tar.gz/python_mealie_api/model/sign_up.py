from __future__ import annotations

from .common import Base, User


class SignUp(Base):
    name: str
    admin: bool
    token: str
    id: int


class CreateSignUpRequest(User):
    password: str


class CreateSignUpTokenRequest(Base):
    name: str
    admin: bool


class CreateSignUpTokenResponse(Base):
    name: str
    admin: bool
    token: str
