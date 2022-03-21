# -*- coding: utf-8 -*-

# Standard imports
from typing import (
    List,
    Union,
)

# External imports
from fastapi import (
    Request,
)
from fastapi.encoders import jsonable_encoder


# Local imports
from tanzanite import TEMPLATES
from tanzanite.backend.app.app import (
    # crud,
    models,
    schemas,
)


def response_page(
    page: str,
    request: Request,
    *,
    user: Union[models.User, None] = None,
    challenges: List[Union[models.Challenge, None]] = None,
    users: List[Union[models.User, None]] = None,
    errors: List[Union[str, None]] = None,
    **kwargs,
):
    """
    Produce a top-level response page from a template, providing all
    necessary data for subordinate templated pages from which the
    top-level pages extend.  This is necessary because shared templates
    like 'navbar.html' rely on variables that aren't obviously used
    due to the nested inclusions.
    """
    data = (
        schemas.User(**jsonable_encoder(user)).dict()
        if user is not None
        else {}
    )
    data['request'] = request
    # Hack to deal with the "username" vs. "email" issue.
    email = data.get('email')
    if email is not None:
        data['username'] = email
    if challenges is not None:
        data['challenges'] = challenges
    if users is not None:
        data['users'] = users
    if errors is not None:
        data['errors'] = errors
    # Fallback to add any remaining dictionary items.
    data.update(kwargs)
    return TEMPLATES.TemplateResponse(page, data)


# vim: set ts=4 sw=4 tw=0 et :
