# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['taxus']

package_data = \
{'': ['*']}

install_requires = \
['gpytorch>=1.6.0,<2.0.0',
 'numpy>=1.22.3,<2.0.0',
 'pandas>=1.4.1,<2.0.0',
 'patsy>=0.5.2,<0.6.0',
 'torch>=1.11.0,<2.0.0']

setup_kwargs = {
    'name': 'taxus',
    'version': '0.0.1',
    'description': 'Gaussian Process models for transcriptome data',
    'long_description': '# _taxus_\n\n### Gaussian Process models for transcriptome data\n',
    'author': 'Rens Holmer',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
