# -*- coding: utf-8 -*-

"""
Update a challenge in the database.
"""

# Standard imports
import argparse
import json
import logging
import sys

# External imports
import requests

from cliff.lister import Lister
from fastapi import status
from fastapi.encoders import jsonable_encoder
from pydantic import ValidationError  # pylint: disable=no-name-in-module

# Local imports
from tanzanite.backend.app.app.schemas.challenge import ChallengeUpdate
# from tanzanite.backend.app.app.models.challenge import Challenge
from tanzanite.cli.challenge import (
    get_challenges_via_api,
    ChallengeBag,
)
from tanzanite.core.security import get_auth_headers
from tanzanite.utils import (
    check_update,
    get_api_base_url,
)


class CmdChallengeUpdate(Lister):
    """
    Update a challenge in the database.

    This command allows you to update one or more properties at a time for
    one or more challenges in the Tanzanite database. Properties are selected by
    command line options and challenges are specified by either their title or
    their internal id value.

    Setting properties for more than one challenge at a time does not make sense
    for all properties that are typically unique to each challenge, such as ``title``
    and ``description``. Other properties, like active status, ``owner_id`` or
    or ``author``, can be changed in bulk.  The flag ``--all`` allows you to
    apply the change to all accounts in the database.

    Changes are made one at a time by specifying the challenge by its ``id`` or
    ``title`` and what to change. Changes to ``active`` status can be changed for
    more than one challenge at a time, while changes the attribute to change,
    and the new value.

    You will be prompted to these if they are not specified, as well as prompted to
    confirm the action prior to applying the updates.  If you use the ``--force``
    flag, no confirmation will be required.
    """  # noqa

    logger = logging.getLogger(__name__)
    requires_login = True

    def __init__(self, args, app_args, cmd_name=None):
        super().__init__(args, app_args, cmd_name=cmd_name)
        self.data = []

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument(
            'arg',
            nargs='*',
            default=None,
            help='Challenge id or title'
        )
        parser.add_argument(
            '--all',
            action='store_true',
            default=False,
            help='Apply changes to all challenges'
        )
        parser.add_argument(
            '--force',
            action='store_true',
            default=False,
            help='Update without confirmation'
        )
        parser.add_argument(
            '--active',
            action=argparse.BooleanOptionalAction,
            default=None,
            help='Mark as active'
        )
        parser.add_argument(
            '--author',
            default=None,
            help='New ``author`` for the challenge'
        )
        parser.add_argument(
            '--title',
            default=None,
            help='New ``title`` for the challenge'
        )
        parser.add_argument(
            '--description',
            default=None,
            help='New ``description`` for the challenge'
        )
        parser.add_argument(
            '--url',
            default=None,
            help='New ``url`` for the challenge'
        )
        parser.add_argument(
            '--owner-id',
            default=None,
            help='New ``owner_id`` for the challenge'
        )
        return parser

    def take_action(self, parsed_args):  # noqa C901
        if parsed_args.all is None and parsed_args.arg is None:
            # TODO(dittrich): Add menu selection feature ala psec
            sys.exit('[-] no challenge id or title specified')
        base_url = get_api_base_url()
        challenges = get_challenges_via_api(auth_token=self.app.auth_token)
        challenge_bag = ChallengeBag(challenges)
        if (
            (parsed_args.all or len(parsed_args.arg) > 1)
            and (
                parsed_args.description is not None
                or parsed_args.title is not None
            )
        ):
            sys.exit(
                "[-] can't set `description` or `title` "
                "for multiple challenges"
            )
        arg_challenges = (
            [challenge.get('title') for challenge in challenges]
            if parsed_args.all
            else parsed_args.arg
        )
        for arg in arg_challenges:
            title, id_ = challenge_bag.get_id(arg)
            if id_ is None:
                sys.exit(f"[-] challenge '{arg}' not found")
            challenge = challenge_bag.get_challenge(id_)
            updates = jsonable_encoder(ChallengeUpdate(**challenge))
            arg_to_attribute = {
                'title': 'title',
                'author': 'author',
                'owner_id': 'owner_id',
                'url': 'url',
                'description': 'description',
            }
            if not check_update(parsed_args, updates, arg_to_attribute):
                self.logger.info(
                    "[-] no changes to challenge id %s ('%s')", id_, title
                )
                continue
            try:
                challenge_update = ChallengeUpdate(**updates)
            except ValidationError:
                self.app.stderr.write(f"[-] challenge: '{title}'\n")
                raise
            response = requests.put(
                f"{base_url}/challenges/{id_}",
                headers=get_auth_headers(token=self.app.auth_token),
                data=challenge_update.json(),
            )
            if response.status_code != status.HTTP_200_OK:
                sys.exit(
                    f"[-] failed to update challenge '{id_}': "
                    f'{response.status_code} {response.reason}'
                )
            updated_challenge = json.loads(response.text)
            # This method is injected in
            # tanzanite/cli/challenge/__init__.py
            self.record_challenge(updated_challenge)  # pylint: disable=not-callable  # noqa
            self.logger.info(
                "[+] updated challenge id %s ('%s')",
                id_,
                updated_challenge.get('title')
            )
        if self.app_args.verbose_level < 1 or len(self.data) == 0:
            sys.exit(0)
        return self.columns, self.data


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
