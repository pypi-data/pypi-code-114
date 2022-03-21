# -*- coding: utf-8 -*-

# pylint: disable=missing-module-docstring

# Standard imports
import logging
import sys

# External imports
import requests

# TODO(dittrich): https://github.com/Mckinsey666/bullet/issues/2
# Workaround until bullet has Windows missing 'termios' fix.
try:
    from bullet import Input
    from bullet import colors
except ModuleNotFoundError:
    pass
from cliff.command import Command
from fastapi import status
from prettytable import PrettyTable

# Local imports
from tanzanite.backend.app.app import schemas
from tanzanite.core.security import get_auth_headers
from tanzanite.cli.challenge import (
    get_challenges_via_api,
    ChallengeBag,
)
from tanzanite.utils import get_api_base_url


def confirm_delete_challenge(challenge: schemas.Challenge):
    """
    Produce a table of challenge details and confirm the user wants to
    delete the challenge.

    Returns a boolean for whether to delete or not.
    """
    id_ = challenge.get('id')
    table = PrettyTable()
    table.field_names = ('Attribute', 'Value')
    table.align = 'l'
    for key, value in challenge.items():
        table.add_row((key, value))
    print(table)
    cli = Input(
        f"Type the challenge id '{id_}' to confirm: ",
        default="",
        word_color=colors.foreground["yellow"]
    )
    confirm = cli.launch()
    return confirm == str(id_)


class CmdChallengeDelete(Command):
    """
    Delete challenges from the database.

    Delete one or more challenges from the Tanzanite database
    by specifying them by ``id`` on the command line, or delete
    all of them at once with the ``--all`` flag.

    Use the ``--force`` flag to prevent being asked to confirm
    deletions. Otherwise, you will be shown details and asked to
    enter the ``id`` value to confirm::

        $ tz challenge delete 5
        +-------------+--------------------------------------------------------------------------+
        | Attribute   | Value                                                                    |
        +-------------+--------------------------------------------------------------------------+
        | title       | Mobile Malware                                                           |
        | author      | Honeynet Project                                                         |
        | url         | https://www.honeynet.org/challenges/forensic-challenge-9-mobile-malware/ |
        | description | Perform analysis of a real compromised smartphone running a popular OS.  |
        | date_posted | 2011-11-01                                                               |
        | id          | 5                                                                        |
        | owner_id    | 1                                                                        |
        +-------------+--------------------------------------------------------------------------+
        Type the challenge id '5' to confirm: 5
        [+] deleted challenge id 5 ('Mobile Malware')
    """  # noqa

    logger = logging.getLogger(__name__)
    requires_login = True

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument(
            'arg',
            nargs='*',
            default=None,
            help='Challenge id or title'
        )
        parser.add_argument(
            '-a', '--all',
            action='store_true',
            default=False,
            help='Delete all challenges'
        )
        parser.add_argument(
            '--force',
            action='store_true',
            default=False,
            help='Delete without confirmation'
        )
        return parser

    def take_action(self, parsed_args):  # noqa C901
        challenges = get_challenges_via_api(auth_token=self.app.auth_token)
        if len(challenges) < 1:
            sys.exit('[-] there are no challenges in the database')
        if parsed_args.all is None and parsed_args.arg is None:
            # TODO(dittrich): Add menu selection feature ala psec
            sys.exit('[-] no challenge id or title specified')
        challenge_bag = ChallengeBag(challenges)
        if parsed_args.all:
            arg_challenges = [challenge.get('id') for challenge in challenges]
        else:
            arg_challenges = []
            for arg in parsed_args.arg:
                _, id_ = challenge_bag.get_id(arg)
                if id_ is None:
                    sys.exit(f"[-] challenge '{arg}' not found")
            arg_challenges.append(id_)
        base_url = get_api_base_url()
        for id_ in arg_challenges:
            if id_ is None:
                sys.exit(f"[-] challenge '{id_}' not found")
            if not parsed_args.force:
                if not confirm_delete_challenge(
                    challenge=challenge_bag.get_challenge(id_)
                ):
                    self.logger.info('[-] cancelled deleting challenge')
                    return
            response = requests.delete(
                f"{base_url}/challenges/{id_}",
                headers=get_auth_headers(token=self.app.auth_token),
            )
            if response.status_code != status.HTTP_200_OK:
                sys.exit(
                    f"[-] failed to delete challenge '{id_}': "
                    f'{response.status_code} {response.reason}'
                )
            self.logger.info(
                "[+] deleted challenge id %s ('%s')",
                id_,
                challenge_bag.get_title(id_)
            )


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
