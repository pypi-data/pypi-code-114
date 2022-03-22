# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['speedpycom']

package_data = \
{'': ['*']}

install_requires = \
['Django>=4.0.3,<5.0.0',
 'Pillow>=9.0.1,<10.0.0',
 'arrow>=1.2.2,<2.0.0',
 'boto3-stubs>=1.21.15,<2.0.0',
 'boto3>=1.21.15,<2.0.0',
 'celery-redbeat>=2.0.0,<3.0.0',
 'celery>=5.2.3,<6.0.0',
 'dj-database-url>=0.5.0,<0.6.0',
 'django-allauth>=0.49.0,<0.50.0',
 'django-braces>=1.15.0,<2.0.0',
 'django-cache-url>=3.3.0,<4.0.0',
 'django-ckeditor>=6.2.0,<7.0.0',
 'django-configurations>=2.3.2,<3.0.0',
 'django-cors-headers>=3.11.0,<4.0.0',
 'django-crispy-forms>=1.14.0,<2.0.0',
 'django-extensions>=3.1.5,<4.0.0',
 'django-filter>=21.1,<22.0',
 'django-import-export>=2.7.1,<3.0.0',
 'django-post-office>=3.6.0,<4.0.0',
 'django-redis>=5.2.0,<6.0.0',
 'django-ses>=2.6.1,<3.0.0',
 'django-storages>=1.12.3,<2.0.0',
 'django-taggit>=2.1.0,<3.0.0',
 'django-tailwind>=3.1.1,<4.0.0',
 'djangoql>=0.17.1,<0.18.0',
 'djangorestframework-simplejwt>=5.1.0,<6.0.0',
 'djangorestframework>=3.13.1,<4.0.0',
 'drf-spectacular>=0.21.2,<0.22.0',
 'flower>=1.0.0,<2.0.0',
 'gunicorn>=20.1.0,<21.0.0',
 'honeybadger>=0.8.0,<0.9.0',
 'psycopg2-binary>=2.9.3,<3.0.0',
 'requests>=2.27.1,<3.0.0',
 'sentry-sdk>=1.5.7,<2.0.0',
 'whitenoise>=6.0.0,<7.0.0']

setup_kwargs = {
    'name': 'speedpycom',
    'version': '0.1.5',
    'description': 'The Django Framework for SaaS',
    'long_description': '# SpeedPyCom – The Django Framework for SaaS\n\nBy [https://appliku.com/]()\n\n## Introduction\n\nSpeedPyCom is the collection of settings and requirements that allows you quick start of new production and deployment\nready Django Project for SaaS apps.\n\n## Some reasons you might want to use SpeedPyCom\n\n- Based on Django-Configurations, so while there is very useful base settings, it is easy to extend/override\n- Storages ready for S3 or local development\n- Credentials and some behaviour controlled via env vars\n- other useful apps and tools included\n\n## Discussions:\n\nJoin our Discord Community: https://appliku.com/discord\n\n',
    'author': 'Kostja P',
    'author_email': '123@appliku.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
