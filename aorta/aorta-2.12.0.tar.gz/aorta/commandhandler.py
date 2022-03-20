"""Declares :class:`CommandHandler`."""
from .command import Command
from .messagehandler import MessageHandler


class CommandHandler(MessageHandler):
    """Handles command messages."""
    __module__: str = 'aorta'
