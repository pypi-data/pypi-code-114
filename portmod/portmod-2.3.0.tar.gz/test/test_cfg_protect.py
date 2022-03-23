# Copyright 2022 Portmod Authors
# Distributed under the terms of the GNU General Public License v3

import os
import sys
from io import StringIO

import pytest

from portmod._cli.main import main
from portmod.cfg_protect import get_redirections
from portmod.globals import env
from portmod.merge import configure

from .env import setup_env, tear_down_env


@pytest.fixture(scope="module", autouse=True)
def setup():
    """
    Sets up and tears down the test environment
    """
    dictionary = setup_env("test")
    os.makedirs(env.prefix().CONFIG_PROTECT_DIR, exist_ok=True)
    yield dictionary
    tear_down_env()


def test_cfg_protect(setup):
    """
    Tests that file protected by CFG_PROTECT don't get their changes overwritten
    when the package is re-installed
    """
    configure(["=test/test-1.0-r1"])
    path = os.path.join(env.prefix().ROOT, "etc", "test")

    with open(path, "a", encoding="utf-8") as file:
        print("bar = baz", file=file)
    with open(path, encoding="utf-8") as file:
        contents = file.readlines()

    configure(["=test/test-1.0-r1"])

    with open(path, encoding="utf-8") as file:
        assert contents == file.readlines()

    # Since the file was the same when re-installed,
    # it shouldn't get added to the list of pending config file updates
    assert not list(get_redirections())

    configure(["=test/test-1.0-r1"], delete=True)
    configure
    os.remove(path)


def test_cfg_protect_changed(setup, monkeypatch):
    """
    Tests that files protected by CFG_PROTECT get installed as separate files
    and registered with cfg_protect when an update changes the file
    """
    configure(["=test/test-1.0-r1"])
    path = os.path.join(env.prefix().ROOT, "etc", "test")

    with open(path, "a", encoding="utf-8") as file:
        print("bar = baz", file=file)
    with open(path, encoding="utf-8") as file:
        contents = file.readlines()

    configure(["=test/test-2.0"])

    # File should not have been changed directly
    with open(path, encoding="utf-8") as file:
        assert contents == file.readlines()

    # Since the file was the same when re-installed,
    # it shouldn't get added to the list of pending config file updates
    redirections = list(get_redirections())
    assert redirections
    src, dst = redirections[0]
    assert dst == path
    assert src == path + ".__cfg_protect__"
    with open(src, encoding="utf-8") as file:
        assert file.read() == "foo = baz\n"

    env.INTERACTIVE = True
    monkeypatch.setattr("sys.stdin", StringIO("y\n"))
    sys.argv = ["portmod", "test", "cfg-update"]
    main()

    with open(path, encoding="utf-8") as file:
        assert file.read() == "foo = baz\n"
