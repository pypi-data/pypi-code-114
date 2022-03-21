# -*- coding: utf-8 -*-

"""
`user` subcommands module initialization.
"""

# Standard imports
import json
import types

from typing import (
    List,
    Tuple,
    Union,
)

# External imports
import requests

from fastapi import status

# Local imports
from tanzanite.core.security import get_auth_headers
from tanzanite.backend.app.app.models.user import User
from tanzanite.utils import get_api_base_url


DEFAULT_SKIP = 0
DEFAULT_LIMIT = 0


def get_users_via_api(
    current=None,
    skip=DEFAULT_SKIP,
    limit=DEFAULT_LIMIT,
    auth_token=None,
) -> List:
    """
    Get users via API call.
    """
    base_url = get_api_base_url()
    params = {}
    if current:
        url_path = 'me'
    else:
        url_path = ''
        if skip is not None:
            params['skip'] = skip
        if limit is not None:
            params['limit'] = limit
    response = requests.get(
        f"{base_url}/users/{url_path}",
        params=params,
        headers=get_auth_headers(token=auth_token),
    )
    if response.status_code != status.HTTP_200_OK:
        raise RuntimeError(
            "[-] failed to get users: "
            f'{response.status_code} {response.reason}'
        )
    users = json.loads(response.text)
    return [users] if current else users


class UserBag():
    """
    Class to index users for identification by email or id.
    """
    def __init__(self, users: List = None) -> None:
        """Initializer."""
        self.email_to_id = {}
        self.id_to_email = {}
        self.users = {}
        if users is not None:
            self.add_users(users=users)

    def add_user(self, user: User) -> None:
        """
        Add a single user to saved state.
        """
        self.email_to_id[user.get('email')] = str(user.get('id'))
        self.id_to_email[str(user.get('id'))] = user.get('email')
        self.users[str(user.get('id'))] = user

    def add_users(self, users: List[User]) -> None:
        """
        Add a list of users to saved state.
        """
        for user in users:
            self.add_user(user)

    def get_user(self, id_: str) -> Union[User, None]:
        """
        Return the user record associated with a given id.
        """
        return self.users.get(id_)

    def get_id(self, item: str) -> Union[Tuple, None]:
        """
        Return a tuple with the email and id for a user,
        or None.
        """
        email, id_ = None, None
        if item in self.email_to_id:
            id_ = self.email_to_id.get(item)
            email = item
        elif item in self.id_to_email:
            id_ = item
            email = self.id_to_email.get(item)
        return (email, id_)


def get_email_and_id(
    item: str,
    users: List[User]
) -> Tuple[Union[str, None], Union[str, None]]:
    """
    Get both email address and id value from `item` (which could
    be either one).
    """
    email, id_ = None, None
    for user in users:
        if user.get('email') == item or user.get('id') == item:
            email = user.get('email')
            id_ = user.get('id')
    return (email, id_)

    # email_to_id = {user.get('email'): str(user.get('id')) for user in users}
    # id_to_email = {str(user.get('id')): user.get('email') for user in users}
    # user_mapping = {user.get('email'): i for i, user in enumerate(users)}
    # id_mapping = {str(user.get('id')): i for i, user in enumerate(users)}


# Patch in a new method to classes inheriting from cliff's abstract classes.

def record_user(self, user):
    """Accumulate data for bulk reporting."""
    # Ensure required object variables initialized.
    self.columns = getattr(self, 'columns', [])
    self.data = getattr(self, 'data', [])
    keys, values = [], []
    for (key, value) in user.items():
        keys.append(key)
        values.append(value)
    if len(self.columns) == 0:
        self.columns.extend(keys)
    self.data.extend([values])


from tanzanite.cli.user.create import CmdUserCreate
from tanzanite.cli.user.update import CmdUserUpdate


CmdUserUpdate.record_user = types.MethodType(record_user, CmdUserUpdate)
CmdUserCreate.record_user = types.MethodType(record_user, CmdUserCreate)

# vim: set ts=4 sw=4 tw=0 et :
