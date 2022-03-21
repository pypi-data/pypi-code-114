# -*- coding: utf-8 -*-

"""
Delete the database.
"""

# Standard imports
import logging
import sys

# External imports
from cliff.command import Command

# Local imports
# from tanzanite.cli.challenge import (
#     get_challenges_via_api,
#     ChallengeBag,
# )


class CmdDbDelete(Command):
    """
    Delete the database.
    """

    logger = logging.getLogger(__name__)
    requires_login = True

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument(
            'arg',
            nargs=1,
            default=None,
            help='Challenge id or title'
        )

    def take_action(self, parsed_args):

        sys.exit('[-] NOT IMPLEMENTED')

# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
