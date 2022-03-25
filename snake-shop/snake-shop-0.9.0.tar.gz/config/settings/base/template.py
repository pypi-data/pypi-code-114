import os
from config.settings import DEBUG
from .django import BASE_DIR

__all__ = ('TEMPLATE_LOADERS', 'TEMPLATES')

#base_dir = Path(__file__).resolve().parent.parent.parent.parent

if DEBUG:
    TEMPLATE_LOADERS = [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader'
    ]
else:
    TEMPLATE_LOADERS = [
        (
            'django.template.loaders.cached.Loader',
            [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]
        )
    ]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'custom_templates')
        ], #OSCAR_ES_MAIN_TEMPLATE_DIR,],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.communication.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
                'custom.context_processors.main'
            ],
            'loaders': TEMPLATE_LOADERS
        },
    },
]
