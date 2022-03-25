# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['booting']
setup_kwargs = {
    'name': 'booting',
    'version': '1.0',
    'description': '1. Open install the module -> pip install booting 2. Write in your code this line -> from booting import keep_alive 3. and after this write keep_alive() 4. Done! Your discord bot repl is alive 24\\7.',
    'long_description': None,
    'author': 'ENDER',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
