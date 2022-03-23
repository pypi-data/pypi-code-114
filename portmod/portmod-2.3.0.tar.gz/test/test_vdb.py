# Copyright 2022 Portmod Authors
# Distributed under the terms of the GNU General Public License v3

"""
Tests the mod selection system
"""

import pytest

from portmod.merge import configure
from portmod.vdb import VDB

from .env import setup_env, tear_down_env


@pytest.fixture(scope="module", autouse=True)
def setup_repo():
    yield setup_env("test")
    tear_down_env()


def test_vdb_untracked():
    """
    Tests that there are no untracked files in the VDB
    following package installation
    """
    configure(["test/test"])
    with VDB() as vdb:
        assert not vdb.git.ls_files(others=True, exclude_standard=True)
