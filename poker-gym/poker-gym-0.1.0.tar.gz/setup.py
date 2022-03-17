# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poker_gym']

package_data = \
{'': ['*']}

install_requires = \
['gym>=0.23.1,<0.24.0', 'numpy>=1.22.3,<2.0.0']

setup_kwargs = {
    'name': 'poker-gym',
    'version': '0.1.0',
    'description': "OpenAI Gym environment for Poker including No Limit Hold'em(NLHE) and Pot Limit Omaha(PLO)",
    'long_description': None,
    'author': 'azriel1rf',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
