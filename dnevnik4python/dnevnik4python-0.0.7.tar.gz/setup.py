# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dnevnik4python']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2',
 'fake-useragent>=0.1.11,<0.2.0',
 'lxml>=4.8.0,<5.0.0',
 'pytz>=2022.1,<2023.0',
 'requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'dnevnik4python',
    'version': '0.0.7',
    'description': '',
    'long_description': None,
    'author': 'hrog-zip',
    'author_email': '65674012+hrog-zip@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
