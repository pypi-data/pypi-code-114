# -*- coding: utf-8 -*-

"""
API dependencies.
"""

# pylint: disable=missing-function-docstring

# Standard imports
from typing import Generator


# External imports
from fastapi import (
    Depends,
    HTTPException,
    Request,
    status,
)
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.utils import get_authorization_scheme_param
from jose import jwt
from jwt import ExpiredSignatureError
from pydantic import ValidationError
from sqlalchemy.orm import Session

# Local imports
from tanzanite.backend.app.app import (
    crud,
    models,
    schemas,
)
from tanzanite.core.config import settings
from tanzanite.backend.app.app.db.session import SessionLocal


reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl="/login/access-token",
    auto_error=False
)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(
    request: Request = None,
    token: str = Depends(reusable_oauth2),
    *,
    db: Session = Depends(get_db)
) -> models.User:
    """
    Get the current user from a JWT consisting of a token or
    a Request cookie.

    Browser sessions should have a 'browser_only' cookie containing
    the access token, while CLI sessions typically use tokens in
    HTTP headers. Tests with fake web clients may end up with both.
    """
    if request is not None:
        authorization = (
            request.headers.get('authorization')
            or request.cookies.get('access_token')
        )
        if authorization is not None:
            _, param = get_authorization_scheme_param(
                authorization
            )
            token = param
    if token is None:
        # raise HTTPException(
        #     status_code=status.HTTP_401_UNAUTHORIZED,
        #     detail="Missing authorization credentials",
        # )
        return None
    try:
        payload = jwt.decode(
            token,
            settings.tanzanite_secret_key,
            algorithms=[settings.tanzanite_jws_algorithm]
        )
        token_data = schemas.TokenPayload(**payload)
    # except ExpiredSignatureError:
        # raise HTTPException(
        #     status_code=status.HTTP_403_FORBIDDEN,
        #     detail="Credentials expired",
        # ) from None
        # return None
    # except (jwt.JWTError, ValidationError) as err:
        # raise HTTPException(
        #     status_code=status.HTTP_401_UNAUTHORIZED,
        #     detail="Could not validate credentials",
        # ) from None
        # return None
    except (
        ExpiredSignatureError,
        jwt.JWTError,
        ValidationError,
    ) as err:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        ) from err
    user = crud.user.get(db, id_=token_data.sub)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        ) from None
        # return None
    return user


def get_current_active_user(
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    if (
        current_user is not None
        and not crud.user.is_active(current_user)
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    return current_user


def get_current_active_superuser(
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user doesn't have enough privileges"
        )
    return current_user


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
