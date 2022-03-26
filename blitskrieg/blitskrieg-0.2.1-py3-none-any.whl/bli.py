# BLITSkrieg - a Bitcoin Lightning Integration Test Service
#
# Copyright (C) 2022 hashbeam contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# For a full list of contributors, please see the AUTHORS.md file.
"""Implementation of a CLI (Command Line Interface) to command BLITSkrieg.

- Exits with code 0 if everything is OK
- Exits with code 1 when a general client-side error occurs
- Exits with code 64 + <gRPC status code> when a gRPC error is raised by server
(https://github.com/grpc/grpc/blob/master/doc/statuscodes.md)
"""

from configparser import Error as ConfigError
from functools import wraps
from json import dumps
from os import getcwd, path

from click import argument, echo, group, option, pass_context, version_option
from google.protobuf.json_format import MessageToJson
from grpc import RpcError

from blitskrieg.utils.common import check_port

from . import __version__
from . import blitskrieg_pb2 as pb
from . import blitskrieg_pb2_grpc as pb_grpc
from . import settings as sett
from .utils.common import (
    connect, die, get_config_parser, get_path, set_defaults)


def _check_rpcserver_addr():
    """Check the RPC server address, adding port if missing."""
    if not sett.CLI_RPCSERVER:
        die('Invalid RPC server address')
    rpcserver = sett.CLI_RPCSERVER.split(':', 1)
    if len(rpcserver) > 1:
        port = rpcserver[1]
        check_port(port)
    else:
        sett.CLI_RPCSERVER = sett.CLI_RPCSERVER + ':' + sett.PORT


def _get_cli_options():
    """Set CLI options."""
    config = get_config_parser()
    if config:
        set_defaults(config, sett.CONFIG_CLI_OPTS)
        sec = 'bli'
        sett.CLI_RPCSERVER = config.get(sec, 'RPCSERVER')
        _check_rpcserver_addr()


def _handle_call(func):
    """Decorator to handle a gRPC call to BLITSkrieg."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        """Get start options and run wrapped function."""
        try:
            _get_cli_options()
            stub_name, api, req = func(*args, **kwargs)
            with connect(stub_name,
                         sett.CLI_RPCSERVER,
                         grpc_proto=pb_grpc,
                         timeout=sett.RPC_CONN_TIMEOUT) as stub:
                res = getattr(stub, api)(req)
            _print_res(res)
        except RpcError as err:
            # pylint: disable=no-member
            json_err = {'code': err.code().name, 'details': err.details()}
            error = dumps(json_err, indent=4, sort_keys=True)
            die(error, sett.CLI_BASE_GRPC_CODE + err.code().value[0])
            # pylint: enable=no-member
        except ConfigError as err:
            die(f'Configuration error: {err}')
        except Exception as err:  # pylint: disable=broad-except
            die(f'Error, terminating cli: {err}')

    return wrapper


def _print_res(response):
    """Print response using JSON format."""
    echo(
        MessageToJson(response,
                      including_default_value_fields=True,
                      preserving_proto_field_name=True,
                      sort_keys=True))


@group()
@option('--config',
        nargs=1,
        help='Path to bli configuration file (default ./config)')
@option('--rpcserver',
        nargs=1,
        help='Set host[:port] of BLITSkrieg gRPC server')
@version_option(version=__version__, message='%(version)s')
@pass_context
def entrypoint(_ctx, config, rpcserver):
    """Bli, a CLI for BLITSkrieg.

    Paths are relative to the working directory.
    """
    sett.CONFIG = 'config'
    if config is not None:
        if not config:
            die('Invalid configuration file')
        config_path = get_path(config, base_path=getcwd())
        if not path.exists(config_path):
            die(f'Could not locate config file "{config_path}"')
        sett.CONFIG = config_path
    if rpcserver is not None:
        sett.CLI_RPCSERVER = rpcserver
        _check_rpcserver_addr()


@entrypoint.command()
@option('--channel_id',
        '-c',
        multiple=True,
        help='Channel to get info about, can be used mutliple times')
@_handle_call
def channelinfo(channel_id):
    """Returns generic information about channels in the running stack."""
    req = pb.ChannelInfoRequest()
    if channel_id is not None:
        req.channel_ids.extend(channel_id)
    return 'BlitskriegStub', 'ChannelInfo', req


@entrypoint.command()
@option('--clightning', nargs=1, type=int)
@option('--eclair', nargs=1, type=int)
@option('--electrum', nargs=1, type=int)
@option('--lnd', nargs=1, type=int)
@_handle_call
def createstack(clightning, eclair, electrum, lnd):  # pylint: disable=unused-argument
    """Create a docker stack with the requested LN nodes."""
    req = pb.CreateStackRequest(**locals())
    return 'BlitskriegStub', 'CreateStack', req


@entrypoint.command()
@_handle_call
def getinfo():
    """Get BLITSkrieg info."""
    req = pb.GetInfoRequest()
    return 'BlitskriegStub', 'GetInfo', req


@entrypoint.command()
@option('--node_id',
        '-n',
        multiple=True,
        help='Channel to get info about, can be used mutliple times')
@_handle_call
def nodeinfo(node_id):
    """Returns generic information about nodes in the running stack."""
    req = pb.NodeInfoRequest()
    if node_id is not None:
        req.node_ids.extend(node_id)
    return 'BlitskriegStub', 'NodeInfo', req


@entrypoint.command()
@_handle_call
def removestack():
    """Remove any existing docker stack."""
    req = pb.RemoveStackRequest()
    return 'BlitskriegStub', 'RemoveStack', req


@entrypoint.command()
@_handle_call
def stackinfo():
    """Returns generic information about the running stack."""
    req = pb.StackInfoRequest()
    return 'BlitskriegStub', 'StackInfo', req


@entrypoint.command()
@argument('blocks', nargs=1, default=0, type=int)
@option('--address', nargs=1, help='Bitcoin mining address')
@_handle_call
def mine(blocks, address):
    """Mine the requested number of blocks, optionally sending the mining
    reward to a specific address.
    """
    request = pb.MineBlockRequest(blocks=blocks, address=address)
    return 'BitcoinStub', 'MineBlock', request


@entrypoint.command()
@argument('blocks', nargs=1, type=int)
@argument('transactions', nargs=1, type=int)
@option('--n_inputs',
        nargs=1,
        type=int,
        help='number of inputs of each transaction (default 1, max 3)')
@option('--n_outputs',
        nargs=1,
        type=int,
        help='number of outputs of each transaction (default 1, max 3)')
@_handle_call
def gentransactions(blocks, transactions, n_inputs, n_outputs):
    """Generate the requested number of blocks, each containing the requested
    number of transactions with the specified number of inputs and outputs.
    """
    request = pb.GenTransactionsRequest(blocks=blocks,
                                        transactions=transactions,
                                        n_inputs=n_inputs,
                                        n_outputs=n_outputs)
    return 'BitcoinStub', 'GenTransactions', request


@entrypoint.command()
@_handle_call
def getaddress():
    """Get a bitcoin address."""
    request = pb.GetAddressRequest()
    return 'BitcoinStub', 'GetAddress', request


@entrypoint.command()
@argument('address', nargs=1)
@argument('amount', nargs=1, type=float)
@option('--confirmations', nargs=1, type=int)
@_handle_call
def send(address, amount, confirmations):
    """Send the requested amount of BTC to the requested address."""
    request = pb.SendRequest(address=address,
                             amount=amount,
                             confirmations=confirmations)
    return 'BitcoinStub', 'Send', request


@entrypoint.command()
@_handle_call
def fundnodes():
    """Send BTC to all LN nodes."""
    req = pb.FundNodesRequest()
    return 'LightningStub', 'FundNodes', req
