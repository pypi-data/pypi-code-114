import sys as sys
import builtins as _builtins
from typing import Type, TypeVar, Callable
from arraydebug.array_like import array_like_info

T = TypeVar("T")


def register_repr(cls: Type[T], info_fn: Callable[[T], str]) -> None:
    repr_fn_table[cls] = info_fn


def register_reprs() -> None:
    # if torch is already loaded
    if "torch" in sys.modules:
        from arraydebug.torch import tensor_info

        torch = sys.modules["torch"]
        register_repr(torch.Tensor, tensor_info)

    # if numpy is already loaded
    if "numpy" in sys.modules:
        from arraydebug.numpy import ndarray_info

        np = sys.modules["numpy"]
        register_repr(np.ndarray, ndarray_info)


_default_repr = _builtins.repr


def _new_repr(obj) -> str:
    if type(obj) in repr_fn_table:
        return repr_fn_table[type(obj)](obj)
    elif not isinstance(obj, type) and "__array__" in dir(obj):
        return array_like_info(obj)
    else:
        return _default_repr(obj)


def recover_repr() -> None:
    _builtins.repr = _default_repr


def inject_repr() -> None:
    _builtins.repr = _new_repr


repr_fn_table = {}
