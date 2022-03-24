import functools
from .line_perf_dbg import LinePerfDbg


def perf(log_func=None):
    def entangle(func):
        @functools.wraps(func)
        def wrapper(*subs, **kwargs):
            dbg = LinePerfDbg()
            ret = dbg.runcall(func, *subs, **kwargs)
            stats = dbg.gen_stats()
            if log_func:
                log_func(stats)
            else:
                dbg.print_stats(stats)
            return ret
        return wrapper
    return entangle
