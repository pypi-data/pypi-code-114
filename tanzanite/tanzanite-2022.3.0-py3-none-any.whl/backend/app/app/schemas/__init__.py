# -*- coding: utf-8 -*-

"""
Schemas initializer.
"""


# flake8: noqa
from .challenge import (
    Challenge,
    ChallengeCreate,
    ChallengeInDB,
    ChallengeUpdate,
)
from .msg import Msg
from .token import (
    Token,
    TokenPayload,
)
from .user import (
    User,
    UserCreate,
    UserInDB,
    UserUpdate,
)


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
