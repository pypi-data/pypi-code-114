from datetime import datetime

STAGE = 'DEVELOPMENT'
MODE = 'STANDALONE'  # 'MASTER', 'SLAVE'

SECRET_KEY = None
ALLOWED_HOSTS = ['localhost']
DEBUG = True
ADMINS = (('Frank Hennige', 'info@snake-soft.com'),)

DB_NAME = None
DB_USER = None
DB_PASSWORD = None
DB_HOST = None
DB_PORT = 5432

EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'no-reply@localhost'
EMAIL_HOST_PASSWORD = 'smtp-secret'
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'no-reply@localhost'
EMAIL_REPLY_TO = 'info@localhost'

URL_PREFIX_DEFAULT_LANGUAGE = True

LOCKDOWN_ENABLED = False
LOCKDOWN_AFTER = datetime.strptime('2021,1,1,0,0', "%Y,%m,%d,%H,%M")
LOCKDOWN_UNTIL = datetime.strptime('2021,12,31,11,59', "%Y,%m,%d,%H,%M")
LOCKDOWN_AUTHFORM_SUPERUSERS_ONLY = True
LOCKDOWN_AUTHFORM_STAFF_ONLY = True
LOCKDOWN_FORM = 'lockdown.forms.AuthForm'

OSCAR_FROM_EMAIL = 'Company.de <info@company.de>'
OSCAR_SEARCH_DISABLED_FIELDS = []
