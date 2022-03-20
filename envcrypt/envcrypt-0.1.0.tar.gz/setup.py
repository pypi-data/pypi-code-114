# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['envcrypt']

package_data = \
{'': ['*']}

install_requires = \
['pycrypto>=2.6.1,<3.0.0']

setup_kwargs = {
    'name': 'envcrypt',
    'version': '0.1.0',
    'description': 'Encrypt and decrypt environment variable files.',
    'long_description': None,
    'author': 'Dan Kelleher',
    'author_email': 'dan@danklabs.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
