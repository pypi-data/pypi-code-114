from abc import ABC, abstractmethod
from syncari.models.request import Request
from ..logger import SyncariLogger

# pylint: disable=missing-function-docstring
class Synapse(ABC):
    """
        The abstract synapse class to enforce synapse implementations
    """

    def __init__(self, request: Request) -> None:
        self.request = Request.parse_raw(request)

    @property
    def name(self) -> str:
        """
            Synapse name.
        """
        return self.__class__.__name__

    def print(self, funcname, request):
        self.logger.info(funcname)
        self.logger.info(request)
        print()

    @property
    def logger(self):
        return SyncariLogger.get_logger(f"{self.name}")

    @abstractmethod
    def synapse_info(self):
        pass

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def refresh_token(self):
        pass

    @abstractmethod
    def get_access_token(self):
        pass

    @abstractmethod
    def describe(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def extract_webhook_identifier(self):
        pass

    @abstractmethod
    def process_webhook(self):
        pass
