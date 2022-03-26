# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tooly']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'tooly',
    'version': '0.1.4',
    'description': '',
    'long_description': None,
    'author': '方块八',
    'author_email': 'liyuan5202004@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
