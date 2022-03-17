from abc import abstractmethod
from herre.types import Token
from typing import Any, List
from abc import ABC
import logging

logger = logging.getLogger(__name__)


class BaseGrant:
    herre: Any

    @abstractmethod
    async def afetch_token(self, herre, **kwargs) -> Token:
        raise NotImplementedError("Implement afetch_token")
