# noqa
import unittest
import os
from unittest import mock
from unittest.mock import patch
import requests_mock

from tyko import Tyko


class BaseTestCase(unittest.TestCase):

    def setUp(self):

        # Default mock of the API.
        self._api_mock = requests_mock.Mocker()

        self._api_mock.get(
            "https://api.tyko.ai/v0/projects/?name=my-project",
            status_code=200,
            json={"count": 0}
        )

        self._api_mock.post(
            "https://api.tyko.ai/v0/api_keys/",
            status_code=201,
            json={"key": "key"}
        )

        self._api_mock.post(
            "https://api.tyko.ai/v0/runs/", status_code=201, json={
                "id": 'r123',
                "url": "https://api.tyko.ai/v0/runs/123/"
            }
        )

        self._api_mock.post(
            "https://api.tyko.ai/v0/projects/",
            status_code=201,
            json={
                'name': 'My Project',
                'slugified_name': 'my-project',
                'id': '123',
                'url': 'https://api.tyko.ai/v0/projects/123/'
            }
        )
        self._api_mock.start()

    def tearDown(self):
        self._api_mock.stop()

    def test_base(self):
        assert True, "This is a simple test."

    @patch('netrc.open', mock.Mock(side_effect=FileNotFoundError))
    def test_netrc_not_found(self):
        tyko = Tyko(project_name="my-project")
        assert tyko.key == "key", "Obtain a new key."

    def test_new_key(self):
        tyko = Tyko(project_name="my-project")
        assert tyko.key == "key", "Obtain a new key."

    @mock.patch.dict(os.environ, {"TYKO_KEY": "yyy"}, clear=True)
    def test_key_from_env(self):
        tyko = Tyko(project_name="my-project")
        assert tyko.key == "yyy", "Get the key from env variables."


class LiveTestCase(unittest.TestCase):

    @patch('netrc.open', mock.Mock(side_effect=FileNotFoundError))
    def test_new_key(self):
        tyko = Tyko("my-project")
        self.assertEqual(len(tyko.key), 64)

    @patch('netrc.open', mock.Mock(side_effect=FileNotFoundError))
    def test_simple_log(self):
        tyko = Tyko("my-project")
        tyko.log({'x': 1.0, 'y': 1, 'z': 1.1})
