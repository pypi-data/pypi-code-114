# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['amanibhavam']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['hello = amanibhavam.cli:main']}

setup_kwargs = {
    'name': 'amanibhavam',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Amanibhavam',
    'author_email': 'iam@defn.sh',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
