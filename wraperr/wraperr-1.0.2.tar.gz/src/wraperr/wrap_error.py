import functools
from typing import Any, Callable, Type


def wrap_error(
    error_handler: Callable[[BaseException], Any],
    exception_type: Type[BaseException] = Exception
):
    def f(wrappee: Callable):
        @functools.wraps(wrappee)
        def g(*args, **kwargs):
            try:
                return wrappee(*args, **kwargs)
            except exception_type as e:
                return error_handler(e)
        return g
    return f
