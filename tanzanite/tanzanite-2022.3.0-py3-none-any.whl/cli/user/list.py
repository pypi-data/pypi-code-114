# -*- coding: utf-8 -*-

"""
List users in the database.
"""

# Standard imports
import logging
import sys

# External imports
from cliff.lister import Lister
from psec.utils import natural_number

# Local imports
from tanzanite.cli.user import (
    get_users_via_api,
    DEFAULT_SKIP,
    DEFAULT_LIMIT,
)


class CmdUserList(Lister):
    """
    List user(s) in the database.

    Lists one or more user entries in the Tanzanite database.
    """
    logger = logging.getLogger(__name__)
    requires_login = True

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument(
            'arg',
            nargs='?',
            default=None
        )
        parser.add_argument(
            '-C', '--current',
            action='store_true',
            default=False,
            help='List current user, active or not'
        )
        parser.add_argument(
            '--skip',
            action='store',
            type=natural_number,
            default=DEFAULT_SKIP,
            help='Users to skip'
        )
        parser.add_argument(
            '--limit',
            action='store',
            type=natural_number,
            default=DEFAULT_LIMIT,
            help='Limit number of users'
        )
        return parser

    def take_action(self, parsed_args):
        if parsed_args.current and (parsed_args.skip or parsed_args.limit):
            sys.exit('[-] cannot use `--current` with `--skip` or `--limit`')
        users = get_users_via_api(
            current=parsed_args.current,
            skip=parsed_args.skip,
            limit=parsed_args.limit,
            auth_token=self.app.auth_token,
        )
        if len(users) < 1:
            sys.exit(1)
        columns = (
            [
                key for key in users[0].keys()
                if key != 'hashed_password'
            ]
        )
        data = [
            [row.get(column) for column in columns]
            for row in users
        ]
        return columns, data


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
