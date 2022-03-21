# -*- coding: utf-8 -*-

"""
Tanzanite webapp user routes.
"""

# Standard imports
import logging

# External imports
from fastapi import (
    APIRouter,
    Depends,
    Request,
    responses,
    status,
)
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

# Local imports
from tanzanite.backend.app.app import (
    crud,
    models,
    schemas,
)
from tanzanite.backend.app.app.api import deps
from tanzanite.webapps import response_page
from tanzanite.webapps.users.forms import UserCreateForm


router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/register/")
def register_form(request: Request):
    """
    Produce registration form via the webapp.
    """
    return response_page(
        "users/register.html",
        request=request,
        msg="Go ahead and register"
    )


@router.post("/register/")
async def register(
    request: Request,
    db: Session = Depends(deps.get_db)
):
    """
    Register a new user via the webapp.
    """
    form = UserCreateForm(request)
    await form.load_data()
    if await form.is_valid():
        user = schemas.UserCreate(
            # email=form.username,
            email=form.email,
            # shell_login=form.shell_login,
            password=form.password,
            is_superuser=False
        )
        try:
            # user = create_new_user(user=user, db=db)
            user = crud.user.create(db=db, obj_in=user)
            # Default is POST request. To use GET request,
            # use status code HTTP_302_FOUND instead of
            # HTTP_307_REDIRECT.
            return responses.RedirectResponse(
                "/?msg=Successfully%20Registered",
                status_code=status.HTTP_302_FOUND
            )
        except IntegrityError:
            form.__dict__.get("errors").append(
                "Duplicate username or shell_login"
            )
            return response_page(
                "users/register.html",
                request=request,
                **form.__dict__
            )
    return response_page(
        "users/register.html",
        request=request,
        **form.__dict__,
    )


@router.get("/users", response_class=JSONResponse)
async def list_users(
    request: Request,
    skip: int = 0,
    limit: int = 0,
    user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db)
):
    """
    List users from the database.
    """
    logger.debug('[+] GET routed to list_users()')
    db_users = crud.user.get_multi(db, skip=skip, limit=limit)
    users = [
        schemas.User(**jsonable_encoder(user)).dict()
        for user in db_users
    ]
    return response_page(
        "users/show_users.html",
        request=request,
        user=user,
        users=users
    )

# vim: set ts=4 sw=4 tw=0 et :
