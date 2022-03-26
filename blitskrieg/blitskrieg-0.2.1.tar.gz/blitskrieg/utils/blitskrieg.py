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
"""Blitskrieg utils module."""

from datetime import datetime
from glob import glob
from logging import getLogger
from os import path, remove
from shutil import rmtree
from subprocess import CalledProcessError, check_output
from time import sleep

from boltlight_proto import boltlight_pb2 as lpb
from grpc import RpcError, StatusCode

from .. import __version__
from .. import blitskrieg_pb2 as pb
from .. import settings as sett
from .bitcoin import gen_blocks, get_block_count
from .common import connect
from .configure_stack import (
    create_boltlight_configs, create_compose_file, init_nodes, init_nodes_env)

LOGGER = getLogger(__name__)


def channel_info(ses, request):
    """Collect information about channels."""
    all_channels = (request.channel_ids == [])
    channels = {}
    response = pb.ChannelInfoResponse()
    for node in sett.CURRENT_BOLTLIGHT_NODES:
        with connect('LightningStub', sett.BL_ADDR.format(node), ses) as stub:
            res = stub.ListChannels(lpb.ListChannelsRequest())
        node_chans = {c.channel_id: c for c in res.channels}
        for chan_id, channel in node_chans.items():
            if not (all_channels or chan_id in request.channel_ids):
                continue
            if chan_id in channels:
                channels[chan_id].peer2_id = node
                response.channels.append(channels[chan_id])
            else:
                channel = node_chans[chan_id]
                channels[chan_id] = pb.Channel(
                    channel_id=chan_id,
                    peer1_id=node,
                    total_capacity_sat=channel.capacity_msat // 1000,
                    peer1_balance_msat=channel.local_balance_msat,
                    peer2_balance_msat=channel.remote_balance_msat)
    return response


def create_stack(ses, request):
    """Create a docker stack with the requested LN nodes."""
    if sett.STACK_CREATING:
        ses.context.abort(StatusCode.CANCELLED,
                          'CreateStack already in progress')
    if sett.STACK_REMOVING:
        ses.context.abort(StatusCode.CANCELLED, 'RemoveStack in progress')
    try:
        sett.STACK_CREATING = 1
        _get_stack_down(ses)
        nodes = {
            field.name.upper(): value
            for field, value in request.ListFields()
        }
        create_compose_file(nodes)
        check_output(sett.COMPOSE_BASE_CMD + 'up --no-start'.split())
        check_output(sett.COMPOSE_BASE_CMD + 'up -d bitcoind'.split())
        # mine a block before turning on eclair to avoid
        # 'bitcoind should be synchronized' error
        gen_blocks(ses, load=True)
        if 'ELECTRUM' in nodes and nodes['ELECTRUM'] > 0:
            check_output(sett.COMPOSE_BASE_CMD + 'up -d electrs'.split())
            start = datetime.now()
            ready = False
            while (datetime.now() - start).seconds <= 10:
                try:
                    check_output('curl -fSs electrs:24224'.split())
                    ready = True
                    break
                except CalledProcessError:
                    sleep(1)
            if not ready:
                _create_stack_error(ses.context, 'electrs is unavailable')
        create_boltlight_configs(nodes)
        init_nodes_env(ses, nodes)
        check_output(sett.COMPOSE_BASE_CMD + 'up -d'.split())
        init_nodes(nodes)
        LOGGER.info('Unlocking boltlight nodes...')
        for node in sett.CURRENT_BOLTLIGHT_NODES:
            _unlock_boltlight_node(ses, node)
        LOGGER.info('Unlocking underlying nodes...')
        for node in sett.CURRENT_BOLTLIGHT_NODES:
            _unlock_underlying_node(ses, node)
        LOGGER.info('Testing connection to boltlight nodes...')
        for node in sett.CURRENT_BOLTLIGHT_NODES:
            _test_node_connection(ses, node)
        sett.STACK_RUNNING = 1
    except (CalledProcessError, RuntimeError) as err:
        _create_stack_error(ses.context, err)
    finally:
        sett.STACK_CREATING = 0
    return pb.CreateStackResponse()


def get_info():
    """Get BLITSkrieg info."""
    return pb.GetInfoResponse(version=__version__)


def node_info(ses, request):
    """Collect information about nodes."""
    response = pb.NodeInfoResponse()
    requested_nodes = request.node_ids or sett.CURRENT_BOLTLIGHT_NODES
    for node in requested_nodes:
        node_res = pb.Node(id=node, implementation=node.split('_')[1])
        with connect('LightningStub', sett.BL_ADDR.format(node), ses) as stub:
            req = lpb.GetNodeInfoRequest()
            res = stub.GetNodeInfo(req)
            host = node.replace("boltlight_", "krieg_") + "_1"
            if res.node_uri:
                node_res.node_uri = res.node_uri.replace('0.0.0.0', host)
            else:
                node_res.node_uri = f"{res.identity_pubkey}@{host}:9735"
            res = stub.BalanceOnChain(lpb.BalanceOnChainRequest())
            node_res.onchain_balance_sat = res.confirmed_sat
            res = stub.BalanceOffChain(lpb.BalanceOffChainRequest())
            node_res.offchain_balance_msat = res.out_tot_msat
            res = stub.ListChannels(lpb.ListChannelsRequest())
            for channel in res.channels:
                node_res.channel_ids.append(channel.channel_id)
        response.nodes.append(node_res)
    return response


def remove_stack(ses, _request):
    """Remove any existing docker stack."""
    if sett.STACK_REMOVING:
        ses.context.abort(StatusCode.CANCELLED,
                          'RemoveStack already in progress')
    if sett.STACK_CREATING:
        ses.context.abort(StatusCode.CANCELLED, 'CreateStack in progress')
    try:
        sett.STACK_REMOVING = 1
        _get_stack_down(ses)
        sett.STACK_RUNNING = 0
    finally:
        sett.STACK_REMOVING = 0
    return pb.RemoveStackResponse()


def stack_info(ses, _request):
    """Collect information about the running stack."""
    response = pb.StackInfoResponse()
    capacity_msat = 0
    channel_ids = set()
    for node in sett.CURRENT_BOLTLIGHT_NODES:
        response.node_ids.append(node)
        with connect('LightningStub', sett.BL_ADDR.format(node), ses) as stub:
            res = stub.BalanceOffChain(lpb.BalanceOffChainRequest())
            capacity_msat += res.out_tot_msat
            res = stub.ListChannels(lpb.ListChannelsRequest())
            channel_ids.update([c.channel_id for c in res.channels])
    response.channel_count = len(channel_ids)
    if capacity_msat % 1000 != 0:
        raise ValueError("capacity should be an even sat number")
    response.total_ln_capacity_sat = capacity_msat // 1000
    response.block_height = get_block_count(ses)
    return response


def _create_stack_error(context, error=None):
    """Terminate RPC call with a create stack error."""
    err_msg = 'Error creating stack'
    if error:
        err_msg += f': {error}'
    context.abort(StatusCode.CANCELLED, err_msg)


def _get_stack_down(ses):
    """If a compose file exists, try to get docker stack down."""
    try:
        if path.exists(sett.COMPOSE_FILE):
            check_output(sett.COMPOSE_BASE_CMD +
                         ' down -v --remove-orphans'.split())
            sett.CURRENT_BOLTLIGHT_NODES = []
            for data in glob(path.join(sett.BOLTLIGHT_DATA, "*")):
                try:
                    rmtree(data)
                except NotADirectoryError:
                    remove(data)
    except CalledProcessError:
        ses.context.abort(StatusCode.CANCELLED, 'Error removing stack')


def _test_node_connection(ses, node):
    """Test node connection.

    Call the GetInfo API, to check whether the node is ready to answer to
    successive calls.
    """
    msg = f'testing connection to {node}'
    LOGGER.debug('%s...', msg.capitalize())
    req = lpb.GetNodeInfoRequest()
    attempts = 10
    with connect('LightningStub', sett.BL_ADDR.format(node), ses) as stub:
        while attempts:
            try:
                stub.GetNodeInfo(req)
                LOGGER.debug('Connected to %s', node)
                return
            except RpcError as err:
                attempts -= 1
                # pylint: disable=no-member
                LOGGER.debug('Error %s (%s), %s attempts left', msg,
                             err.details(), attempts)
                # pylint: enable=no-member
                sleep(3)
        raise RuntimeError(f'Failed {msg}')


def _unlock_boltlight_node(ses, node):
    """Call the Unlock API on the given boltlight's instance."""
    msg = f'unlocking {node}'
    LOGGER.debug('%s...', msg.capitalize())
    req = lpb.UnlockRequest(password=sett.PASSWORD)
    attempts = 5
    with connect('UnlockerStub', sett.BL_ADDR.format(node), ses) as stub:
        while attempts:
            try:
                stub.Unlock(req)  # pylint: disable=no-member
                LOGGER.debug('Unlocked %s', node)
                return
            except RpcError as err:
                attempts -= 1
                # pylint: disable=no-member
                LOGGER.debug('Error %s (%s), %s attempts left', msg,
                             err.details(), attempts)
                # pylint: enable=no-member
                sleep(.3)
        raise RuntimeError(f'Failed {msg}')


def _unlock_underlying_node(ses, node):
    """Call the UnlockNode API on each boltlight's instance."""
    msg = f'unlocking {node} underlying implementation'
    LOGGER.debug('%s...', msg.capitalize())
    req = lpb.UnlockNodeRequest(password=sett.PASSWORD)
    attempts = 10
    with connect('LightningStub', sett.BL_ADDR.format(node), ses) as stub:
        while attempts:
            try:
                stub.UnlockNode(req)
                LOGGER.debug('Unlocked %s underlying implementation', node)
                return
            except RpcError as err:
                # pylint: disable=no-member
                if err.code() == StatusCode.UNIMPLEMENTED and \
                        'not supported for this implementation' in \
                        err.details():
                    return
                attempts -= 1
                LOGGER.debug('Error %s (%s), %s attempts left', msg,
                             err.details(), attempts)
                # pylint: enable=no-member
                sleep(.5)
        raise RuntimeError(f'Failed {msg}')
