from .generated.vega.api.v1 import corestate_grpc
from .grpcclient import GRPCClient


class VegaCoreStateClient(GRPCClient):
    """
    The Vega Core State Client talks to a back-end node.
    """

    def __init__(self, url: str, channel=None) -> None:
        super().__init__(url, channel=channel)
        self._corestate = corestate_grpc.CoreStateServiceStub(self.channel)

    def __getattr__(self, funcname):
        return getattr(self._corestate, funcname)
