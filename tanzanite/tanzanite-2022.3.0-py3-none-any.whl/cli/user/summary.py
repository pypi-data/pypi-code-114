# -*- coding: utf-8 -*-

"""
Summarize users in the database.
"""

# Standard imports
import logging

# External imports
from cliff.show import ShowOne

# Local imports
from tanzanite.cli.user import get_users_via_api


class CmdUserSummary(ShowOne):
    """
    Summarize data about users in the database.

    This includes::

        +-----------+---------------------------------------+
        | Field     | Description                           |
        +-----------+---------------------------------------+
        | total     | total number of users in the database |
        | active    | users who have `is_active` set        |
        | proctor   | users who have `is_proctor` set       |
        | superuser | users who have `is_superuser` set     |
        | min_id    | lowest user id value (usually 1)      |
        | max_id    | highest user id value                 |
        +-----------+---------------------------------------+
    """

    logger = logging.getLogger(__name__)
    requires_login = True

    def take_action(self, parsed_args):
        def count(users, prop=None):
            return len([user for user in users if user.get(prop) is True])

        users = get_users_via_api(
            skip=None,
            limit=None,
            auth_token=self.app.auth_token,
        )
        columns = (
            'total',
            'active',
            'proctor',
            'superuser',
            'min_id',
            'max_id',
        )
        data = [
            len(users),
            count(users, 'is_active'),
            count(users, 'is_proctor'),
            count(users, 'is_superuser'),
            min([user.get('id') for user in users]),
            max([user.get('id') for user in users])
        ]
        return columns, data


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
