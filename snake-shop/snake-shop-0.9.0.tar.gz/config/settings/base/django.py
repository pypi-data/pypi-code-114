import os
import sys
from pathlib import Path
from django.urls.base import reverse_lazy
from django.contrib.messages import constants as messages

__all__ = ('SECURE_PROXY_SSL_HEADER', 'X_FRAME_OPTIONS', 'ROOT_URLCONF', 
           'AUTH_USER_MODEL', 'BASE_DIR', 'LANGUAGE_CODE',
           'TIME_ZONE', 'USE_I18N', 'USE_L10N', 'USE_TZ',
           'LOGIN_REDIRECT_URL', 'LOGIN_URL', 'STATIC_URL', 'STATIC_ROOT',
           'STATICFILES_DIRS', 'MEDIA_URL', 'MEDIA_ROOT', 'TESTING',
           'WSGI_APPLICATION', 'AUTH_PASSWORD_VALIDATORS',
           'THUMBNAIL_PROCESSORS', 'PASSWORD_HASHERS',
           'AUTHENTICATION_BACKENDS', 'DATA_UPLOAD_MAX_NUMBER_FIELDS',
           'PHONENUMBER_DEFAULT_REGION', 'INTERNAL_IPS', 'LOCALE_PATHS',
           'LANGUAGES', 'MESSAGE_TAGS', 'DBBACKUP_STORAGE',
           'DBBACKUP_STORAGE_OPTIONS', 'DEFAULT_AUTO_FIELD',
           'DEBUG_TOOLBAR_CONFIG', 'EMAIL_BACKEND', 'EMAIL_FILE_PATH',
           'DATA_UPLOAD_MAX_NUMBER_FIELDS')

#MIGRATION_MODULES = {'flatpages': None}
WSGI_APPLICATION = 'config.wsgi.application'

ROOT_URLCONF = 'config.urls'
AUTH_USER_MODEL = 'user.User'

TESTING = sys.argv[1:2] == ['test']
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
X_FRAME_OPTIONS = 'SAMEORIGIN'

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'), )
LANGUAGES = (('de', 'Deutsch'), )
LANGUAGE_CODE = 'de'
TIME_ZONE = 'Europe/Berlin'
USE_I18N = True
USE_L10N = True
USE_TZ = True
URL_PREFIX_DEFAULT_LANGUAGE = False

LOGIN_REDIRECT_URL = reverse_lazy('catalogue:index')
LOGIN_URL = reverse_lazy('customer:login')
INTERNAL_IPS = ['127.0.0.1', ]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),
                    os.path.join(BASE_DIR, 'custom', 'static'),]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTHENTICATION_BACKENDS = ('user.backends.EmailModelBackend', )
DATA_UPLOAD_MAX_NUMBER_FIELDS = 2000

PHONENUMBER_DEFAULT_REGION = 'DE'


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'user.hashers.PBKDF2WrappedSHA1PasswordHasher',
]

MESSAGE_TAGS = {messages.ERROR: 'danger'}

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': os.path.join(BASE_DIR, 'backup')}

EMAIL_BACKEND = "custom.email_backend.EmailBackend"
EMAIL_FILE_PATH = f"{MEDIA_ROOT}/emails"

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

DEBUG_TOOLBAR_CONFIG={
    'DISABLE_PANELS': [
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.profiling.ProfilingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]
}

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240
