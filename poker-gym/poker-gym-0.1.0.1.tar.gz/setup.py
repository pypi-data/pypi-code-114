# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poker_gym', 'poker_gym.envs']

package_data = \
{'': ['*']}

install_requires = \
['PettingZoo>=1.17.0,<2.0.0',
 'gym>=0.23.1,<0.24.0',
 'numpy>=1.21.5,<2.0.0',
 'phevaluator>=0.5.0.4,<0.6.0.0']

extras_require = \
{'rllib': ['ray>=1.11.0,<2.0.0'], 'tune': ['ray>=1.11.0,<2.0.0']}

setup_kwargs = {
    'name': 'poker-gym',
    'version': '0.1.0.1',
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
    'extras_require': extras_require,
    'python_requires': '>=3.7,<3.10',
}


setup(**setup_kwargs)
