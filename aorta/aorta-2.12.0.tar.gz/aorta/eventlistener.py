"""Declares :class:`EventListener`."""
from .event import Event
from .messagehandler import MessageHandler


class EventListener(MessageHandler):
    """Handles event messages."""
    __module__: str = 'aorta'
