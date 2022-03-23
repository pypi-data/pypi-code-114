from __future__ import annotations

from pydantic import BaseModel

from .common import Base


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class ApiTokenRequest(Base):
    name: str


class ApiTokenResponse(Base):
    token: str
