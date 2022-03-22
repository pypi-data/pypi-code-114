# external imports
from chainlib.eth.connection import RPCConnection
from cic_eth_registry import CICRegistry


def extension_start(network, *args, **kwargs):
    """Called by the "export" cli tool subcommand for initialization of the eth extension.

    :param network: Network object to read and write settings from
    :type network: cic.network.Network
    """
    CICRegistry.address = kwargs.get("registry_address")
    key_account_address = kwargs.get("key_account_address")
    RPCConnection.register_location(
        kwargs.get("rpc_provider"), kwargs.get("chain_spec")
    )
    conn = RPCConnection.connect(kwargs.get("chain_spec"))

    registry = CICRegistry(kwargs.get("chain_spec"), conn)

    address_declarator = registry.by_name("AddressDeclarator")
    network.resource_set(
        "eth", "address_declarator", address_declarator, key_account=key_account_address
    )

    token_index = registry.by_name("TokenRegistry")
    network.resource_set(
        "eth", "token_index", token_index, key_account=key_account_address
    )

    network.resource_set("eth", "token", None, key_account=key_account_address)

    network.set("eth", kwargs["chain_spec"])
    network.save()
