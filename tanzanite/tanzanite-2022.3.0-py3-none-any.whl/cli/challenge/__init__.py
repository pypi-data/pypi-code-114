# -*- coding: utf-8 -*-

"""
`challenge` subcommands module initialization.
"""

# Standard imports
import json
import types

from typing import (
    List,
    Tuple,
    Union,
)
# External imports
import requests

from fastapi import status

# Local imports
from tanzanite.backend.app.app.schemas.challenge import Challenge
from tanzanite.core.security import get_auth_headers
from tanzanite.utils import get_api_base_url


LONG_ATTRIBUTES = ['owner_id', 'id']


def get_challenges_via_api(auth_token=None):
    """
    Get challenges via API call.
    """
    base_url = get_api_base_url()
    response = requests.get(
        f"{base_url}/challenges/",
        headers=get_auth_headers(token=auth_token),
    )
    if response.status_code == status.HTTP_200_OK:
        challenges = json.loads(response.text)
    elif response.status_code == status.HTTP_404_NOT_FOUND:
        challenges = []
    else:
        raise RuntimeError(
            "[-] failed to get challenges: "
            f'{response.status_code} {response.reason}'
        )
    return challenges


class ChallengeBag():
    """
    Class to index challenges for identification by title or id.
    """
    def __init__(self, challenges: List = None) -> None:
        """Initializer."""
        self.title_to_id = {}
        self.id_to_title = {}
        self.challenges = {}
        if challenges is not None:
            self.add_challenges(challenges=challenges)

    def add_challenge(self, challenge: Challenge) -> None:
        """
        Add a single challenge to saved state.
        """
        self.title_to_id[challenge.get('title')] = str(challenge.get('id'))
        self.id_to_title[str(challenge.get('id'))] = challenge.get('title')
        self.challenges[str(challenge.get('id'))] = challenge

    def add_challenges(self, challenges: List[Challenge]) -> None:
        """
        Add a list of challenges to saved state.
        """
        for challenge in challenges:
            self.add_challenge(challenge)

    def get_challenge(self, id_: str) -> Union[Challenge, None]:
        """
        Return the challenge record associated with a given id.
        """
        return self.challenges.get(str(id_))

    def get_title(self, id_: str) -> Union[str, None]:
        """
        Return the title associated with the given id or None.
        """
        return self.id_to_title.get(id_)

    def get_id(self, item: str) -> Union[Tuple, None]:
        """
        Return a tuple with the title and id for a challenge,
        or None.
        """
        if not isinstance(item, str):
            item = str(item)
        title, id_ = None, None
        if item in self.title_to_id:
            id_ = str(self.title_to_id.get(item))
            title = item
        elif item in self.id_to_title:
            id_ = str(item)
            title = self.id_to_title.get(item)
        return (title, id_)


# Patch in a new method to classes inheriting from cliff's abstract classes.

def record_challenge(self, challenge):
    """Accumulate data for bulk reporting."""
    # Ensure required object variables initialized.
    self.columns = getattr(self, 'columns', [])
    self.data = getattr(self, 'data', [])
    keys, values = [], []
    for (key, value) in challenge.items():
        keys.append(key)
        values.append(str(value))
    if len(self.columns) == 0:
        self.columns.extend(keys)
    self.data.extend([values])


from tanzanite.cli.challenge.create import CmdChallengeCreate
from tanzanite.cli.challenge.update import CmdChallengeUpdate


CmdChallengeUpdate.record_challenge = types.MethodType(record_challenge, CmdChallengeUpdate)  # noqa
CmdChallengeCreate.record_challenge = types.MethodType(record_challenge, CmdChallengeCreate)  # noqa

# vim: set ts=4 sw=4 tw=0 et :
