# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qctrltoolkit', 'qctrltoolkit.superconducting']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.16.2',
 'python-forge>=18.6.0,<19.0.0',
 'qctrl-commons>=15.0.2,<16.0.0',
 'toml>=0.10.0,<0.11.0']

extras_require = \
{':python_full_version >= "3.6.4" and python_version < "3.7"': ['dataclasses']}

setup_kwargs = {
    'name': 'qctrl-toolkit',
    'version': '0.0.0',
    'description': 'Q-CTRL Python Toolkit',
    'long_description': '# Q-CTRL Python Toolkit\n\nToolkit of convenience functions and classes for the Q-CTRL Python package.\n',
    'author': 'Q-CTRL',
    'author_email': 'support@q-ctrl.com',
    'maintainer': 'Q-CTRL',
    'maintainer_email': 'support@q-ctrl.com',
    'url': 'https://q-ctrl.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.4,<3.10',
}


setup(**setup_kwargs)
