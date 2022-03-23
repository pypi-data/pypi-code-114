# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pipetory',
 'pipetory.exceptions',
 'pipetory.futils',
 'pipetory.pipes',
 'pipetory.types']

package_data = \
{'': ['*']}

install_requires = \
['modin>=0.13.3,<0.14.0',
 'numpy>=1.22.3,<2.0.0',
 'pandas>=1.4.1,<2.0.0',
 'pyarrow>=7.0.0,<8.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'ray>=1.11.0,<2.0.0']

setup_kwargs = {
    'name': 'pipetory',
    'version': '0.1.0',
    'description': 'Package to easily build and compose pipelines with several backends',
    'long_description': None,
    'author': 'Juan Lara',
    'author_email': 'julara@unal.edu.co',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
