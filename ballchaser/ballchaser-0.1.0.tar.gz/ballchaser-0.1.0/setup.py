# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ballchaser']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'ballchaser',
    'version': '0.1.0',
    'description': 'Unofficial Python API client for the ballchasing.com API.',
    'long_description': '# ballchaser\nUnofficial Python API client for the ballchasing.com API.\n',
    'author': 'Tom Boyes-Park',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tom-boyes-park/ballchaser',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
