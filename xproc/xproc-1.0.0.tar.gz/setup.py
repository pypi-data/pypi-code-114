# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xproc']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'xproc',
    'version': '1.0.0',
    'description': 'Linux Proc File System Snooper',
    'long_description': '',
    'author': 'liyong',
    'author_email': 'hungrybirder@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/hungrybirder/xproc',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
