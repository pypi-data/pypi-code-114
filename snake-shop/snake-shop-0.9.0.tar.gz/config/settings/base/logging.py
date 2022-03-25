
__all__ = ('LOGGING', )

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'oscar.checkout': {
            'level': 'ERROR',
            #'filters': ['require_debug_false'],
            'handlers': ['mail_admins'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
}
