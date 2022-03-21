# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yacmmal', 'yacmmal.load', 'yacmmal.types']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'pydantic>=1.9.0,<2.0.0']

setup_kwargs = {
    'name': 'yacmmal',
    'version': '0.1.1',
    'description': 'Yet Another Config Manager for MAchine Learning (yacmmal) is a package to automatically load config files for machine learning projects.',
    'long_description': None,
    'author': 'Juan Lara',
    'author_email': 'julara@unal.edu.co',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
