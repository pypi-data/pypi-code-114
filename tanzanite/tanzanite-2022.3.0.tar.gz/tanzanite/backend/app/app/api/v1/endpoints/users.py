# -*- coding: utf-8 -*-

# pylint: disable=missing-module-docstring

# Standard imports
from typing import (
    Any,
    Dict,
    List,
    Union,
)

# External imports
from fastapi import (
    APIRouter,
    Body,
    Depends,
    HTTPException,
    status,
)
from fastapi.encoders import jsonable_encoder
from pydantic import EmailStr  # pylint: disable=no-name-in-module
from sqlalchemy.orm import Session

# Local imports
from tanzanite.backend.app.app import (
    crud,
    models,
    schemas,
)
from tanzanite.backend.app.app.api import deps
from tanzanite.core.config import settings
from tanzanite.backend.app.app.utils import send_new_account_email


router = APIRouter()


# pylint: disable=unused-argument


@router.get("/", response_model=List[schemas.User])
def read_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 0,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve users.

    Only proctors and superuser can get all users.
    """
    if not (
        current_user
        and (
            crud.user.is_superuser(current_user)
            or crud.user.is_proctor(current_user)
        )
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient permission",
        )
    db_users = crud.user.get_multi(db, skip=skip, limit=limit)
    return db_users


@router.post(
    "/",
    dependencies=[Depends(deps.get_current_active_superuser)],
    response_model=schemas.User,
)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
) -> Any:
    """
    Create new user.
    """
    db_user = crud.user.get_by_email(db, email=user_in.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user with this username already exists in the system.",
        )
    created_user = crud.user.create(db, obj_in=user_in)
    if settings.EMAILS_ENABLED and created_user.email:
        send_new_account_email(
            email_to=created_user.email,
            username=created_user.email,
            # password=created_user.password
        )
    return created_user


@router.put("/me", response_model=schemas.User)
def update_user_me(
    *,
    db: Session = Depends(deps.get_db),
    password: str = Body(None),
    full_name: str = Body(None),
    email: EmailStr = Body(None),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update own user.

    Fields that can be updated are:
      `full_name`
      `password`
      `email`
    """
    current_user_data = jsonable_encoder(current_user)
    user_in = schemas.UserUpdate(**current_user_data)
    if password is not None:
        user_in.password = password
    if full_name is not None:
        user_in.full_name = full_name
    if email is not None:
        user_in.email = email
    updated_user = crud.user.update(db, db_obj=current_user, obj_in=user_in)
    return updated_user


@router.get("/me", response_model=schemas.User)
def read_user_me(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get current user.
    """
    db_user = crud.user.get_by_email(db, email=current_user.email)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The user with this uid does not exist in the system",
        )
    return schemas.User(**db_user.__dict__)


@router.post("/open", response_model=schemas.User)
def create_user_open(
    *,
    db: Session = Depends(deps.get_db),
    password: str = Body(...),
    email: EmailStr = Body(...),
    full_name: str = Body(None),
) -> Any:
    """
    Create new user without the need to be logged in.

    Properties that must be included are:
        `email`
        `password`
        `full_name`
    """
    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Open user registration is forbidden on this server",
        )
    db_user = crud.user.get_by_email(db, email=email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user with this username already exists in the system",
        )
    user_in = schemas.UserCreate(
        password=password,
        email=email,
        full_name=full_name
    )
    created_user = crud.user.create(db, obj_in=user_in)
    return created_user


# Avoiding shadowing of `id` builtin while also not exposing `id_` to the API.
@router.get("/{uid}", response_model=schemas.User)
def read_user_by_id(
    uid: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.

    Must be a superuser or the current user getting their own data.
    """
    db_user = crud.user.get(db, id_=uid)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The user with this uid does not exist in the system",
        )
    if not (
        crud.user.is_superuser(current_user)
        or db_user == current_user
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient permission",
        )
    return db_user


# Avoiding shadowing of `id` builtin while also not exposing `id_` to the API.
@router.put("/{uid}", response_model=schemas.User)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    uid: int,
    user_in: Union[schemas.UserUpdate, Dict[str, Any]],
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a user entry.

    Must be a superuser to update entries. You cannot remove superuser
    privilege if the user is the only superuser on the system.
    """
    db_user = crud.user.get(db, id_=uid)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No user with this username exists in the system",
        )
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient permission",
        )
    if (
        db_user.is_superuser is True
        and user_in.is_superuser is False
    ):
        superusers = [
            item.email for item in crud.user.get_multi(db, limit=0)
            if item.is_superuser is True
        ]
        if db_user.email in superusers and len(superusers) < 2:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=(
                    "Would leave no superusers in the database"
                ),
            )
    updated_user = crud.user.update(db, db_obj=db_user, obj_in=user_in)
    return updated_user


# Avoiding shadowing of `id` builtin while also not exposing `id_` to the API.
@router.delete("/{uid}", response_model=schemas.User)
def delete_user(
    *,
    db: Session = Depends(deps.get_db),
    uid: int,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Delete a user.
    """
    if uid == 1:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot delete initial user",
        )
    db_user = crud.user.get(db, id_=uid)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The user with this username does not exist in the system",
        )
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient permission",
        )
    deleted_user = crud.user.delete(db, db_obj=db_user)
    return deleted_user


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
