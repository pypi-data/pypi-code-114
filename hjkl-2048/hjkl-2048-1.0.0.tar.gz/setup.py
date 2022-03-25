# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['hjkl_2048']
install_requires = \
['numpy>=1.18.5,<2.0.0']

entry_points = \
{'console_scripts': ['hjkl-2048 = hjkl_2048:main']}

setup_kwargs = {
    'name': 'hjkl-2048',
    'version': '1.0.0',
    'description': 'play 2048 with hjkl',
    'long_description': None,
    'author': 'worldmaker',
    'author_email': 'worldmaker18349276@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
