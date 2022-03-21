# -*- coding: utf-8 -*-

"""
Update a user entry in the database.
"""

# Standard imports
import argparse
import logging
import sys


# External imports
import json
import requests

from cliff.lister import Lister
from fastapi import status
from fastapi.encoders import jsonable_encoder
from pydantic import (  # pylint: disable=no-name-in-module
    EmailStr,
    ValidationError,
)

# Local imports
from tanzanite.backend.app.app.schemas import (
    # UserDB,
    UserUpdate,
)
from tanzanite.cli.user import (
    get_users_via_api,
    UserBag,
)
from tanzanite.core.security import get_auth_headers
from tanzanite.utils import (
    check_update,
    get_api_base_url,
)


class CmdUserUpdate(Lister):
    """
    Update user entries in the database.

    This command allows you to update one or more properties at a time for
    one or more users in the Tanzanite database. Properties are selected by
    command line options and users are specified by either their email address
    or their internal id value.

    Setting properties for more than one user at a time does not make sense
    for all properties that are typically unique to each user, such as the
    user's full name or their email address. Other properties, like active
    status or superuser status, can be changed in bulk.  The flag ``--all``
    allows you to apply the change to all accounts in the database.
    """  # noqa

    logger = logging.getLogger(__name__)
    requires_login = True

    def __init__(self, args, app_args, cmd_name=None):
        super().__init__(args, app_args, cmd_name=cmd_name)
        self.data = []

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument(
            'arg',
            nargs='*',
            default=None,
            help='User id or email'
        )
        parser.add_argument(
            '--all',
            action='store_true',
            default=False,
            help='Apply changes to all users'
        )
        parser.add_argument(
            '--email',
            type=EmailStr,
            default=None,
            help='New email address'
        )
        # parser.add_argument(
        #     '--shell-login',
        #     type=get_shell_login,
        #     default=None,
        #     help='New `shell_login` for the user'
        # )
        parser.add_argument(
            '--full-name',
            type=str,
            default=None,
            help='New `full_name` for the user'
        )
        parser.add_argument(
            '--active',
            action=argparse.BooleanOptionalAction,
            default=None,
            help='Mark as active'
        )
        parser.add_argument(
            '--proctor',
            action=argparse.BooleanOptionalAction,
            default=None,
            help='Mark the user as a proctor'
        )
        parser.add_argument(
            '--superuser',
            action=argparse.BooleanOptionalAction,
            default=None,
            help='Mark the user as superuser'
        )
        parser.add_argument(
            '--verified',
            action=argparse.BooleanOptionalAction,
            default=None,
            help='Mark the user as verified'
        )
        return parser

    def take_action(self, parsed_args):  # noqa: C901
        if parsed_args.all is None and parsed_args.arg is None:
            # TODO(dittrich): Add menu selection feature ala psec
            sys.exit('[-] no user id or email specified')
        base_url = get_api_base_url()
        users = get_users_via_api(auth_token=self.app.auth_token)
        user_bag = UserBag(users)
        if (
            (parsed_args.all or len(parsed_args.arg) > 1)
            and (
                parsed_args.full_name is not None
                or parsed_args.email is not None
            )
        ):
            sys.exit("[-] can't set `full_name` or `email` for multiple users")
        arg_users = (
            [user.get('email') for user in users]
            if parsed_args.all
            else parsed_args.arg
        )
        for arg in arg_users:
            username, id_ = user_bag.get_id(arg)
            if id_ is None:
                sys.exit(f"[-] email or id '{arg}' not found")
            user = user_bag.get_user(id_)
            # FIXME: use schema instead of `exclude`?
            updates = jsonable_encoder(
                UserUpdate(**user), exclude={'password'}
            )
            arg_to_attribute = {
                'email': 'email',
                'full_name': 'full_name',
                'active': 'is_active',
                'superuser': 'is_superuser',
                'proctor': 'is_proctor',
                'verified': 'is_verified',
            }
            if not check_update(parsed_args, updates, arg_to_attribute):
                self.logger.info(
                    "[-] no changes to user id %s ('%s')", id_, username
                )
                continue
            try:
                user_update = UserUpdate(**updates)
            except ValidationError:
                self.app.stderr.write(f"[-] username: '{username}'\n")
                raise
            response = requests.put(
                f"{base_url}/users/{id_}",
                headers=get_auth_headers(token=self.app.auth_token),
                data=user_update.json(),
            )
            if response.status_code in [
                status.HTTP_400_BAD_REQUEST,
                status.HTTP_403_FORBIDDEN,
                status.HTTP_404_NOT_FOUND,
            ]:
                detail = json.loads(response.text).get("detail")
                sys.exit(
                    f"[-] failed to update user '{id_}': {detail}"
                )
            if response.status_code != status.HTTP_200_OK:
                sys.exit(
                    f"[-] failed to update user '{id_}': "
                    f'{response.status_code} {response.reason}'
                )
            updated_user = json.loads(response.text)
            # This method is injected in tanzanite/cli/user/__init__.py
            self.record_user(updated_user)  # pylint: disable=not-callable
            self.logger.info(
                "[+] updated user id=%s (%s)",
                id_,
                updated_user.get('email')
            )
        if self.app_args.verbose_level < 1 or len(self.data) == 0:
            sys.exit(0)
        return self.columns, self.data


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
