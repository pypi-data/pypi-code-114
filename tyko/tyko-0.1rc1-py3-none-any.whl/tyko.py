# coding=utf-8
"""Tyko library."""
__version__ = '0.1rc1'

import logging
import netrc
import os
from typing import Dict
from urllib.parse import urljoin, urlparse

import requests

logger = logging.getLogger(__name__)


_TYKO_KEY = 'TYKO_KEY'
_TYKO_VER = 'v0'


class Tyko:
    """Main class for reporting to Tyko."""

    _hostname = 'api.tyko.ai'
    _prefix_url: str
    _session: requests.Session
    _cur_key: str

    # Run Information
    _run_id: str = None
    _run_url: str = None

    # Project ID.
    _project_id: str = None
    _project_url: str = None
    _project_name: str = None
    _project_slugified_name: str = None

    def _get_new_key(self) -> str:
        res = self._session.post(self._fix_url('/v0/api_keys/'))
        return res.json()['key']

    def _serialize_data(self, value: any) -> str:

        if isinstance(value, dict):
            return {k: self._serialize_data(v) for k, v in value.items()}

        if isinstance(value, str):
            return {'value': value, 'type': 'str'}

        if isinstance(value, int):
            return {'value': value, 'type': 'int'}

        if isinstance(value, float):
            return {'value': value, 'type': 'float'}

        return {'value': str(value), 'type': str(type(value))}

    def _log(self, data: Dict[str, any]):
        self._session.post(
            f'/v0/projects/{self._project_id}/logs/',
            data=self._serialize_data(data)
        )

    def _set_run(self, data):
        self._run_id = data['id']
        self._run_url = data['url']

    def _set_project(self, data: dict):
        self._project_url = data['url']
        self._project_id = data['id']
        self._project_slugified_name = data['slugified_name']
        self._project_name = data['name']

    def _create_run(self):
        res = self._post('/v0/runs/', {'config': {}})
        if res.status_code == 201:
            self._set_run(res.json())
        else:
            logger.error(res.content)
            raise Exception('Problems with the API.')

    def _create_or_get_project(self, name: str) -> str:

        # Try this several times in case of race conditions.
        for _i in range(10):

            # Try to get the current project.
            res = self._get('/v0/projects/', {'name': name})
            if res.status_code != 200:
                raise Exception('Problems with the API.')

            # Get the found project.
            res = res.json()
            if res['count'] > 0:
                self._set_project(res['results'][0])
                break

            # Try to create the project.
            res = self._post('/v0/projects/', {'name': name})
            if res.status_code == 201:
                res = res.json()
                logger.info(f"Project '{name}' created.")
                logger.debug(f'API Response: {res}')
                self._set_project(res)
                break

        if self._project_id is None:
            # TODO: This should not stop the experiment, it should save
            # local data that can be used later to upload to the server.
            raise Exception('Error creating project!')

    def _resolve_key(self, netrc_file: str = None):
        if not hasattr(self, '_cur_key'):
            if _TYKO_KEY in os.environ:
                self._cur_key = os.environ[_TYKO_KEY]
            else:
                try:
                    netrc_ = netrc.netrc(netrc_file)
                except FileNotFoundError:
                    netrc_ = None
                if netrc_ is not None and self._hostname in netrc_.hosts:
                    self._cur_key = netrc_.hosts[self._hostname][2]
                else:
                    self._cur_key = self._get_new_key()
                    print(f'A new key was created: {self._cur_key}') # noqa

        # Add key to sessions.
        self._session.headers['X-API-KEY'] = self._cur_key
        return self._cur_key

    def _headers(self):
        self._resolve_key()

    def _fix_url(self, url: str) -> str:
        return urljoin(self._prefix_url, url)

    def _get(self, url: str, params: dict = None) -> requests.Response:
        """GET request to the backend."""
        if params is None:
            params = {}

        return self._session.get(self._fix_url(url), params=params)

    def _post(self, url: str, data: dict = None):
        """POST request to the backend."""
        return self._session.post(self._fix_url(url), json=data)

    @property
    def key(self) -> str:
        """Return the API key used by the current instance."""
        return self._resolve_key()

    def log(self, values: Dict[str, any]):
        """Create a log entry in the current run."""
        res = self._post(
            '/v0/logs/', data={'run': self._run_url, 'data': values}
        )
        if res.status_code != 201:
            logger.error(res.content)
            raise Exception('Problems with the API')

    def __init__(
        self, project_name: str, desc: str = None, prefix_url: str = None
    ):
        """Nothing here."""
        if prefix_url is None:
            prefix_url = 'https://api.tyko.ai'

        """Keep track of prefix url."""
        self._session = requests.Session()
        self._prefix_url = prefix_url
        self._hostname = urlparse(prefix_url).hostname
        self._resolve_key()

        # Create the project.
        self._create_or_get_project(project_name)

        # TODO: Check if it's better to do this as a context manager.
        # TODO: Add configurations.
        # Create a run
        self._create_run()
