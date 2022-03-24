from functools import lru_cache


def is_number(s):
    return not isinstance(to_number(s), str)


@lru_cache(maxsize=1)
def to_number(s):
    try:
        return float(s)
    except ValueError:
        return s
