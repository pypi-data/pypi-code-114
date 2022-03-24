import os

import pytest
import vegaapiclient as vac


@pytest.fixture(scope="module")
def corenode_core():
    """
    Provide a `VegaCoreClient`, connected to `$CORE_GRPC_NODE`.
    """
    grpc_node = os.getenv("CORE_GRPC_NODE")
    assert grpc_node is not None and grpc_node != ""
    return vac.VegaCoreClient(grpc_node)


@pytest.fixture(scope="module")
def corenode_corestate():
    """
    Provide a `VegaCoreStateClient`, connected to `$CORE_GRPC_NODE`.
    """
    grpc_node = os.getenv("CORE_GRPC_NODE")
    assert grpc_node is not None and grpc_node != ""
    return vac.VegaCoreStateClient(grpc_node)
