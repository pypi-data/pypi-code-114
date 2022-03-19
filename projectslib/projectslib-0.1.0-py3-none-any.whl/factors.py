import math
import itertools

flatten_iter = itertools.chain.from_iterable


# https://stackoverflow.com/a/6909532/5538273
def factors(n):
    return set(flatten_iter((i, n//i) for i in range(1, int(math.sqrt(n)+1)) if n % i == 0))
