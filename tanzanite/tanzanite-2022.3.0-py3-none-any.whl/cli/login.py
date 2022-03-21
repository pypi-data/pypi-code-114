# -*- coding: utf-8 -*-

"""
Log in to user account from command line and save JWT in python-secrets
environment directory for future CLI operations.
"""

# External imports
import logging
import sys

from cliff.command import Command
from psec.utils import safe_delete_file


# Local imports
from tanzanite.core.security import (
    get_cached_auth_token,
    get_jwt_path,
    cli_login_for_access_token,
    prompt_for_login_creds,
)
# from tanzanite.utils import (
#     prompt_for_password,
# )


class CmdLogin(Command):
    """
    Log in to Tanzanite account.

    Logging in consists of acquiring a JWT token from the Tanzanite API
    server by matching login user name (email) and password. The JWT is
    cached locally for further commands to use to reduce the number of
    times this handshake is required.
    """

    logger = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument(
            'username',
            nargs='?',
            default=None
        )
        parser.add_argument(
            'password',
            nargs='?',
            default=None
        )
        return parser

    def take_action(self, parsed_args):
        jwt_path = get_jwt_path()
        auth_token = get_cached_auth_token(jwt_path=jwt_path)
        if auth_token is not None:
            self.logger.debug("[+] already logged in")
            sys.exit(0)
        se = self.app.secrets
        # se.requires_environment()
        # se.read_secrets_descriptions()
        admin_username = se.get_secret("tanzanite_admin_user_email")
        admin_password = se.get_secret("tanzanite_admin_password")
        if parsed_args.username is None:
            self.logger.debug(
                '[+] defaulting to username %s', admin_username
            )
            username = admin_username
        else:
            username = parsed_args.username
        if parsed_args.password is not None:
            password = parsed_args.password
        else:
            if username == admin_username:
                # password = se.get_secret("tanzanite_admin_password")
                password = admin_password
            else:
                # password = prompt_for_password()
                prompt_for_login_creds(username=username)
        # self.app.auth_token = get_cached_auth_token(
        #     username=username,
        #     password=password
        # )
        auth_token = cli_login_for_access_token(
            jwt_path=jwt_path,
            cache_auth_token=(not self.app_args.disallow_auth_token_cache),
            username=username,
            password=password,
        )
        if auth_token is None:
            sys.exit('[-] failed to log in')
        else:
            self.logger.info('[+] login successful')


class CmdLogout(Command):
    """
    Log out of Tanzanite account.

    Logging out consists of deleting the cached JWT (if any).
    """

    logger = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        jwt_path = get_jwt_path()
        if not jwt_path.exists():
            self.logger.warning('[-] not logged in')
        else:
            self.logger.debug("[-] removing JWT '%s'", jwt_path)
            try:
                safe_delete_file(str(jwt_path))
            except RuntimeError:
                sys.exit(f"[!] failed to remove JWT '{jwt_path}'")
            self.logger.info('[+] logged out')


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
