import datetime
import json
import logging
import os
import shutil
from enum import Enum
from typing import Optional

from asgiref.sync import async_to_sync
from envparse import env
from vtb_http_interaction.process_authorization_header import MemoryCache
from vtb_http_interaction.services import AuthorizationHttpService, HttpServiceWithRequestId

from state_service_utils.conf import (
    REFERENCES_MOCK,
    REFERENCES_HOST_URL,
    SSL_VERIFY,
    REFERENCES_TIMEOUT,
    REFERENCES_FETCH_INTERVAL,
    KEYCLOAK_CONFIG
)
from state_service_utils.exceptions import BadStatusCodeError

logger = logging.getLogger('default')


def _create_enums_values(data: dict) -> dict:
    return {k: v if v is not None else k.lower() for k, v in data.items()}


def _deserialize(data: list) -> dict:
    return {ref['name']: Enum(ref['name'], _create_enums_values(ref['data'])) for ref in data}


class EnumsClient:  # __base__
    def __init__(self, *args, **kwargs):
        self._data = dict()

    def __getattr__(self, item):
        if item not in self._data:
            self.update()
        return self._data[item]

    def update(self):
        raise NotImplementedError


class EnumsHttpClient(EnumsClient):
    def __init__(self, url, timeout, service, ssl_verify=True, fetch_interval=60, *args, **kwargs):
        super(EnumsHttpClient, self).__init__(*args, **kwargs)

        self._url = url
        self._timeout = timeout
        self._ssl_verify = ssl_verify
        self._service = service
        self.fetch_interval = datetime.timedelta(seconds=fetch_interval)
        self.last_fetch = None

    def __getattr__(self, item):
        if self.last_fetch + self.fetch_interval <= datetime.datetime.now():
            self.update()
            return self._data[item]
        return super(EnumsHttpClient, self).__getattr__(item)

    def update(self) -> bool:
        fetching_dt = datetime.datetime.now()
        try:
            data = self.fetch_remote()
        except Exception as err:
            msg = (
                'Exception while connecting to references service. '
                f'REFERENCES_HOST_URL: {self._url}, '
                f'REFERENCES_TIMEOUT: {self._timeout}, '
                f'Original exception: {err}'
            )
            # if there is only the first connection attempt, then raise ConnectionError
            if not self.last_fetch:
                raise ConnectionError(msg)
            # otherwise, log it and try to reconnect after the period
            logger.warning(msg, exc_info=False)
            self.last_fetch = fetching_dt
            return False
        self._data = _deserialize(data)
        self.last_fetch = fetching_dt
        logger.debug(f"updated: {', '.join((k for k in self._data))}")
        return True

    def fetch_remote(self) -> list:
        request = {
            'method': "GET",
            'url': self._url,
            'cfg': {'timeout': self._timeout, 'ssl': self._ssl_verify}
        }

        async def request_wrapper():  # unable to use `functools.partial()`
            return await self._service.send_request(**request)

        status, resp_data = async_to_sync(request_wrapper)()
        if not (200 <= status < 400):
            raise BadStatusCodeError(f'server status code: {status}')
        if not isinstance(resp_data, list):
            raise ValueError(f'server response should be a list.')
        return resp_data


class EnumsCacheFileClient(EnumsClient):
    def __init__(self, cache_file, *args, **kwargs):
        super(EnumsCacheFileClient, self).__init__(*args, **kwargs)
        self._cache_file = self._create_cache_file(cache_file)

    def update(self) -> bool:
        with open(self._cache_file) as f:
            data = json.load(f)
        self._data = _deserialize(data)
        return True

    @staticmethod
    def _create_cache_file(file_path: Optional[str]):
        if not file_path:
            file_path = '/cache/enums.json'
        cache_file = os.path.join(os.getcwd(), *file_path.split('/'))
        if not os.path.exists(cache_file):
            logger.warning(
                "You're using `REFERENCES_MOCK` without providing cache file.\n"
                "It will be automatically created with data from template.\n"
                "Now you can manually add or change any enums in %s" % cache_file
            )
            os.makedirs(os.path.dirname(cache_file), exist_ok=True)
            src = os.path.join(os.path.dirname(__file__), 'datafiles/enums_template.json')
            shutil.copy(src, cache_file)
        return cache_file


def _initialize() -> EnumsClient:
    if REFERENCES_MOCK:
        return EnumsCacheFileClient(cache_file=env.str('REFERENCES_MOCK_FILE', default=''))
    service = AuthorizationHttpService(
        KEYCLOAK_CONFIG, token_cache=MemoryCache()
    ) if KEYCLOAK_CONFIG else HttpServiceWithRequestId()
    client = EnumsHttpClient(
        url=REFERENCES_HOST_URL, ssl_verify=SSL_VERIFY,
        timeout=REFERENCES_TIMEOUT, fetch_interval=REFERENCES_FETCH_INTERVAL,
        service=service
    )
    client.update()
    return client


enums = _initialize()
