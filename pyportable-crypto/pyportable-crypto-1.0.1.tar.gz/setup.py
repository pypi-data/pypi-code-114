# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyportable_crypto', 'pyportable_crypto.cipher_gen']

package_data = \
{'': ['*'], 'pyportable_crypto.cipher_gen': ['cache/*']}

install_requires = \
['lk-logger>=5.0.1,<6.0.0', 'lk-utils>=2.2.0,<3.0.0']

setup_kwargs = {
    'name': 'pyportable-crypto',
    'version': '1.0.1',
    'description': 'Crypto plugin for pyportable-installer project.',
    'long_description': None,
    'author': 'Likianta',
    'author_email': 'likianta@foxmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
