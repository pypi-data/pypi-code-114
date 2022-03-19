from abc import ABC, abstractmethod
from typing import Tuple


class IMiddlewareHandler(ABC):
  """"""

  def __init__(self, next=None):
    self._next = next

  @property
  def next(self):
    return self._next

  def set_next(self, value):
    """"""

    self._next = value

    # enable daisy chaining
    return self._next

  @abstractmethod
  def _can_handle(self, request, response) -> bool:
    """"""

  @abstractmethod
  def _on_handle(self, request, response) -> Tuple[any, any]:
    """"""

  @abstractmethod
  def _on_cannot_handle(self, request, response):
    """"""
  
  def handle(self, request, response):
    """"""

    if self._can_handle(request, response):
      result = self._on_handle(request, response)
      if self._next:
        return self._next.handle(*result)
      return result
    return self._on_cannot_handle(request, response)
