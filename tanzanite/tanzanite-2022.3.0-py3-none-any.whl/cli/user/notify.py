# -*- coding: utf-8 -*-

# Standard imports
import logging
import sys
import textwrap

# External imports
from cliff.command import Command

# Local import


class CmdUserNotify(Command):
    """Send email notifications to users in the database."""

    logger = logging.getLogger(__name__)
    requires_login = True

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument(
            'arg',
            nargs='?',
            default=None
        )
        parser.epilog = textwrap.dedent("""
            Sends email notifications to one or more users in the
            Tanzanite database.
            """)
        return parser

    def take_action(self, parsed_args):
        se = self.app.secrets
        se.requires_environment(path_only=True)
        se.read_secrets_descriptions()
        if parsed_args.arg is None:
            sys.exit('[-] no user name(s) specified')
        sys.exit('[!] NOT IMPLEMENTED YET')


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
