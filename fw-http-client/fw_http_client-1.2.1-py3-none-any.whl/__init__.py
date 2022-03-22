"""Prod-ready HTTP client with timeout and retries by default."""
import functools

try:
    from importlib.metadata import version
except ImportError:  # pragma: no cover
    from importlib_metadata import version  # type: ignore

from pydantic.json import pydantic_encoder
from requests.compat import json  # type: ignore

# pylint: disable=redefined-builtin
from requests.exceptions import InvalidJSONError  # type: ignore
from requests.exceptions import ConnectionError, HTTPError, RequestException

from . import errors
from .client import HttpClient, dump_useragent, load_useragent
from .config import AnyAuth, HttpConfig
from .errors import ClientError, ServerError

__version__ = version(__name__)
__all__ = [
    "AnyAuth",
    "HttpClient",
    "HttpConfig",
    "dump_useragent",
    "load_useragent",
    "errors",
    "ConnectionError",
    "ClientError",
    "RequestException",
    "ServerError",
]

# patch the exceptions for more useful default error messages
RequestException.__getattr__ = errors.request_exception_getattr  # type: ignore
RequestException.__str__ = errors.request_exception_str  # type: ignore
ConnectionError.__str__ = errors.connection_error_str  # type: ignore
HTTPError.__str__ = errors.http_error_str  # type: ignore
InvalidJSONError.__str__ = errors.json_error_str  # type: ignore

# path json.dumps to use the same encoder as pydantic
json.dumps = functools.partial(json.dumps, default=pydantic_encoder)
