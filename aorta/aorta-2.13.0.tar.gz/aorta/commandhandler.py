"""Declares :class:`CommandHandler`."""
from .command import Command
from .commandhandlermetaclass import CommandHandlerMetaclass
from .messagehandler import MessageHandler


class CommandHandler(MessageHandler, metaclass=CommandHandlerMetaclass):
    """Handles command messages."""
    __abstract__: bool = True
    __module__: str = 'aorta'
