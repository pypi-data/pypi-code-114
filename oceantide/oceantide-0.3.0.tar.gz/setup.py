# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oceantide', 'oceantide.core', 'oceantide.input', 'oceantide.output']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.4,<9.0.0',
 'dask>=2022.3.0,<2023.0.0',
 'gcsfs>=2022.2.0,<2023.0.0',
 'netCDF4>=1.5.8,<2.0.0',
 'numpy>=1.22.3,<2.0.0',
 'scipy>=1.8.0,<2.0.0',
 'xarray>=2022.3.0,<2023.0.0',
 'zarr>=2.11.1,<3.0.0']

setup_kwargs = {
    'name': 'oceantide',
    'version': '0.3.0',
    'description': 'Ocean tide prediction',
    'long_description': None,
    'author': 'Oceanum Developers',
    'author_email': 'developers@oceanum.science',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
