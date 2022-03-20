# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['random_snake']
entry_points = \
{'console_scripts': ['random-snake = random_snake:main']}

setup_kwargs = {
    'name': 'random-snake',
    'version': '1.0.0',
    'description': 'just a random sneaky snake',
    'long_description': None,
    'author': 'worldmaker',
    'author_email': 'worldmaker18349276@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
