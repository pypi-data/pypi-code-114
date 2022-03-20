# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['dbspace',
 'dbspace.control',
 'dbspace.readout',
 'dbspace.signal',
 'dbspace.signal.PAC',
 'dbspace.signal.PRE',
 'dbspace.signal.dLFP',
 'dbspace.testing.readout',
 'dbspace.utils',
 'dbspace.viz',
 'dbspace.viz.MM',
 'dbspace.viz.TF']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.4.3,<4.0.0',
 'nibabel>=3.2.1,<4.0.0',
 'nilearn>=0.8.1,<0.9.0',
 'numpy>=1.21.2,<2.0.0',
 'scikit-learn>=1.0,<2.0',
 'scipy>=1.7.1,<2.0.0',
 'seaborn>=0.11.2,<0.12.0',
 'setuptools==49.2.1',
 'sklearn>=0.0,<0.1']

setup_kwargs = {
    'name': 'dbspace',
    'version': '0.1.0',
    'description': 'Library for data-driven, network-level modeling of clinical DBS dynamics',
    'long_description': None,
    'author': 'Vineet Tiruvadi',
    'author_email': 'virati@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.12,<4.0.0',
}


setup(**setup_kwargs)
