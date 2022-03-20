from typing import Any, Dict, Type, Union

from siphon.queue.types import DataT


class ViolationStrategy:
    """
    ViolationStrategy for dealing with TypedAioQueue errors

    If you attempt to put an item on a TypedAioQueue that isn't of the type specified we will
    decide what to do based on the ViolationStrategy provided. Note: This class is not meant
    to be used directly
    """

    def checks(self, item: Any, model: Type[DataT]):
        raise NotImplementedError()

    @staticmethod
    def _is_item_of_type(item: Any, model: Type[DataT]):
        return isinstance(item, model)

    def __call__(self, item: Any, model: Type[DataT]) -> Union[Dict, Type[DataT]]:
        checked = self.checks(item, model)
        return checked


class RaiseOnViolation(ViolationStrategy):
    name: str = 'raise-error-on-violation'

    def checks(self, item: Any, model: Type[DataT]):
        if not self._is_item_of_type(item, model):
            raise TypeError(
                f'this is a TypedQueue with a strict {self.name} strategy. '
                f'Item must be of type {model.__name__} not {type(item)}'
            )
        return item


class DiscardOnViolation(ViolationStrategy):
    name: str = 'discard-error-on-violation'

    def checks(self, item: Any, model: Type[DataT]) -> None:
        if self._is_item_of_type(item, model):
            return item
        return None
