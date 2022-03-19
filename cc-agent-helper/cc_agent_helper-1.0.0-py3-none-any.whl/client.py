import collections
import io
from datetime import datetime
from random import randrange
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from . import settings


def login_required(f):
    def deco(self, *args, **kwargs):
        if not self.is_authenticated:
            self.login()
        return f(self, *args, **kwargs)

    return deco


class BaseClient(requests.Session):
    debug_captcha = False
    is_authenticated = False

    def __init__(self, credentials, base_domain=None):
        super(BaseClient, self).__init__()
        self.credentials = credentials
        self.base_domain = base_domain or self.default_domain

    @property
    def default_domain(self):
        raise NotImplementedError

    def captcha_solver(self, img, **kwargs):
        """
        captcha solver
        """
        origin_img = img

        if isinstance(img, str):
            img = io.StringIO(img)

        if isinstance(img, bytes):
            img = io.BytesIO(img)

        r = self.post(settings.CAPTCHA_API, data=kwargs, files=dict(file=img))
        captcha = r.text.replace(' ', '')

        return r.text.replace(' ', '')

    @property
    def username(self):
        return self.credentials.get('username')

    @property
    def password(self):
        return self.credentials.get('password')

    @property
    def base_uri(self):
        return urlparse(self.base_domain)

    @property
    def root(self):
        raise NotImplementedError

    def _url(self, path='', origin=None):
        return '{origin.scheme}://{origin.netloc}/{path}'.format(
            path=path.lstrip('/'),
            origin=origin or self.base_uri
        )

    @staticmethod
    def str2time(text):
        if isinstance(text, str):
            return datetime.fromisoformat(text)

        return text

    @staticmethod
    def format_float(text):
        try:
            return float(text.replace(',', ''))
        except ValueError:
            return text

    def format_date(self, date_time):
        return self.str2time(date_time).strftime(self.date_time_pattern)

    @property
    def date_time_pattern(self):
        raise NotImplementedError

    @staticmethod
    def get_form(html, **kwargs):
        soup = BeautifulSoup(html, 'html.parser')
        form = soup.find('form', attrs=kwargs)
        target_url = form.get('action')
        form_data = dict(map(lambda n: (n.get('name'), n.get('value')), form.find_all('input')))

        return target_url, form_data

    def random_ip(self, base_ip='116.118.{}.{}'):
        self.headers.update({
            'X-Forwarded-For': base_ip.format(randrange(200), randrange(200))
        })

    IGNORE_FIELDS = ['deep']

    def parent_report(self, data, category=False, filter_fn=None):
        key_fn = build_key(['category'] if category else None, (('username', self.root),))
        return merge_stream(data, key_fn=key_fn, filter_fn=filter_fn, ignore_fields=self.IGNORE_FIELDS)

    def login(self):
        raise NotImplementedError

    def win_lose(self, from_date, to_date, **kwargs):
        raise NotImplementedError

    def outstanding(self, *args, **kwargs):
        return []

    def tickets(self, from_date, to_date):
        return []


def merge_stream(data, key_fn=None, repeat=True, filter_fn=None, ignore_fields=None):
    collector = collections.defaultdict(lambda: collections.defaultdict(int))

    key_fn = key_fn or build_key()

    for item in data:
        key = key_fn(item)
        if repeat:
            yield item

        # only collect data from filtered item
        if filter_fn and not filter_fn(item):
            continue

        for k, v in item.items():
            if not isinstance(v, (float, int)):
                continue

            if ignore_fields and k in ignore_fields:
                continue

            collector[key][k] += v

    for key, values in collector.items():
        yield dict(values, **dict(key))


def build_key(fields=['username'], extras=None):
    def f(item):
        result = tuple()

        if fields:
            result += tuple(map(lambda x: (x, item.get(x)), fields))

        if extras:
            result += extras

        return result

    return f
