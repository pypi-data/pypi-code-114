# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mpipartition']

package_data = \
{'': ['*']}

install_requires = \
['mpi4py>=3.1.0,<4.0.0', 'numpy>1.10']

setup_kwargs = {
    'name': 'mpipartition',
    'version': '0.1.0',
    'description': 'MPI volume decomposition and particle distribution tools',
    'long_description': None,
    'author': 'Michael Buehlmann',
    'author_email': 'buehlmann.michi@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
