import asyncio


def rearfloor(f):
    from functools import wraps

    @wraps(f)
    def wrapped(*args, **kwargs):
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        if callable(f):
            return loop.run_in_executor(None, f, *args, **kwargs)
        else:
            raise TypeError("Task must be a callable function or class method.")
    return wrapped
