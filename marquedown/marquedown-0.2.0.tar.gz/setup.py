# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['marquedown']

package_data = \
{'': ['*']}

install_requires = \
['Markdown>=3.3.6,<4.0.0']

setup_kwargs = {
    'name': 'marquedown',
    'version': '0.2.0',
    'description': 'Extending Markdown further by adding a few more useful notations.',
    'long_description': '',
    'author': 'Maximillian Strand',
    'author_email': 'maximillian.strand@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/deepadmax/marquedown',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
