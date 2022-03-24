from functools import lru_cache, wraps
from typing import Any, Callable, TypeVar

from typing_extensions import ParamSpec

P = ParamSpec("P")
T = TypeVar("T")


def _enforce_hashable_kwargs(function: Callable[P, T]) -> Callable[P, T]:
    """Cast list kwargs to tuples for hashable cache keys."""

    @wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> T:
        for key, value in kwargs.items():
            if isinstance(value, list):
                kwargs[key] = tuple(value)

        return function(*args, **kwargs)

    return wrapper


def cache(function: Callable[P, T]) -> Callable[P, T]:
    """Decorate function to cache return values.

    Thin wrapper around functools.lru_cache that sets a default cache size of
    1024 recent calls per function (approximately 1 MB per resource) and type
    casts unhashable kwargs.
    """
    cached_function = lru_cache(1024)(function)
    wrapper = wraps(function)(_enforce_hashable_kwargs(cached_function))

    # Preserve cache instrumentation as attributes of the wrapped function. This
    # is consistent with the interface of functools.lru_cache which gets
    # overridden when the second decorator is applied to enforce arguments are
    # hashable but will not get picked up by type checkers and IDE autocomplete.
    wrapper.cache_info = cached_function.cache_info  # type: ignore
    wrapper.cache_clear = cached_function.cache_clear  # type: ignore
    return wrapper
