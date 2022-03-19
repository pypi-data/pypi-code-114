# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mpsf']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'mpsf',
    'version': '0.3.1',
    'description': 'Multiprocessing Single Function (mpsf)',
    'long_description': None,
    'author': 'morten',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/Yggdrasil27/mpsf',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
