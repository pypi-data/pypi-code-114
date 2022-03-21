# -*- coding: utf-8 -*-

"""
Delete user(s) from the database.
"""

# Standard imports
import logging
import sys

# External imports
import requests

from cliff.command import Command
from fastapi import status
from tanzanite.cli.user import get_users_via_api

# Local imports
from tanzanite.core.security import get_auth_headers
from tanzanite.utils import (
    USERNAME_PROMPT,
    prompt_for_input,
    get_api_base_url,
)


class CmdUserDelete(Command):
    """
    Delete user(s) from the database.

    Deletes one or more user entries from the Tanzanite database.

    If you do not provide a username, you will be prompted for one.
    """
    logger = logging.getLogger(__name__)
    requires_login = True

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument(
            'username',
            nargs='*',
            default=None,
            help='Users to delete'
        )
        return parser

    def take_action(self, parsed_args):
        base_url = get_api_base_url()
        users = get_users_via_api(auth_token=self.app.auth_token)
        email_to_id = {
            user.get('email'): str(user.get('id'))
            for user in users
        }
        id_to_email = {
            str(user.get('id')): user.get('email')
            for user in users
        }
        if parsed_args.username is None:
            usernames = [prompt_for_input(USERNAME_PROMPT)]
        else:
            usernames = parsed_args.username
        for user_item in usernames:
            if user_item in id_to_email:
                uid = user_item
                username = id_to_email.get(user_item)
            elif user_item in email_to_id:
                uid = email_to_id.get(user_item)
                username = user_item
            else:
                sys.exit(
                    f"[-] no user found with email or id '{user_item}'"
                )
            # TODO(dittrich): Add 'ya sure?' check.
            response = requests.delete(
                f"{base_url}/users/{uid}",
                headers=get_auth_headers(token=self.app.auth_token),
            )
            if response.status_code != status.HTTP_200_OK:
                sys.exit(
                    f"[-] failed to delete user '{user_item}': "
                    f'{response.status_code} {response.reason}'
                )
            self.logger.info(
                "[+] deleted user '%s' (id %s)", username, uid
            )

# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
