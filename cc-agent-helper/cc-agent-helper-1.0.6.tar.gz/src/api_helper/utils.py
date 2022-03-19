import random
from collections import defaultdict
from functools import reduce
from urllib.parse import urlparse
from . import settings


def get_uri(uri='', base=None):
    return '{}{}'.format(base, uri)


def get_base_url(origin):
    url = urlparse(origin)  # type: ParseResult
    return url.scheme + "://" + url.netloc + '/'


def patch_header(session, header=None):
    if header is None:
        header = settings.DEFAULT_HEADERS
    session.headers.update(header)


def random_ip(session, base_ip='116.118.{}.{}'):
    session.headers.update({
        'X-Forwarded-For': base_ip.format(random.randrange(200), random.randrange(200))
    })

def _sum_reduce(a, b):
    a[b[1]] += b[2]
    return a


def filter_data(fields, reserve=False):
    def f(x):
        return x[1] not in fields if reserve else x[1] in fields

    return f


def sum_reduce(parent, data):
    return [(parent, k, v) for k, v in reduce(_sum_reduce, data, defaultdict(int)).items()]
