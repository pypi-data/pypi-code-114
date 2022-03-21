# -*- coding: utf-8 -*-

"""
Create user accounts.
"""

# Standard imports
import logging
import secrets
import sys

# External imports
import argparse
import json
import requests

from cliff.lister import Lister
from fastapi import status
from psec.utils import natural_number
from pydantic import (  # pylint: disable=no-name-in-module
    EmailStr,
    ValidationError,
)

# Local imports
from tanzanite.backend.app.app.schemas.user import UserCreate
from tanzanite.core.security import get_auth_headers
from tanzanite.cli.user import get_users_via_api
from tanzanite.utils import (
    USERNAME_PROMPT,
    get_api_base_url,
    prompt_for_input,
    prompt_for_password,
)


# pylint: disable=missing-function-docstring
class TestNames():
    """
    Class providing an iterator for test account names.

    Produces a list of N unique user names based on adding a random
    string to the user portion of an email address using the '+'
    mechanism supported by many email services.  For example,
    a variation of "testuser@example.com" would be something like
    "testuser+s8@example.com"
    """

    def __init__(
        self,
        count: int = 5,
        existing: list = None,
        max_randomizer_length: int = 6,
        email: EmailStr = "",
    ):
        self.count = count
        self.max_randomizer_length = max_randomizer_length
        self.existing = [] if existing is None else existing
        self.names = []
        self.email_name, self.email_domain = email.split('@')

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        while len(self.names) < self.count:
            word = secrets.token_hex()[:self.max_randomizer_length]
            name = (
                word
                if self.email_name == ''
                else '+'.join([self.email_name, word])
            )
            email_name = "@".join([name, self.email_domain])
            if (
                email_name not in self.names
                and email_name not in self.existing
            ):
                self.names.append(email_name)
                return email_name
        raise StopIteration()
# pylint: enable=missing-function-docstring


def test_user_full_name(
    username: str,
    full_name: str,
) -> str:
    """
    Form a full_name for a test user.
    """
    suffix = username.split('@')[0].split('+')[1]
    return (
        f'{full_name} {suffix}'
        if full_name is not None
        else f"Test User {suffix}"
    )


class CmdUserCreate(Lister):
    """
    Create users in the database.

    You can create user entries in the Tanzanite database from the command line
    in one of two ways: individually using option flags and arguments, or in bulk
    from a file in CSV or JSON format.

    To bootstrap a system, there needs to be an initial privileged account. This
    account is created in the database automatically on first initialization of
    the database. You can then immediately log in via the CLI or web app
    and start managing the system.

    When no ``username`` or ``password`` are specified on the command line,
    the values for the ``psec`` secrets ``tanzanite_admin_user_email`` and
    ``tanzanite_admin_password`` will be used.

    The ``--from-file`` option is used for mass-creation of users in the
    database. For security reasons, it can only be used by someone who has
    the ``is_supervisor`` property set.

    Users created with this command are automatically verified unless the
    ``--no-verified`` flag is present.  This helps in pre-populating the system
    with a large number of users who are already known by the system operator
    to have accurate email addresses (e.g., for large purpleteaming exercises,
    closed capture the flag contests, or training events). If open registration
    is enabled, users can create accounts for themselves but must verify their
    email address before they can log in to the platform.
    """  # noqa

    logger = logging.getLogger(__name__)
    requires_login = True

    def __init__(self, args, app_args, cmd_name=None):
        super().__init__(args, app_args, cmd_name=cmd_name)
        self.data = []

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument(
            'username',
            nargs='?',
            type=EmailStr,
            default=None,
            help='Email address for login username'
        )
        parser.add_argument(
            'password',
            nargs='?',
            default=None,
            help='Password of 8 or more characters in length'
        )
        parser.add_argument(
            '--full-name',
            type=str,
            default=None,
            help="Person's full name"
        )
        parser.add_argument(
            '--superuser',
            action='store_true',
            dest='is_superuser',
            default=False,
            help='Enable `is_superuser` flag on this account'
        )
        parser.add_argument(
            '--proctor',
            action='store_true',
            dest='is_proctor',
            default=False,
            help='Enable `is_proctor` flag on this account'
        )
        parser.add_argument(
            '--verified',
            action=argparse.BooleanOptionalAction,
            dest='is_verified',
            default=True,
            help='Mark the user as verified or not'
        )
        parser.add_argument(
            '--test-users',
            action='store',
            dest='test_users',
            type=natural_number,
            default=0,
            help=argparse.SUPPRESS
        )
        return parser

    def take_action(self, parsed_args):
        base_url = get_api_base_url()
        db_users = get_users_via_api(auth_token=self.app.auth_token)
        db_users_names = [user.get('email') for user in db_users]
        username = (
            prompt_for_input(USERNAME_PROMPT)
            if parsed_args.username is None
            else parsed_args.username
        )
        password = (
            prompt_for_password()
            if parsed_args.password is None
            else parsed_args.password
        )
        if parsed_args.test_users == 0:
            usernames = [username]
        else:
            usernames = [
                name for name in
                TestNames(
                    count=parsed_args.test_users,
                    existing=db_users_names,
                    email=username
                )
            ]
        for name in usernames:
            if name in db_users_names:
                sys.exit(
                    f"[-] a user '{name}' already exists"
                )
            if parsed_args.test_users > 0:
                full_name = test_user_full_name(
                    name,
                    parsed_args.full_name,
                )
            else:
                full_name = parsed_args.full_name
            try:
                user_create = UserCreate(
                    email=name,
                    password=password,
                    full_name=full_name,
                    is_active=parsed_args.is_verified,
                    is_proctor=parsed_args.is_proctor,
                    is_superuser=parsed_args.is_superuser,
                )
            except ValidationError:
                self.app.stderr.write(f"[-] username: '{name}'\n")
                raise
            response = requests.post(
                f"{base_url}/users/",
                headers=get_auth_headers(token=self.app.auth_token),
                data=user_create.json(),
            )
            if response.status_code != status.HTTP_200_OK:
                sys.exit(
                    "[-] failed to create user: "
                    f'{response.status_code} {response.reason}'
                )
            new_user = json.loads(response.text)
            # This method is injected in tanzanite/cli/user/__init__.py
            self.record_user(new_user)  # pylint: disable=not-callable
        if self.app_args.verbose_level > 0:
            self.log_success(username, usernames, parsed_args)
        if self.app_args.verbose_level < 1:
            sys.exit(0)
        return self.columns, self.data

    def log_success(self, username, usernames, parsed_args):
        """
        Produce success log message including details of user properties.
        """
        count = len(usernames)
        user_type = "privileged" if parsed_args.is_superuser else "standard"
        if parsed_args.test_users:
            user_type += " test"
        user_type += " users" if count > 1 else " user"
        if parsed_args.test_users:
            user_type += " based on"
        self.logger.info(
            "[+] created %d %s '%s'", count, user_type, username
        )


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
