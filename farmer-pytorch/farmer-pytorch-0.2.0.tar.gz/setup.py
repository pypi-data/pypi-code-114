# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['farmer_pytorch',
 'farmer_pytorch.logger',
 'farmer_pytorch.metrics',
 'farmer_pytorch.readers']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.3.2,<9.0.0',
 'matplotlib>=3.5.1,<4.0.0',
 'numpy>=1.21.2,<2.0.0',
 'torch>=1.9.1,<2.0.0']

setup_kwargs = {
    'name': 'farmer-pytorch',
    'version': '0.2.0',
    'description': 'deep learning tools: easy to run, easy to customize',
    'long_description': '# Pytorch segmentation\n\n## installation\n```\npip install farmer-pytorch\n```\n\n\n## Quick start\n[quick start](quickstart/)',
    'author': 'aiorhiroki',
    'author_email': '1234defgsigeru@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/aiorhiroki/farmer.pytorch',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.9',
}


setup(**setup_kwargs)
