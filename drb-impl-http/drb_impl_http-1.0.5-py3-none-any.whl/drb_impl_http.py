import io
import re
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlparse

import requests
from drb import DrbNode
from drb.abstract_node import AbstractNode
from drb.exceptions import DrbException, DrbNotImplementationException
from drb.factory import DrbFactory
from drb.path import ParsedPath
from requests import Response
from requests.auth import AuthBase
from tenacity import retry, stop_after_attempt, stop_after_delay, wait_fixed

from drb_impl_http.execptions import DrbHttpNodeException


@retry(stop=(stop_after_delay(120) | stop_after_attempt(5)),
       wait=wait_fixed(15))
def get(path: str, auth: AuthBase, headers, params: Dict[str, str]):
    return requests.get(
        path, stream=True, auth=auth, headers=headers, params=params
    )


@retry(stop=(stop_after_delay(120) | stop_after_attempt(5)),
       wait=wait_fixed(15))
def head(path: str, auth: AuthBase, params: Dict[str, str]):
    return requests.head(
        path,
        auth=auth,
        params=params
    )


def check_response(resp: Response):
    if resp.status_code >= 300:
        raise DrbHttpNodeException(
            "ERROR: " + str(resp.status_code) +
            " reason : " + resp.reason +
            " request : " + resp.request.url
        )


def check_args(*args):
    return len(args) > 0 and isinstance(
        args[0],
        int
    ) and args[0] > 0


class Download(io.BytesIO):
    def __init__(self, path: str,
                 auth: AuthBase,
                 params: Dict[str, str],
                 headers,
                 chunk_size: int
                 ):
        self.__res = None
        self._chunk_size = chunk_size
        self._path = path
        self._auth = auth
        self._params = params
        self._headers = headers
        self._iter = None
        self._buff = bytearray(0)
        super().__init__()

    def __init_request(self):
        if self.__res is None:
            self.__res = get(
                self._path,
                self._auth,
                self._headers,
                self._params
            )
            check_response(self.__res)

    def getvalue(self) -> bytes:
        self.__init_request()
        return self.__res.content

    def __init_generator(self):
        self.__init_request()
        if self._iter is None:
            self._iter = self.__res.iter_content(self._chunk_size)

    def read(self, *args, **kwargs):
        self.__init_request()
        if not check_args(*args):
            with self.__res as resp:
                return resp.content
        self.__init_generator()
        try:
            self._buff.extend(bytearray(next(self._iter)))
            res = self._buff[0:args[0]]
            del (self._buff[0:args[0]])
            return res
        except StopIteration:
            if len(self._buff) > 0:
                if args[0] < len(self._buff):
                    res = self._buff[0:args[0]]
                    del (self._buff[0:args[0]])
                    return res
                else:
                    return self._buff
            else:
                return bytes(0)

    def close(self) -> None:
        super().close()
        self.__res.close()


class DrbHttpNode(AbstractNode):
    """
    Parameters:
        path: The url of the http or https server
        auth (AuthBase): The authentication object to get
                         the connexion (default: None)
        params (Dict[str, str]): Parameters to send with all
                                 requests (default: None)
    """

    def __init__(self, path, auth: AuthBase = None,
                 params: Dict[str, str] = None):
        super().__init__()
        self._path = path
        self._headers = None
        self._auth = auth
        self._params = params

    def __init_header(self):
        if self._headers is None:
            res = head(self._path, self._auth, self._params)
            check_response(res)
            self._headers = res.headers

    @property
    def name(self) -> str:
        key = ('Content-Disposition', None)
        if key in self.attributes.keys():
            p = re.compile('filename ?= ?"(.*)"')
            res = p.search(self.get_attribute(key[0]))
            if res is not None:
                return res.group(1)
        parsed_uri = urlparse(self._path)
        return str(parsed_uri.path).split('/')[-1]

    @property
    def children(self) -> List[DrbNode]:
        return []

    @property
    def auth(self):
        return self._auth

    @property
    def params(self):
        return self._params

    @property
    def has_child(self, name: str = None, namespace: str = None) -> bool:
        return False

    @property
    def namespace_uri(self) -> Optional[str]:
        return None

    @property
    def parent(self) -> Optional[DrbNode]:
        return None

    @property
    def value(self) -> Optional[Any]:
        return None

    @property
    def path(self) -> ParsedPath:
        return ParsedPath(self._path)

    @property
    def attributes(self) -> Dict[Tuple[str, str], Any]:
        self.__init_header()
        return {(k, None): v for k, v in self._headers.items()}

    def get_attribute(self, name: str, namespace_uri: str = None) -> Any:
        self.__init_header()
        key = (name, namespace_uri)
        if namespace_uri is None and key in self.attributes.keys():
            return self.attributes[key]
        raise DrbException(f'Attribute not found name: {name}, '
                           f'namespace: {namespace_uri}')

    def has_impl(self, impl: type) -> bool:
        return impl == io.BytesIO

    def get_impl(self, impl: type, **kwargs) -> Any:
        """
          This operation returns a reference to an object implementing a
          specific interface. This method authorizes a specific and/or direct
          API instead of using the DrbNode interface. The provided object is
          independent of this node and shall be released/closed by the caller
          when interface requires such finally operations.

          Parameters:
              impl (type): the implementation type expected

          Keyword Arguments:
              start (int): The first byte to be downloaded.
              end (int): The last byte to be downloaded.

          Return:
              Any: the expected implementation.
          Raises:
              DrbNotImplementedException: if `impl` is not supported by the
                                          current node
        """
        if self.has_impl(impl):
            headers = None
            if 'start' in kwargs:
                if 'end' in kwargs:
                    headers = {
                        "range":
                            f"bytes={kwargs.get('start')}"
                            f"-{kwargs.get('start') + kwargs.get('end')}"}
                else:
                    headers = {"range": f"bytes={kwargs.get('start')}-"}

            return Download(self.path.name,
                            self._auth,
                            self.params,
                            headers,
                            kwargs.get('chunk_size', 1)
                            )
        raise DrbNotImplementationException(
            f'no {impl} implementation found')

    def close(self) -> None:
        pass


class DrbHttpFactory(DrbFactory):

    @staticmethod
    def _create_from_uri_of_node(node: DrbNode):
        uri = node.path.name
        return DrbHttpNode(uri)

    def _create(self, node: DrbNode) -> DrbNode:
        return self._create_from_uri_of_node(node)
