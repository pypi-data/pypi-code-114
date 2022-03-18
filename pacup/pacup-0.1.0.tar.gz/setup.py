# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pacup']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.22.0,<0.23.0',
 'packaging>=21.3,<22.0',
 'rich>=12.0.0,<13.0.0',
 'typer>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['pacup = pacup.__main__:main']}

setup_kwargs = {
    'name': 'pacup',
    'version': '0.1.0',
    'description': 'Help maintainers update pacscripts',
    'long_description': None,
    'author': 'Sourajyoti Basak',
    'author_email': 'wiz28@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
