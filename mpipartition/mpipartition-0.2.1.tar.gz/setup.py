# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mpipartition']

package_data = \
{'': ['*']}

install_requires = \
['mpi4py>=3.1.0,<4.0.0', 'numpy>=1.10,<2.0']

setup_kwargs = {
    'name': 'mpipartition',
    'version': '0.2.1',
    'description': 'MPI volume decomposition and particle distribution tools',
    'long_description': 'MPIPartition\n============\n\n\n.. image:: https://img.shields.io/pypi/v/mpipartition.svg\n        :target: https://pypi.python.org/pypi/mpipartition\n\n\n\nA python module for MPI volume decomposition and particle distribution\n\n\n* Free software: MIT license\n* Documentation: https://argonnecpac.github.io/MPIPartition\n\n\nFeatures\n--------\n\n* Cartesian partitioning of a cubic volume among available MPI ranks\n* distributing particle-data among ranks to the corresponding subvolume\n* overloading particle-data at rank boundaries\n* exchaning particle-data according to a "owner"-list of keys per rank\n\n\nInstallation\n------------\n\nInstalling from the PyPI repository:\n\n.. code-block:: bash\n\n   pip install mpipartition\n\nInstalling the development version from the GIT repository\n\n.. code-block:: bash\n\n   git clone https://github.com/ArgonneCPAC/mpipartition.git\n   cd mpipartition\n   python setup.py develop\n\nRequirements\n------------\n\n* `mpi4py <https://mpi4py.readthedocs.io/en/stable/>`_: MPI for Python\n* `numpy <https://numpy.org/>`_: Python array library',
    'author': 'Michael Buehlmann',
    'author_email': 'buehlmann.michi@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ArgonneCPAC/MPIPartition',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
