from abc import abstractmethod
from .i_handler import IHandler


class MultiHandler(IHandler):
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
  def _on_handle(self, request) -> bool:
    """"""

  @abstractmethod
  def _on_cannot_handle(self, request) -> bool:
    """"""
  
  def handle(self, request):
    """"""

    if self._can_handle(request):
      if not self._on_handle(request):
        self._next.handle(request)
    elif not self._on_cannot_handle(request):
      self._next.handle(request)
