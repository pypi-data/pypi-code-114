# -*- coding: utf-8 -*-


"""
Tanzanite webapp base.

This is where routes for the front-end webapp GUI are defined.
"""

# External imports
from fastapi import APIRouter

# Local imports
from tanzanite.webapps.auth import route_login
from tanzanite.webapps.challenges import route_challenges
from tanzanite.webapps.users import route_users


api_router = APIRouter()
api_router.include_router(
    route_login.router,
    prefix="",
    tags=["auth-webapp"]
)
api_router.include_router(
    route_challenges.router,
    prefix="",
    tags=["challenge-webapp"]
)
api_router.include_router(
    route_users.router,
    prefix="",
    tags=["users-webapp"]
)


# vim: set ts=4 sw=4 tw=0 et :
