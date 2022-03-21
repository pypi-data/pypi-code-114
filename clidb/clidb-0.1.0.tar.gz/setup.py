# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['clidb']

package_data = \
{'': ['*']}

install_requires = \
['duckdb>=0.3.2,<0.4.0',
 'textual-inputs>=0.2.0,<0.3.0',
 'textual>=0.1.0,<0.2.0']

extras_require = \
{'pandas': ['pandas>=1.3,<2.0']}

entry_points = \
{'console_scripts': ['clidb = clidb.cli:CliDB.run']}

setup_kwargs = {
    'name': 'clidb',
    'version': '0.1.0',
    'description': 'CLI based SQL client for local data',
    'long_description': None,
    'author': 'Danny Boland',
    'author_email': 'email@dannyboland.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
