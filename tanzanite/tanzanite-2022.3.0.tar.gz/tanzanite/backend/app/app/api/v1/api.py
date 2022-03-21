# pylint: disable=missing-module-docstring


from fastapi import APIRouter

from tanzanite.backend.app.app.api.v1.endpoints import (
    challenges,
    login,
    users,
    utils,
)
from tanzanite.core.config import settings

api_router = APIRouter()
prefix = f"/{settings.API_PATH}"
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix=f"{prefix}/users", tags=["users"])  # noqa
api_router.include_router(utils.router, prefix=f"{prefix}/utils", tags=["utils"])  # noqa
api_router.include_router(challenges.router, prefix=f"{prefix}/challenges", tags=["challenges"])  # noqa
