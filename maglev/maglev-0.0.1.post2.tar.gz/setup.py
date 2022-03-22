# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['maglev']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'maglev',
    'version': '0.0.1.post2',
    'description': "Python utilities for working with NVIDIA's MLOps infrastructure.",
    'long_description': "NVIDIA MagLev\n=============\n\nPython utilities for working with NVIDIA's MLOps infrastructure.\n",
    'author': 'Eric Hall',
    'author_email': 'ehall@nvidia.com',
    'maintainer': 'Ryan Miller',
    'maintainer_email': 'rjmill@nvidia.com',
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
