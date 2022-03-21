# -*- coding: utf-8 -*-

"""
Show details for a single challenge.
"""

# Standard imports
import logging
import sys

# External imports
from cliff.show import ShowOne

# Local imports
from tanzanite.cli.challenge import (
    LONG_ATTRIBUTES,
    get_challenges_via_api,
    ChallengeBag,
)


class CmdChallengeShow(ShowOne):
    """
    Show details about a challenge.
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
        parser.add_argument(
            '-l', '--long',
            action='store_true',
            dest='long',
            default=False,
            help='Return long set of attributes'
        )
        return parser

    def take_action(self, parsed_args):
        challenges = get_challenges_via_api(auth_token=self.app.auth_token)
        if parsed_args.arg is None:
            # TODO(dittrich): Add menu selection feature ala psec
            sys.exit('[-] no challenge id or title specified')
        arg = parsed_args.arg.pop()
        challenge_bag = ChallengeBag(challenges)
        _, id_ = challenge_bag.get_id(arg)
        if id_ is None:
            sys.exit(f"[-] challenge '{arg}' not found")
        challenge = challenge_bag.get_challenge(id_)
        if parsed_args.long:
            columns = ([key for key in challenges[0].keys()])
        else:
            columns = ([
                key for key in challenges[0].keys()
                if key not in LONG_ATTRIBUTES
            ])
        data = ([
            str(value) for key, value in challenge.items()
            if key in columns
        ])
        return columns, data


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
