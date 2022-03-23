import inspect

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

DEFAULT_TIMEOUT = 5


def get_retry_strategy(
        total=3,
        backoff_factor=0.01,
        raise_on_status=False,
        status_forcelist=[413, 429, 500, 501, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "PUT", "DELETE", "OPTIONS", "TRACE"],
        **kwargs):
    if "allowed_methods" in inspect.getfullargspec(Retry.__init__).args:
        return Retry(total=total,
                     backoff_factor=backoff_factor,
                     raise_on_status=raise_on_status,
                     status_forcelist=status_forcelist,
                     allowed_methods=allowed_methods,
                     **kwargs)
    return Retry(total=total,
                 backoff_factor=backoff_factor,
                 raise_on_status=raise_on_status,
                 status_forcelist=status_forcelist,
                 method_whitelist=allowed_methods,
                 **kwargs)


class TimeoutHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout = DEFAULT_TIMEOUT
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)


class RetryHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        if "max_retries" not in kwargs:
            kwargs["max_retries"] = get_retry_strategy()
        super().__init__(*args, **kwargs)


class Adapter(RetryHTTPAdapter, TimeoutHTTPAdapter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
