# -*- coding: utf-8 -*-

"""
Webapp routes related to logging in.
"""

# Standard imports
import logging
import traceback


# External imports
import jinja2.exceptions
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Request,
    responses,
)
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session


# Local imports
from tanzanite.backend.app.app import crud
# from tanzanite.backend.app.app import models
from tanzanite.backend.app.app.api import deps
from tanzanite.backend.app.app.api.v1.endpoints.login import login_access_token
# from tanzanite.core.security import get_auth_headers
from tanzanite.webapps import response_page
from tanzanite.webapps.auth.forms import LoginForm


router = APIRouter()
logger = logging.getLogger(__name__)


# router.get(
#     "/",
#     response_class=responses.HTMLResponse,
# )
# async def home(
#     request: Request,
#     msg: str = None,
#     user: models.User = Depends(deps.get_current_user),
# ):
#     logger.debug('[+] GET routed to home()')
#     if user is None:
#         return response_page(
#             "auth/login.html",
#             request=request,
#             errors=['Login expired'],
#         )
#     return response_page(
#         "general_pages/homepage.html",
#         request=request,
#         user=user,
#         msg=msg,
#     )


@router.get("/login/", response_class=responses.HTMLResponse)
def login_form(request: Request):
    """
    Create login form for the webapp.
    """
    return response_page(
        "auth/login.html",
        request=request,
        user=None,
    )


@router.post("/login/")
async def login_post(
    request: Request,
    db: Session = Depends(deps.get_db)
):
    """
    Process login result form.
    """
    form = LoginForm(request)
    await form.load_data()
    if await form.is_valid():
        form.__dict__.update(msg="Login successful")
        user = crud.user.get_by_email(db, email=form.email)
        try:
            response = response_page(
                # "auth/login.html",
                "general_pages/homepage.html",
                # form already contains 'request',
                **form.__dict__,
                user=user,
            )
        except jinja2.exceptions.UndefinedError:
            return PlainTextResponse(
                f'Error while rendering template\n{traceback.format_exc()}'  # noqa
            )
        except HTTPException:
            form.__dict__.update(msg="")
            form.__dict__.get("errors").append("Authentication failed")
            return response_page(
                "auth/login.html",
                # form already contains 'request'
                **form.__dict__
            )
        _ = login_access_token(
            response=response,
            form_data=form,
            db=db
        )
        return response
    return response_page(
        "auth/login.html",
        # form already contains 'request'
        **form.__dict__
    )


@router.get("/logout/")
async def logout(
    request: Request,
):
    """
    Log out.
    """
    request.cookies.clear()
    response = responses.RedirectResponse("/login")
    response.set_cookie(
        key="access_token",
        value="TheseAreNotTheDroidsYouAreLookingFor"
    )
    return response


# vim: set ts=4 sw=4 tw=0 et :
