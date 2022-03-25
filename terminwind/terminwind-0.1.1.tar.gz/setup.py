# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['terminwind', 'terminwind.terminal']

package_data = \
{'': ['*']}

install_requires = \
['aiofile>=3.7.4,<4.0.0',
 'pyperclip>=1.8.2,<2.0.0',
 'rich>=11,<12',
 'textual>=0.1.15,<0.2.0']

setup_kwargs = {
    'name': 'terminwind',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Yubo Wang',
    'author_email': 'yubowang2007@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
