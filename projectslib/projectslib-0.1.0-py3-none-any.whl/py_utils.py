import datetime
import functools


def range2(start, end=None, step=1):
    """1-index inclusive range"""
    if end is None:
        return range(1, start + 1, step)
    else:
        return range(start, end + 1, step)


def relative_date_range(start, end=None, step=1):
    base = datetime.date.today()
    return (base + datetime.timedelta(days=x) for x in range(start, end, step))


def print_items(iterable):
    for item in iterable:
        print(item)


def union(args):
    return functools.reduce(lambda x, y: x | y, args, set())
