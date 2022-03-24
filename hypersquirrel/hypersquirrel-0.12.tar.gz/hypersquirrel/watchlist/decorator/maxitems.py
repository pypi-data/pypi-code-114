import sys


def decorator(watchlist):
    if not hasattr(watchlist, "max_items"):
        watchlist.max_items = sys.maxsize
