import json
import os

import pytest

from tktl.commands.login import LogInCommand, SetApiKeyCommand
from tktl.core.exceptions import APIClientException


def test_set_api_key_command(capsys):
    cmd = SetApiKeyCommand()
    cmd.execute(api_key=None)
    out, err = capsys.readouterr()
    assert "API Key cannot be empty.\n" == err

    cmd.execute(api_key="ABC")
    assert os.path.exists(os.path.expanduser("~/.config/tktl/config.json"))
    with open(os.path.expanduser("~/.config/tktl/config.json"), "r") as j:
        d = json.load(j)
        assert d["api-key"] == "ABC"


def test_login_command(logged_in_context, capsys):
    cmd = LogInCommand()
    assert cmd.execute() is True
    out, err = capsys.readouterr()
    assert out == f"Authentication successful for user: {os.environ['TEST_USER']}\n"


def test_login_fail_command(capfd):
    cmd = LogInCommand()
    with pytest.raises(APIClientException):
        cmd.execute()
