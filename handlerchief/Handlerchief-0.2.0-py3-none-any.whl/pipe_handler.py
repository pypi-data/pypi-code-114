from abc import abstractmethod
from .i_handler import IHandler


class PipeHandler(IHandler):
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
  def _can_handle(self, request) -> bool:
    """"""

  @abstractmethod
  def _on_handle(self, request):
    """"""

  @abstractmethod
  def _on_cannot_handle(self, request):
    """"""
  
  def handle(self, request):
    """"""

    if self._can_handle(request):
      if self._next:
        return self._on_handle(self._next.handle(request))
      return self._on_handle(request)
    return self._on_cannot_handle(request)
