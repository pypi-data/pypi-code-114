# -*- coding: utf-8 -*-

"""
Create challenges in the database
"""

# Standard imports
import logging
import sys
import os

# External imports
import csv
import json
import requests

from cliff.command import Command
from fastapi import status
from pydantic import ValidationError

# Local imports
from tanzanite.backend.app.app.schemas.challenge import ChallengeCreate
from tanzanite.core.security import get_auth_headers
from tanzanite.utils import get_api_base_url


def _get_new_challenges(infile=None):
    """Get challenge metadata."""
    if infile is None:
        challenges = _get_new_challenges_from_user()
    else:
        challenges = _get_new_challenges_from_file(infile=infile)
    return challenges


def _get_new_challenges_from_user():
    challenges = []
    return challenges


def _get_new_challenges_from_file(infile=None):
    ext = os.path.splitext(infile)[1].lower()
    challenges = []
    if ext == '.csv':
        challenges = _read_csv(infile=infile)
    elif ext == '.json':
        challenges = _read_json(infile=infile)
    else:
        sys.exit(
            f"[-] file type '{ext}' is not supported: "
            "must be 'csv' or 'json'."
        )
    # Validate entries before returning results.
    for challenge in challenges:
        try:
            ChallengeCreate(**challenge)
        except ValidationError as err:  # pylint: disable=unused-variable  # noqa
            sys.stderr.write(f"[-] {str(challenge)}\n")
            raise
    return challenges


def _read_json(infile=None):
    with open(infile, mode='r', encoding='utf-8') as infile_h:
        content = json.loads(infile_h.read())
    return content


def _read_csv(infile=None):
    reader = csv.DictReader(open(infile, mode='r', encoding='utf-8'))
    challenges = [item for item in reader]
    return challenges


class CmdChallengeCreate(Command):
    """
    Create challenges in the database.

    Creates one or more challenges in the Tanzanite database.
    """

    logger = logging.getLogger(__name__)
    requires_login = True

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument(
            'challenge',
            nargs='?',
            default=None
        )
        parser.add_argument(
            '-i', '--import',
            action='store',
            dest='import_file',
            default=None,
            help='Import challenges metadata from a file'
        )
        return parser

    def take_action(self, parsed_args):
        if parsed_args.import_file is not None:
            challenges = _get_new_challenges(infile=parsed_args.import_file)
        else:
            raise RuntimeError(
                '[!] creating individual challenges not implemented yet'
            )
        errors = 0
        for challenge in challenges:
            title = challenge.get('title')
            author = challenge.get('author')
            title_author = f"'{title}' ({author})"
            base_url = get_api_base_url()
            response = requests.post(
                f"{base_url}/challenges/",
                headers=get_auth_headers(token=self.app.auth_token),
                json=challenge,
            )
            if response.status_code == status.HTTP_200_OK:
                self.logger.info(
                    "[+] added challenge '%s'", title)
            elif response.status_code == status.HTTP_409_CONFLICT:
                self.app.stderr.write(
                    f'[-] creating {title_author} failed: '
                    f'{response.json()["detail"]}\n'
                )
                errors += 1
            else:
                sys.exit(
                    '[-] failed to create challenge: '
                    f'{response.status_code} {response.reason}'
                )
        if errors > 0:
            sys.exit(1)


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
