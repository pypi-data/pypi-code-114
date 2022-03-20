from abc import ABC, abstractmethod
import typing

if typing.TYPE_CHECKING:
    from pydantic.typing import CallableGenerator

class BaseField(type, ABC):

    @abstractmethod
    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        """
        Yield a series of functions that return the value if
        it passes validation, otherwise raises an error

        eg.::

            def float_validator(v: typing.Any) -> float:
                if isinstance(v, float):
                    return v
                else:
                    raise ValueError('not a float!')

            def __get_validators__(cls):
                yield float_validator

        """