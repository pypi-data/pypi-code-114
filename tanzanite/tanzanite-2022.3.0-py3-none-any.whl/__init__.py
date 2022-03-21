# -*- coding: utf-8 -*-

# pylint: disable=missing-module-docstring

# Standard imports
import datetime
import os
import textwrap

from pathlib import Path

# External imports
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


# Networking variables
DOMAIN = os.environ.get('DOMAIN', '127.0.0.1')
LOCALHOST = ['::', '127.0.0.1', 'localhost']
SERVER_NAME = DOMAIN
SERVER_HOST = f"http://{SERVER_NAME}"
SERVER_PORT = os.environ.get('SERVER_PORT', '8000')

# API variables
DEFAULT_API_VER = 'v1'
DEFAULT_API_PORT = '8000'

# File system variables
DEFAULT_UMASK = 0o007
TANZANITE_BASE_DIR = Path(__file__).parent
TANZANITE_DATA_DIR = Path(os.environ.get('TANZANITE_DATA_DIR', Path.cwd()))
TANZANITE_SOURCE_ROOT = TANZANITE_BASE_DIR.parent
DOCS_DIR = TANZANITE_SOURCE_ROOT / 'docs'
TESTS_DIR = TANZANITE_SOURCE_ROOT / 'tests'
BACKEND_DIR = TANZANITE_BASE_DIR / 'backend'
WEBAPPS_DIR = TANZANITE_BASE_DIR / 'webapps'
TEMPLATES_DIR = WEBAPPS_DIR / 'templates'
try:
    TEMPLATES = Jinja2Templates(directory=str(TEMPLATES_DIR))
except AssertionError:
    TEMPLATES = None
STATIC_DIR = TANZANITE_BASE_DIR / 'static'
STATIC_FILES = StaticFiles(directory=str(STATIC_DIR))
SPHINX_DOCS_HTML = DOCS_DIR / 'build' / 'html'
FAVICON_PATH = 'static/images/icons/favicon.ico'
# SQLITE_DATABASE_PATH = os.path.join(
#     f'{settings.environment_path}',
#     f'{str(settings.secrets_environment)}.db'
# )
# TODO(dittrich): FIX THIS
SQLITE_DATABASE_PATH = TANZANITE_DATA_DIR / 'tztest_db'
SQLALCHEMY_DATABASE_URI = f'sqlite://{str(SQLITE_DATABASE_PATH)}'


def _copyright():
    """Copyright string"""
    this_year = str(datetime.datetime.today().year)
    copyright_years = (
        f'2021-{this_year}'
        if '2021' != this_year
        else '2021'
    )
    copyright_str = textwrap.dedent(f"""
        This program was bootstrapped from a ``cookiecutter`` template created
        by Dave Dittrich <dave.dittrich@gmail.com>:

            https://github.com/davedittrich/cookiecutter-cliffapp-template.git
            https://cookiecutter-cliffapp-template.readthedocs.io

        Author:    Dave Dittrich <dave.dittrich@gmail.com>
        Copyright: {copyright_years}, Dave Dittrich. All rights reserved.
        License:   Apache Software License 2.0
        URL:       https://pypi.python.org/pypi/tanzanite""")  # noqa
    return copyright_str


__author__ = 'Dave Dittrich'
__copyright__ = _copyright()
__email__ = 'dave.dittrich@gmail.com'
__license__ = 'Apache Software License 2.0'
__summary__ = 'The Tanzanite purpleteaming and CTF platform.'
__title__ = 'tanzanite'
__url__ = 'https://github.com/davedittrich/tanzanite'

# Get development version from repository tags:
# https://github.com/tiangolo/poetry-version-plugin
__release__ = '2022.3.0'
__version__ = '2022.3.0'


__all__ = [
    'DOMAIN',
    'LOCALHOST',
    'DEFAULT_UMASK',
    'TANZANITE_BASE_DIR',
    'TANZANITE_DATA_DIR',
    'TANZANITE_SOURCE_ROOT',
    'TESTS_DIR',
    'BACKEND_DIR',
    'TEMPLATES_DIR',
    'TEMPLATES',
    'STATIC_DIR',
    'STATIC_FILES',
    'SPHINX_DOCS_HTML',
    'SQLITE_DATABASE_PATH',
    'SQLALCHEMY_DATABASE_URI',
    '_copyright',
    '__author__',
    '__copyright__',
    '__email__',
    '__release__',
    '__summary__',
    '__title__',
    '__url__',
    '__version__',
]

# vim: set ts=4 sw=4 tw=0 et :
