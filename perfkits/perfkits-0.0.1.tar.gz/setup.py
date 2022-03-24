# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['perfkits']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'perfkits',
    'version': '0.0.1',
    'description': '',
    'long_description': None,
    'author': 'Gongziting Tech Ltd.',
    'author_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
