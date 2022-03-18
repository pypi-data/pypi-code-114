# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['daemonize']
setup_kwargs = {
    'name': 'lel-python-daemonize',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Léo El Amri',
    'author_email': 'leo@superlel.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/lel-amri/lel-python-daemonize',
    'py_modules': modules,
    'python_requires': '>=3.8,<3.9',
}


setup(**setup_kwargs)
