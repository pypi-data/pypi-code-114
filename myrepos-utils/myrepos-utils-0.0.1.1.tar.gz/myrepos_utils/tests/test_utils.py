#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (c) Meta Platforms, Inc. and affiliates.
#
# Fedora-License-Identifier: GPLv2+
# SPDX-2.0-License-Identifier: GPL-2.0+
# SPDX-3.0-License-Identifier: GPL-2.0-or-later
#
# This program is free software.
# For more information on the license, see COPYING.md.
# For more information on free software, see
# <https://www.gnu.org/philosophy/free-sw.en.html>.

import os
from myrepos_utils import utils
from unittest import mock


REPOS = [
    "src/github/owner1/projA",
    "src/gitlab/owner2/projB",
]


def get_mock_config():
    mock_config = mock.Mock()
    mock_config.keys.return_value = iter(REPOS)
    return mock_config


def test_get_repos():
    mock_config = get_mock_config()
    result = utils.get_repos(mock_config)
    mock_config.keys.assert_called_once()
    assert result == REPOS


def test_find_repo():
    mock_config = get_mock_config()
    result = utils.find_repo("github", mock_config)
    mock_config.keys.assert_called_once()
    assert result == [os.path.expanduser(f"~/{REPOS[0]}")]
