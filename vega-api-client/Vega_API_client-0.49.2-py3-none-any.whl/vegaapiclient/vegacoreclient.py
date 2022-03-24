from .generated.vega.api.v1 import core_grpc
from .grpcclient import GRPCClient


class VegaCoreClient(GRPCClient):
    """
    The Vega Core Client talks to a back-end node.
    """

    def __init__(self, url: str, channel=None) -> None:
        super().__init__(url, channel=channel)
        self._core = core_grpc.CoreServiceStub(self.channel)

    def __getattr__(self, funcname):
        return getattr(self._core, funcname)
