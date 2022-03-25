import sys
import os
from pathlib import Path
import django

from django.test import TestCase, Client
from django_extensions.management.commands import show_urls

import functools
import re

from django.conf import settings
from django.contrib.admindocs.views import simplify_regex
from django.utils import translation
from django.urls.exceptions import NoReverseMatch
FMTR = show_urls.FMTR



class TestAllUrlsTestCase(TestCase):
    #databases = []

    def setUp(self):
        self.urls = UrlFetcher().get_names()
        self.anon = Client()
        #print(list(self.urls))

    def test_urls(self):
        for url in self.urls:
            continue  # <-------------
            try:
                self.anon.get(url)
            except NoReverseMatch as err:
                print(err)
            else:
                print(url)
            #self.assert
            #self.assertEqual(self.anon.get(), second, msg)

    def url_runner(self, url):
        return url


class UrlFetcher(show_urls.Command):

    cached_result = None

    def get_urls(self):
        for url in self.url_dicts():
            yield url['url']

    def get_names(self):
        for url in self.url_dicts():
            if url['url_name']:
                yield url['url_name']

    def url_dicts(self):
        for url, module, url_name, decorator in self.fetch_urls():
            yield {'url': url, 'module': module, 'url_name': url_name, 'decorator': decorator}

    def fetch_urls(self):
        if self.cached_result:
            return self.cached_result
        options = {
            'decorator': None,
            'language': 'de',
            'no_color': True,
            'format_style': 'table',
            'urlconf': 'ROOT_URLCONF',
            'unsorted': False,
        }
        self.cached_result = self.handle(**options)
        return self.cached_result

    def handle(self, *args, **options):
        language = options['language']
        if language is not None:
            translation.activate(language)
            self.LANGUAGES = [(code, name) for code, name in getattr(settings, 'LANGUAGES', []) if code == language]
        else:
            self.LANGUAGES = getattr(settings, 'LANGUAGES', ((None, None), ))

        decorator = options['decorator']
        if not decorator:
            decorator = ['login_required']

        format_style = options['format_style']
        pretty_json = format_style == 'pretty-json'
        if pretty_json:
            format_style = 'json'

        urlconf = options['urlconf']
        urlconf = __import__(getattr(settings, urlconf), {}, {}, [''])

        view_functions = self.extract_views_from_urlpatterns(urlconf.urlpatterns)
        for (func, regex, url_name) in view_functions:
            if hasattr(func, '__globals__'):
                func_globals = func.__globals__
            elif hasattr(func, 'func_globals'):
                func_globals = func.func_globals
            else:
                func_globals = {}

            decorators = [d for d in decorator if d in func_globals]

            if isinstance(func, functools.partial):
                func = func.func
                decorators.insert(0, 'functools.partial')

            if hasattr(func, '__name__'):
                func_name = func.__name__
            elif hasattr(func, '__class__'):
                func_name = '%s()' % func.__class__.__name__
            else:
                func_name = re.sub(r' at 0x[0-9a-f]+', '', repr(func))

            module = '{0}.{1}'.format(func.__module__, func_name)
            url_name = url_name or ''
            url = simplify_regex(regex)
            decorator = ', '.join(decorators)
            yield(url, module, url_name, decorator)
