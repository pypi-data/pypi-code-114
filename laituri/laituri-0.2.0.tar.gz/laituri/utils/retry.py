import random
import time
from functools import wraps


def retry(*, tries: int = 5, max_delay: float = 32):
    """
    Decorator that retries the wrapped function if any exception occurs.
    """

    def inner_retry(func):
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            attempt = 1
            while attempt < tries:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    delay = (2 ** (attempt - 1))  # 1, 2, 4, 8, 16, 32...
                    delay += random.random()  # a tiny bit of random for desynchronizing multiple potential users
                    delay = min(delay, max_delay)
                    time.sleep(delay)
                    attempt += 1
            # and finally, just try one more time but let any exceptions bubble up
            return func(*args, **kwargs)

        return wrapped_func

    return inner_retry
