import logging
import requests
import sys

ATF_LOGGER = logging.getLogger('APC_Temp_fetch')

class ApcKind:
    def __init__(self, host: str, rqargs, **kwargs):
        # forwards all unused arguments, to make this class usable as a mixin
        super().__init__(**kwargs) # type: ignore[call-arg]

        self._host = host
        self._rqargs = rqargs

    def urlway(self, num: int, in_url: str, handler, **kwargs):
        ATF_LOGGER.debug(F'{self._host}: [{num}] {in_url}')
        try:
            r = handler(in_url, **kwargs, **self._rqargs)
            ATF_LOGGER.debug(F'{self._host}: [{num}] -> {r.url}')
            if 'stream' in kwargs and bool(kwargs['stream']) and r.encoding is None:
                r.encoding = 'utf-8'
            return r
        except Exception as e:
            # it does not make sense to try to use r.url here, it may be unavailable
            ATF_LOGGER.error(F'{self._host}: [{num}] while fetching {in_url}: {repr(e)}')
            # do not use ATF_LOGGER.exception because we re-raise
            # the exception and don't want to clutter the output
            raise

    def fetch(self, user: str, password: str):
        raise NotImplementedError

    @staticmethod
    def extract(upsst) -> str:
        """extract the temperature from the return value of the `fetch` method"""
        raise NotImplementedError

class AuthError(Exception):
    def __init__(self, message='authentification failed'):
        super().__init__(message)

# source: https://github.com/psf/requests/issues/2773#issuecomment-174312831
class NullAuth(requests.auth.AuthBase):
    '''force requests to ignore the ``.netrc``

    Some sites do not support regular authentication, but we still
    want to store credentials in the ``.netrc`` file and submit them
    as form elements. Without this, requests would otherwise use the
    .netrc which leads, on some sites, to a 401 error.

    Use with::

        requests.get(url, auth=NullAuth())
    '''

    def __call__(self, r): return r
