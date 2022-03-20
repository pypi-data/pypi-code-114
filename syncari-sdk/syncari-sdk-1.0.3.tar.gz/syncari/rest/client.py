# pylint: disable=import-error
import backoff
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from syncari.logger import SyncariLogger

logger = SyncariLogger.get_logger('rest_client')

class RetryableException(Exception):
    """Class to mark an ApiException as retryable."""

# pylint: disable=too-many-instance-attributes
class SyncariRestClient:
    """
        Default Syncari Rest Client
    """
    def __init__(self, base_url, auth_config, rest_headers):
        self.auth_config = auth_config
        self.rest_url = base_url
        self.rest_headers = rest_headers
        self._session = requests.Session()

        retry_strategy = Retry(
            total=3,
            status_forcelist=[429, 500, 502, 503, 504],
            method_whitelist=["HEAD", "GET", "OPTIONS"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)

        adapter = requests.adapters.HTTPAdapter(max_retries=3)
        self._session.mount('https://', adapter)

    def get_url(self, url):
        """
            A default get url request
        """
        resp = self._retryable_request('GET', url, headers=self.rest_headers)
        print(resp.status_code)
        resp.raise_for_status()
        return resp

    @backoff.on_exception(backoff.expo,
                          RetryableException,
                          max_time=5 * 60, # in seconds
                          factor=30,
                          jitter=None)
    def _retryable_request(self, method, url, stream=False, **kwargs):
        """
            A retryable request call
        """
        req = requests.Request(method, url, **kwargs).prepare()
        resp = self._session.send(req, stream=stream)

        if resp.status_code == 500:
            raise RetryableException(resp)
        return resp

    def _request(self, method, url, **kwargs):
        """
            A non-retryable request call
        """
        logger.info("%s: %s", method, url)
        resp = self._retryable_request(method, url, **kwargs)
        return resp

    def rest_request(self, method, path, **kwargs):
        """
            Rest request with relative path. The rest_url (base_url) should be set
        """
        url = self.rest_url+path
        return self._request(method, url, headers=self.rest_headers, **kwargs)
