# -*- coding: utf-8 -*-

"""
Initialize the database.
"""

# Standard imports
import logging
import sys

# External imports
from cliff.command import Command

# Local imports


class CmdDBInit(Command):
    """
    Initialize the database.

    Create the database, schemas and tables (via ``alembic`` migrations),
    and seed the database with an initial superuser for immediate use.
    """

    logger = logging.getLogger(__name__)
    # requires_login = True

    def take_action(self, parsed_args):
        self.logger.info('[+] initializing the database...')
        sys.exit('[!] NOT IMPLEMENTED')


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
