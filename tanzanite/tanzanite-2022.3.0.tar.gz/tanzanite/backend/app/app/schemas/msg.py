# -*- coding: utf-8 -*-

"""
Schemas for messages.
"""


from pydantic import BaseModel  # pylint: disable=no-name-in-module


class Msg(BaseModel):
    """Message base model."""
    msg: str


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
