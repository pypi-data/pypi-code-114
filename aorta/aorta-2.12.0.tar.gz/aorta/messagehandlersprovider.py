"""Declares :class:`MessageHandlersProvider`."""
import collections
import typing

from .basemessage import BaseMessage
from .exceptions import UnknownMessageType
from .messagemetaclass import MessageMetaclass
from .models import MessageHeader
from .models import Message


class MessageHandlersProvider:
    """Implements a registry that can match handlers to messages."""
    __module__: str = 'aorta'
    UnknownMessageType: type = UnknownMessageType

    def __init__(self):
        self._handlers = collections.defaultdict(list)
        self._types = {}

    def match(self, message: typing.Union[MessageHeader, Message]) -> list:
        """Return the list of handler classes for the given message."""
        return self.get(message)

    def get(self, message: typing.Union[MessageHeader, Message]) -> list:
        return self._handlers[message.api_version, message.kind]

    def parse(self, data: dict) -> Message:
        """Return a concrete message type by inspecting the metadata in the
        header.
        """
        try:
            header = MessageHeader(**data)
        except ValueError:
            raise self.UnknownMessageType
        else:
            key = (header.api_version, header.kind)
            if key not in self._types:
                raise self.UnknownMessageType
            return self._types[key](**data)

    def register(self, spec: MessageMetaclass, cls: type):
        """Register handler class `cls` for the message of type
        `spec`.
        """
        key = (spec._meta.api_version, spec._meta.name)
        self._handlers[key].append(cls)
        if key not in self._types:
            self._types[key] = spec._envelope


_default: MessageHandlersProvider = MessageHandlersProvider()


def match(
    message: typing.Union[MessageHeader, Message]
) -> typing.List[type]:
    """Match a message against the registered handlers in the default
    provider.
    """
    return _default.match(message)


def parse(data: dict):
    """Parse a message using the default provider."""
    return _default.parse(data)


def register(spec: MessageHandlersProvider, cls: typing.Callable):
    """Register a message handle using the default provider."""
    return _default.register(spec, cls)
