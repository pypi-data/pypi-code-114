# -*- coding: utf-8 -*-

"""
Schemas for tokens.
"""


from typing import Optional

from pydantic import BaseModel  # pylint: disable=no-name-in-module


class Token(BaseModel):
    """Token base model."""
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    """Token payload model."""
    sub: Optional[int] = None


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
