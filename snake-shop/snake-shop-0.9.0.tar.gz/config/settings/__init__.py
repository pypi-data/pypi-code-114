import os
from pathlib import Path
from django.core.management.utils import get_random_secret_key

if os.path.isfile(os.path.join(
    Path(__file__).resolve().parent, 'customize.py')):
    from .customize import SECRET_KEY, DEBUG  # @UnresolvedImport
else:
    from .customize_template import SECRET_KEY, DEBUG  # @Reimport
SECRET_KEY = SECRET_KEY or get_random_secret_key()
secret_key = SECRET_KEY  #pylint: disable=invalid-name

from .base.django import *
from .base.installed_apps import *
from .base.template import *
from .base.middleware import *
from oscar.defaults import *
from .base.oscar import *
from .base.logging import *
from .base.api import *
from django.utils.timezone import now


if os.path.isfile(os.path.join(
    Path(__file__).resolve().parent, 'customize.py')):
    from .customize import *
else:
    from .customize_template import *
SECRET_KEY = secret_key

SITE_ID = int(os.environ.get('SITE_ID', 1))

_DB = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': DB_NAME,
    'USER': DB_USER,
    'PASSWORD': DB_PASSWORD,
    'HOST': DB_HOST,
    'PORT': DB_PORT,
    'ATOMIC_REQUESTS': True,
    }

if not all((DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)) or TESTING:
    _DB = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
_DB['ATOMIC_REQUESTS'] = True
DATABASES = {'default': _DB}

SERVER_EMAIL = DEFAULT_FROM_EMAIL

TIMESTAMP = now()
MODE = MODE if 'MODE' in dir() else 'STANDALONE'
