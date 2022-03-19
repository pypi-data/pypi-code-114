from typing import List

from .i_handler import IHandler
from .i_builder import IBuilder


class SimpleHandlerBuilder(IBuilder):
  """"""

  def __init__(self, handlers: List[IHandler] = []):
    """"""

    self._handlers = handlers.copy()

  def add_next(self, next: IHandler):
    """"""

    self._handlers.append(next)

    return self

  def build(self):
    """"""

    handler_count = len(self._handlers)

    if handler_count < 1:
        raise ValueError('Too few handlers added to the builder.')

    for i in range(handler_count - 1):
        self._handlers[i].set_next(self._handlers[i + 1])

    result = self._handlers[0]

    return result
