# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['inspyred_print']

package_data = \
{'': ['*']}

install_requires = \
['lastversion>=2.0.1,<3.0.0', 'pypattyrn>=1.2,<2.0', 'toml>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'inspyred-print',
    'version': '1.2.1',
    'description': 'A collection of ascii codes to make your visible strings prettier.',
    'long_description': None,
    'author': 'Taylor B.',
    'author_email': '43686206+tayjaybabee@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
