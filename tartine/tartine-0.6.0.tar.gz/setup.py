# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['tartine']
install_requires = \
['glom>=22.1.0,<23.0.0']

setup_kwargs = {
    'name': 'tartine',
    'version': '0.6.0',
    'description': 'Manipulate dynamic spreadsheets with arbitrary layouts using Python ',
    'long_description': None,
    'author': 'MaxHalford',
    'author_email': 'maxhalford25@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
