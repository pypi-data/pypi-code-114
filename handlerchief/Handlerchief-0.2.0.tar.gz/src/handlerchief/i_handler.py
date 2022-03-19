from abc import ABC, abstractmethod


class IHandler(ABC):
  """"""

  @abstractmethod
  def set_next(self, value):
    """"""

  @abstractmethod
  def _can_handle(self, request) -> bool:
    """"""

  @abstractmethod
  def _on_handle(self, request):
    """"""
  
  @abstractmethod
  def _on_cannot_handle(self, request):
    """"""
  
  @abstractmethod
  def handle(self, request):
    """"""
