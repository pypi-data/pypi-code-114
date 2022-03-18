from contextlib import contextmanager
import socket
import threading

from paramiko import DSSKey, RSAKey, ServerInterface, Transport
from paramiko import AUTH_FAILED, AUTH_SUCCESSFUL
from paramiko import OPEN_SUCCEEDED, OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED


LONG_BANNER = """\
Welcome to the super-fun-land BBS, where our MOTD is the primary thing we
provide. All rights reserved. Offer void in Tennessee. Stunt drivers were
used. Do not attempt at home. Some restrictions apply.

Happy birthday to Commie the cat!

Note: An SSH banner may eventually appear.

Maybe.
"""


class NullServer(ServerInterface):
    paranoid_did_password = False
    paranoid_did_public_key = False
    paranoid_key = DSSKey.from_private_key_file("tests/test_dss.key")

    def __init__(self, allowed_keys=None):
        self.allowed_keys = allowed_keys if allowed_keys is not None else []

    def get_allowed_auths(self, username):
        if username == "slowdive":
            return "publickey,password"
        return "publickey"

    def check_auth_password(self, username, password):
        if (username == "slowdive") and (password == "pygmalion"):
            return AUTH_SUCCESSFUL
        return AUTH_FAILED

    def check_auth_publickey(self, username, key):
        if key in self.allowed_keys:
            return AUTH_SUCCESSFUL
        return AUTH_FAILED

    def check_channel_request(self, kind, chanid):
        if kind == "bogus":
            return OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
        return OPEN_SUCCEEDED

    def check_channel_exec_request(self, channel, command):
        if command != b"yes":
            return False
        return True

    def check_channel_shell_request(self, channel):
        return True

    def check_global_request(self, kind, msg):
        self._global_request = kind
        # NOTE: for w/e reason, older impl of this returned False always, even
        # tho that's only supposed to occur if the request cannot be served.
        # For now, leaving that the default unless test supplies specific
        # 'acceptable' request kind
        return kind == "acceptable"

    def check_channel_x11_request(
        self,
        channel,
        single_connection,
        auth_protocol,
        auth_cookie,
        screen_number,
    ):
        self._x11_single_connection = single_connection
        self._x11_auth_protocol = auth_protocol
        self._x11_auth_cookie = auth_cookie
        self._x11_screen_number = screen_number
        return True

    def check_port_forward_request(self, addr, port):
        self._listen = socket.socket()
        self._listen.bind(("127.0.0.1", 0))
        self._listen.listen(1)
        return self._listen.getsockname()[1]

    def cancel_port_forward_request(self, addr, port):
        self._listen.close()
        self._listen = None

    def check_channel_direct_tcpip_request(self, chanid, origin, destination):
        self._tcpip_dest = destination
        return OPEN_SUCCEEDED


@contextmanager
def server(
    hostkey=None,
    init=None,
    server_init=None,
    client_init=None,
    connect=None,
    pubkeys=None,
    catch_error=False,
):
    """
    SSH server contextmanager for testing.

    :param hostkey:
        Host key to use for the server; if None, loads
        ``test_rsa.key``.
    :param init:
        Default `Transport` constructor kwargs to use for both sides.
    :param server_init:
        Extends and/or overrides ``init`` for server transport only.
    :param client_init:
        Extends and/or overrides ``init`` for client transport only.
    :param connect:
        Kwargs to use for ``connect()`` on the client.
    :param pubkeys:
        List of public keys for auth.
    :param catch_error:
        Whether to capture connection errors & yield from contextmanager.
        Necessary for connection_time exception testing.
    """
    if init is None:
        init = {}
    if server_init is None:
        server_init = {}
    socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socks.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socks.bind(("", 2223))
    socks.listen()
    client, addr = socks.accept()
    ts = Transport(client, **dict(init, **server_init))

    if hostkey is None:
        hostkey = RSAKey.from_private_key_file("tests/test_rsa.key")
    ts.add_server_key(hostkey)
    event = threading.Event()
    server = NullServer(allowed_keys=pubkeys)
    ts.start_server(event, server)

    yield ts
    chan = ts.accept()
    if not chan:
        return
    event.wait()
    chan.send("\r\n\r\nWelcome to my dorky little BBS!\r\n\r\n")
    chan.close()

    ts.close()
    client.close()


_disable_sha2 = dict(
    disabled_algorithms=dict(keys=["rsa-sha2-256", "rsa-sha2-512"])
)
_disable_sha1 = dict(disabled_algorithms=dict(keys=["ssh-rsa"]))
_disable_sha2_pubkey = dict(
    disabled_algorithms=dict(pubkeys=["rsa-sha2-256", "rsa-sha2-512"])
)
_disable_sha1_pubkey = dict(disabled_algorithms=dict(pubkeys=["ssh-rsa"]))

import logging

logging.basicConfig(level=logging.DEBUG)
privkey = RSAKey.from_private_key_file("tests/test_rsa.key")


with server(
    pubkeys=[privkey],
    server_init=dict(server_sig_algs=True),
    init=dict(disabled_algorithms=dict(pubkeys=["rsa-sha2-512"])),
) as ts:
    pass
