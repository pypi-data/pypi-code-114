# -*- coding: utf-8 -*-

"""
Tanzanite webapp challenge routes.
"""

# Standard imports
import logging

# External imports
from typing import Optional

from fastapi import (
    APIRouter,
    Depends,
    Request,
    responses,
    status,
)
from sqlalchemy.orm import Session

# Local imports
from tanzanite.backend.app.app import (
    crud,
    models,
    schemas,
)
from tanzanite.backend.app.app.api import deps
# FIXME: create these functions and use in API?
# from tanzanite.backend.app.app.db.repository.challenges import (
#     create_new_challenge,
#     list_challenges,
#     retreive_challenge,
#     search_challenge,
# )
from tanzanite.webapps import response_page
from tanzanite.webapps.challenges.forms import ChallengeCreateForm


router = APIRouter()
logger = logging.getLogger(__name__)


# pylint: disable=unused-argument
# Dependencies are used for authentication, etc. in params.


@router.get(
    "/",
    response_class=responses.HTMLResponse,
)
async def home(
    request: Request,
    msg: str = None,
    user: models.User = Depends(deps.get_current_user),
):
    logger.debug('[+] GET routed to home()')
    # if user is None:
    #     return response_page(
    #         "auth/login.html",
    #         request=request,
    #         errors=['Login expired'],
    #     )
    return response_page(
        "general_pages/homepage.html",
        request=request,
        user=user,
        msg=msg,
    )


@router.get(
    "/list",
    response_class=responses.HTMLResponse,
)
async def challenges_list(
    request: Request,
    skip: int = 0,
    limit: int = 0,
    db: Session = Depends(deps.get_db),
    user: models.User = Depends(deps.get_current_active_user),
    msg: str = None
):
    logger.debug('[+] GET routed to challenges_list()')
    challenges = crud.challenge.get_multi(db, skip=skip, limit=limit)
    return response_page(
        "general_pages/homepage.html",
        request=request,
        user=user,
        challenges=challenges,
        msg=msg,
    )


@router.get(
    "/details/{cid}",
    response_class=responses.HTMLResponse,
)
async def challenge_detail(
    cid: int,
    request: Request,
    user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db)
):
    logger.debug('[+] GET routed to challenge_detail()')
    challenge = crud.challenge.get(id_=cid, db=db)
    return response_page(
        "challenges/detail.html",
        request=request,
        user=user,
        challenge=challenge
    )


@router.get(
    "/post-a-challenge/",
    response_class=responses.HTMLResponse,
)
async def create_challenge_form(
    request: Request,
    user: models.User = Depends(deps.get_current_active_user),
):
    logger.debug('[+] GET routed to create_challenge()')
    return response_page(
        "challenges/create_challenge.html",
        request,
        user=user,
    )


@router.post(
    "/post-a-challenge/",
    response_class=responses.HTMLResponse,
)
async def create_challenge(  # noqa
    request: Request,
    user: models.User = Depends(deps.get_current_active_superuser),
    db: Session = Depends(deps.get_db)
):
    logger.debug('[+] POST routed to create_challenge()')
    challenges = crud.challenge.get_multi(db=db, skip=0, limit=0)
    form = ChallengeCreateForm(request, challenges=challenges)
    await form.load_data()
    if form.is_valid():
        challenge_in = schemas.ChallengeCreate(**form.__dict__)
        challenge = crud.challenge.create_with_owner(
            db=db,
            obj_in=challenge_in,
            owner_id=user.id
        )
        return responses.RedirectResponse(
            f"/details/{challenge.id}",
            status_code=status.HTTP_303_SEE_OTHER
        )
    return response_page(
        "challenges/create_challenge.html",
        user=user,
        **form.__dict__
    )


@router.get(
    "/delete-challenge/",
    dependencies=[Depends(deps.get_current_active_superuser)],
    response_class=responses.HTMLResponse,
)
async def show_challenges_to_delete(
    request: Request,
    user: models.User = Depends(deps.get_current_active_superuser),
    db: Session = Depends(deps.get_db)
):
    logger.debug('[+] GET routed to show_challenges_to_delete()')
    challenges = crud.challenge.get_multi(db=db, skip=0, limit=0)
    return response_page(
        "challenges/show_challenges_to_delete.html",
        request,
        user=user,
        challenges=challenges,
    )


@router.get(
    "/search/",
    response_class=responses.HTMLResponse,
)
async def search(
    request: Request,
    user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
    query: Optional[str] = None
):
    logger.debug('[+] GET routed to search()')
    challenges = crud.challenge.get_multi_by_content(
        db=db,
        query=query,
    )
    query_string = query.strip()
    msg = (
        f'Challenges related to "{query_string}"'
        if query_string not in ['', None]
        else None
    )
    return response_page(
        "general_pages/homepage.html",
        request,
        user=user,
        challenges=challenges,
        msg=msg,
    )

# vim: set ts=4 sw=4 tw=0 et :
