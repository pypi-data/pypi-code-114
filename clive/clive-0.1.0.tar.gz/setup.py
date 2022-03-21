# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['clive']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.4,<0.5.0',
 'requests>=2.27.1,<3.0.0',
 'websocket-client>=1.3.1,<2.0.0']

entry_points = \
{'console_scripts': ['clive = clive.cli:run']}

setup_kwargs = {
    'name': 'clive',
    'version': '0.1.0',
    'description': 'Follow Reddit live feeds from the comfort of the CLIS',
    'long_description': None,
    'author': 'Sven Steinbauer',
    'author_email': 'sven@unlogic.co.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Svenito/clive',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
