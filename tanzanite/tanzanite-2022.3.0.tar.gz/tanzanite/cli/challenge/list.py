# -*- coding: utf-8 -*-

"""
List challenges in the database.
"""

# Standard imports
import logging
import sys

# External imports
from cliff.lister import Lister

# Local imports
from tanzanite.cli.challenge import (
    LONG_ATTRIBUTES,
    get_challenges_via_api,
)


class CmdChallengeList(Lister):
    """
    List challenges in the database.

    Lists one or more challenges in the Tanzanite database with a
    minimal set of properties that excludes ``owner_id`` and ``id``.
    This default set of properties is suitable for exporting the
    contents of the ``challenge`` table for later importing using
    ``--format json`` and redirecting to a file.

    Use the ``--long`` flag to output all properties. You may want
    to also use ``--fit-width`` to minimize line wrapping, or select
    only the database table columns you need with ``-c``.

    By default, all challenges are listed. If you want to only see
    a few, specify them by ``id`` or ``title`` as arguments on the
    command line.
    """

    logger = logging.getLogger(__name__)
    requires_login = True

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument(
            '-l', '--long',
            action='store_true',
            dest='long',
            default=False,
            help='Return long set of attributes'
        )
        parser.add_argument(
            'arg',
            nargs='?',
            default=None,
            help="Challenge title or id"
        )
        return parser

    def take_action(self, parsed_args):
        challenges = get_challenges_via_api(auth_token=self.app.auth_token)
        if len(challenges) < 1:
            sys.exit('[-] there are no challenges in the database')
        if parsed_args.long:
            columns = ([key for key in challenges[0].keys()])
        else:
            columns = ([
                key for key in challenges[0].keys()
                if key not in LONG_ATTRIBUTES
            ])
        data = [
            [
                value for key, value in challenge.items()
                if key in columns
            ]
            for challenge in challenges
        ]
        return columns, data

# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
