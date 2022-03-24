import datetime as dt
import typing as tp
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from urllib.request import Request

from ..doi import DOI


class UpdateType(Enum):
    RETRACTION = "RETRACTION"
    CONCERN = "CONCERN"
    UPDATE = "UPDATE"


@dataclass
class Update:
    original_doi: DOI
    type: UpdateType
    timestamp: tp.Optional[dt.datetime] = None
    update_doi: tp.Optional[DOI] = None


class Backend(ABC):
    @abstractmethod
    def make_request(self, doi: DOI) -> Request:
        pass

    @abstractmethod
    def parse_content(self, content: bytes) -> tp.Optional[Update]:
        pass
