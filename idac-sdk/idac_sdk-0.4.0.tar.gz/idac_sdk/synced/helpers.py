from functools import wraps
import asyncio
import inspect


def sync_method(async_method):
    @wraps(async_method)
    def wrapper(self, *args, **kwargs):
        coro = async_method(self, *args, **kwargs)
        caller = inspect.stack()[1][0].f_locals.get("self", None)
        if caller and getattr(caller, "__idac_synced_obj__", False):
            return coro
        return asyncio.run(coro)

    return wrapper
