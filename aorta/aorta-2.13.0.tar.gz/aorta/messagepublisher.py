"""Declares :class:`MessagePublisher`."""
import typing

from .command import Command
from .event import Event
from .sender import Sender


class MessagePublisher(Sender):
    """Provides an interface to published event messages."""
    __module__: str = 'aorta'

    async def publish(self,
        objects: typing.Union[Command, Event, list],
        correlation_id: str = None
    ):
        """Publish an message to the upstream peer."""
        if not isinstance(objects, list):
            objects = [objects]
        return await self.send([x.as_message(correlation_id) for x in objects])
