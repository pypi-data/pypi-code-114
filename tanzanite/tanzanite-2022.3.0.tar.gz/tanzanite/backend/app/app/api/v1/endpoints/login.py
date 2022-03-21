# -*- coding: utf-8 -*-

# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

# Standard imports
from datetime import timedelta
from typing import Any

# External imports
from fastapi import status
from fastapi import (
    APIRouter,
    Body,
    Depends,
    HTTPException,
)
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette.responses import Response

# Local imports
from tanzanite.backend.app.app import (
    crud,
    models,
    schemas,
)
from tanzanite.backend.app.app.api import deps
from tanzanite.backend.app.app.utils import (
    generate_password_reset_token,
    send_reset_password_email,
    verify_password_reset_token,
)
from tanzanite.core import security
from tanzanite.core.config import settings
from tanzanite.core.security import get_password_hash

router = APIRouter()


@router.post("/login/access-token", response_model=schemas.Token)
def login_access_token(
    response: Response,
    db: Session = Depends(deps.get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = crud.user.authenticate(
        db,
        email=form_data.username,
        password=form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    if not crud.user.is_active(user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    access_token_expires = timedelta(
        minutes=int(settings.tanzanite_jws_token_expire_minutes)
    )
    access_token = security.create_access_token(
        user.id, expires_delta=access_token_expires
    )
    response.set_cookie(
        key="access_token", value=f"Bearer {access_token}", httponly=True
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


@router.post("/login/test-token", response_model=schemas.User)
def test_token(
    current_user: models.User = Depends(deps.get_current_user)
) -> Any:
    """
    Test access token
    """
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
    return current_user


@router.post("/password-recovery/{email}", response_model=schemas.Msg)
def recover_password(
    email: str,
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Password Recovery
    """
    user = crud.user.get_by_email(db, email=email)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The user with this username does not exist in the system.",
        )
    password_reset_token = generate_password_reset_token(email=email)
    send_reset_password_email(
        email_to=user.email,
        email=email,
        token=password_reset_token,
    )
    return {"msg": "Password recovery email sent"}


@router.post("/reset-password/", response_model=schemas.Msg)
def reset_password(
    token: str = Body(...),
    new_password: str = Body(...),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Reset password
    """
    email = verify_password_reset_token(token)
    if not email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid token",
        )
    user = crud.user.get_by_email(db, email=email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No user with this username exists in the system.",
        )
    if not crud.user.is_active(user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user",
        )
    hashed_password = get_password_hash(new_password)
    user.hashed_password = hashed_password
    db.add(user)
    db.commit()
    return {"msg": "Password updated successfully"}


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
