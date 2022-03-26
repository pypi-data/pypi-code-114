import os
try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backport to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

from ..assets import css
from ..assets import js
from ..assets.js import cft

class StaticFilesManager(object):
    def __init__(self):
        pass

    def js(self, file):
        code = ''
        try:
            code = pkg_resources.read_text(js, f'{file}.js')
        except Exception as e:
            print(e)
        return code

    def cft(self, file):
        code = ''
        try:
            code = pkg_resources.read_text(cft, f'{file}.js')
        except Exception as e:
            print(e)
        return code

    def css(self):
        styles = ''
        try:
            styles = pkg_resources.read_text(css, 'style.css')
        except Exception as e:
            print(e)
        return styles
