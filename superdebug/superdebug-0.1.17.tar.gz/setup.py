# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['superdebug']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=5.0.0,<6.0.0',
 'mypyc-ipython>=0.0.2,<0.0.3',
 'numpy>=1.0.0,<2.0.0',
 'torch>=1.0.0,<2.0.0',
 'torchvision>=0.1.0,<0.2.0']

setup_kwargs = {
    'name': 'superdebug',
    'version': '0.1.17',
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
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
