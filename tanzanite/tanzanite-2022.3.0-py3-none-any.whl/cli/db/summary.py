# -*- coding: utf-8 -*-

"""
Summarize the database.
"""

# Standard imports
import json
import logging
import sys

# External imports
import requests
from cliff.show import ShowOne
from fastapi import status

# Local imports
from tanzanite.core.security import get_auth_headers
from tanzanite.utils import get_api_base_url


class CmdDBSummary(ShowOne):
    """
    Summarize data about the database.

    This command can be used to verify that the API server is accessible
    and the database is connected. When running a local server for
    testing, the output would look like this::

        +------------+--------------------------------------+
        | Field      | Value                                |
        +------------+--------------------------------------+
        | dialect    | sqlite+pysqlite                      |
        | db_file    | /tmp/.tzsecrets/batstest/batstest.db |
        | exists     | True                                 |
        | users      | 1                                    |
        | challenges | 0                                    |
        +------------+--------------------------------------+
    """

    logger = logging.getLogger(__name__)
    requires_login = True

    def take_action(self, parsed_args):  # noqa
        base_url = get_api_base_url()
        response = requests.get(
            f"{base_url}/utils/db/",
            headers=get_auth_headers(token=self.app.auth_token)
        )
        if response.status_code != status.HTTP_200_OK:
            sys.exit(f'[-] FAILED: {response.status_code} {response.reason}')
        results = json.loads(response.text)
        db_data = json.loads(results['msg'])
        columns = []
        data = []
        for key, value in db_data.items():
            columns.append(key)
            data.append(value)
        return columns, data


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
