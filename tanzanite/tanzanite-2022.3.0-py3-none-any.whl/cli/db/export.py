# -*- coding: utf-8 -*-

"""
Export the database.
"""

# Standard imports
import logging
import sys

# External imports
from cliff.command import Command

# Local imports
# from tanzanite.cli.challenge import get_challenges_via_api
# from tanzanite.cli.user import get_users_via_api


class CmdDbExport(Command):
    """
    Export the database.
    """

    logger = logging.getLogger(__name__)
    requires_login = True

    def take_action(self, parsed_args):
        sys.exit('[-] NOT IMPLEMENTED')

# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
