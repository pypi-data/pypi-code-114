import typing
from threading import Lock, Thread, Condition

import websocket
import json
from functools import reduce

from dataclasses import dataclass

from .interceptors.retry_response import RetryResponseInterceptor


class FailedToConnect(Exception):
    pass


@dataclass
class RequestData:
    jsonrpc: str
    id: int
    method: str
    handle: int
    params: typing.List[any]


RequestInterceptor = typing.Callable[[RequestData], RequestData]
ResponseInterceptor = typing.Callable[[dict], dict]


class RpcClient:
    """
    RpcClient represents an WS RPC client, tailored to the
    QIX Associative Engine's RPC API specifically.

    It is safe to use the client.send from multiple threads.
    """

    def __init__(
        self,
        url: str,
        header: typing.List[str] = None,
        request_interceptors: typing.List[RequestInterceptor] = None,
        response_interceptors: typing.List[ResponseInterceptor] = None,
    ):
        self._socket = None
        self._id = -1
        self._received = None
        self._recv_error = None

        if header is None:
            header = []
        self._response_interceptors = [RetryResponseInterceptor(self).intercept]
        if response_interceptors:
            self._response_interceptors.extend(response_interceptors)
        self._request_interceptors = []
        if request_interceptors:
            self._request_interceptors.extend(request_interceptors)
        self.lock = Lock()
        if not url:
            raise Exception("Empty url")
        self.connect(url, header)

    def _watch_recv(self):
        """
        _watch_recv watches for socket responses.
        Adds the response to _received.
        """

        while True:
            if not self.is_connected():
                return
            try:
                res = self._socket.recv()
            except Exception as err:
                self._socket = None
                res = False
                self._recv_error = err
            with self._received_added:
                if res:
                    res = json.loads(res)
                    # add response to _received and notify waiting
                    if "id" in res:
                        self._received[res["id"]] = res
                        self._received_added.notify_all()
                else:
                    # notify waiting receivers so that
                    # the not connected error can be raised
                    # if the error is raised from here then the
                    # wait_response will never finish
                    self._received_added.notify_all()

    def connect(self, url: str, headers: typing.List[str] = None):
        """
        connect establishes a connection to provided url
        using the specified headers.

        If the client is already connected an exception will
        be raised.

        Parameters
        ----------
        url: string the websocket url
        headers: list[str] headers
        """
        if headers is None:
            headers = []

        if self.is_connected():
            raise Exception("Client already connected")
        socket = websocket.WebSocket()
        try:
            socket.connect(url, header=headers, suppress_origin=True)
        except Exception as exc:
            raise FailedToConnect() from exc

        self._socket = socket
        self._received = {}
        self._id = -1
        self._received_added = Condition()

        self._watch_recv_thread = Thread(target=self._watch_recv)
        self._watch_recv_thread.start()

    def is_connected(self):
        """
        return connected state
        """

        return self._socket and self._socket.connected

    def close(self):
        """
        close closes the socket (if it's open).
        """

        if self.is_connected():
            self._socket.send_close()
        if self._watch_recv_thread.is_alive():
            self._watch_recv_thread.join()

    def __enter__(self):
        """
        __enter__ is called when client is used in a 'with' statement.
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        __exit__ is called when the 'with' scope is exited. This will call
        the client's close method.
        """

        self.close()

    def send(self, method: str, handle: int, *params):
        """
        send is a thread-safe method that sends a websocket-message with the
        specified method, handle and parameters.
        The resulting response is returned.

        If the client isn't connected an exception is raised.

        Parameters
        ----------
        method: string engine method name for the request
        handle: int the associated handle
        params: Any data to be sent
        """

        if not self.is_connected():
            raise Exception("Client not connected")

        self.lock.acquire()
        self._id += 1
        id_ = self._id
        self.lock.release()

        encoded_params = []
        for param in params:
            encoded_params.append(param)

        data = {
            "jsonrpc": "2.0",
            "id": self._id,
            "method": method,
            "handle": handle,
            "params": encoded_params,
        }
        # send and wait respons
        data = reduce(lambda d, f: f(d), self._request_interceptors, data)
        json_data = json.dumps(data)
        self._socket.send(json_data)
        res = self._wait_response(id_)
        res["request_data"] = data
        res = reduce(lambda r, f: f(r), self._response_interceptors, res)
        return_value = None
        if "result" in res:
            return_value = res["result"]
        elif "error" in res:
            raise Exception(res["error"]["message"])
        else:
            return_value = res
        return return_value

    def _wait_response(self, id_):
        """
        _wait_response waits (blocking) for a message with the specified id.
        Internal method that should only be called from send
        """

        with self._received_added:
            while id_ not in self._received:
                if not self.is_connected():
                    if self._recv_error:
                        raise self._recv_error
                    else:
                        raise Exception("not connected")
                self._received_added.wait()
            res = self._received[id_]
            del self._received[id_]
            return res
