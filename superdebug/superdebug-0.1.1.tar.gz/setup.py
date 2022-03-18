# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['superdebug']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.0.1,<10.0.0',
 'mypyc-ipython>=0.0.2,<0.0.3',
 'numpy>=1.22.3,<2.0.0',
 'torch>=1.11.0,<2.0.0',
 'torchvision>=0.12.0,<0.13.0']

setup_kwargs = {
    'name': 'superdebug',
    'version': '0.1.1',
    'description': 'Convenient debugging for machine learning projects',
    'long_description': None,
    'author': 'Azure-Vision',
    'author_email': 'hewanrong2001@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
