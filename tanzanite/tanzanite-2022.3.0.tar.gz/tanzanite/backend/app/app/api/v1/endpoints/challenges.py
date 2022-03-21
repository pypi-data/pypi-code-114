# -*- coding: utf-8 -*-

# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

# Standard imports
from typing import Any, List

# External imports
from fastapi import status
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from sqlalchemy.orm import Session

# Local imports
from tanzanite.backend.app.app import (
    crud,
    models,
    schemas,
)
from tanzanite.backend.app.app.api import deps

router = APIRouter()


@router.get(
    "/",
    dependencies=[Depends(deps.get_current_active_user)],
    response_model=List[schemas.Challenge])
def read_challenges(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 0,
) -> Any:
    """
    Retrieve challenges.

    Must be an active user to read challenges.
    """
    challenges = crud.challenge.get_multi(db, skip=skip, limit=limit)
    if not challenges:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No challenges found",
        )
    return challenges


@router.post("/", response_model=schemas.Challenge)
def create_challenge(
    *,
    db: Session = Depends(deps.get_db),
    challenge_in: schemas.ChallengeCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create a new challenge.

    Must be a superuser to create challenges.
    """
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient permission"
        )
    challenge = crud.challenge.create_with_owner(
        db=db,
        obj_in=challenge_in,
        owner_id=current_user.id
    )
    return challenge


# Avoiding shadowing of `id` builtin while also not exposing `id_` to the API.
@router.get("/{cid}", response_model=schemas.Challenge)
def read_challenge(
    *,
    db: Session = Depends(deps.get_db),
    cid: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get a challenge by ID.

    Must be an active user.
    """
    challenge = crud.challenge.get(db=db, id_=cid)
    if not challenge:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Challenge not found",
        )
    if not crud.user.is_active(current_user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient permission"
        )
    return challenge


# Avoiding shadowing of `id` builtin while also not exposing `id_` to the API.
@router.put("/{cid}", response_model=schemas.Challenge)
def update_challenge(
    *,
    db: Session = Depends(deps.get_db),
    cid: int,
    challenge_in: schemas.ChallengeUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a challenge entry.

    Must be a superuser or owner of the challenge to update.
    """
    challenge = crud.challenge.get(db=db, id_=cid)
    if not challenge:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Challenge with this id not found",
        )
    if not (
        crud.user.is_superuser(current_user)
        or challenge.owner_id == current_user.id
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient permission",
        )
    challenge = crud.challenge.update(
        db,
        db_obj=challenge,
        obj_in=challenge_in
    )
    return challenge


# Avoiding shadowing of `id` builtin while also not exposing `id_` to the API.
@router.delete(
    "/{cid}",
    dependencies=[Depends(deps.get_current_active_user)],
    response_model=schemas.Challenge
)
def delete_challenge(
    *,
    db: Session = Depends(deps.get_db),
    cid: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete a challenge.

    Must be a superuser or owner of the challenge to delete it.
    """
    challenge = crud.challenge.get(db=db, id_=cid)
    if not challenge:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Challenge not found",
        )
    if not (
        crud.user.is_superuser(current_user)
        or challenge.owner_id == current_user.id
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient permission",
        )
    challenge = crud.challenge.remove(db=db, id_=cid)
    return challenge


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
