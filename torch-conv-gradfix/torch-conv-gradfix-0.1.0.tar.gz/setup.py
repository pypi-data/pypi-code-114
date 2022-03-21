# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['torch_conv_gradfix']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.21.0', 'torch>1.7']

entry_points = \
{'console_scripts': ['docs = torch_conv_gradfix:__docs',
                     'serve = torch_conv_gradfix:__serve',
                     'test = torch_conv_gradfix:__test']}

setup_kwargs = {
    'name': 'torch-conv-gradfix',
    'version': '0.1.0',
    'description': "(Taken from NVIDIA) Replacement for Pytorch's Conv2D and Conv2DTranspose with support for higher-order gradients and disabling unnecessary gradient computations.",
    'long_description': "# PyTorch Conv2D Gradient Fix\n\n**(Taken from NVIDIA) Replacement for Pytorch's Conv2D and Conv2DTranspose with support for higher-order gradients and disabling unnecessary gradient computations.**\n\n![action](https://img.shields.io/github/workflow/status/ppeetteerrs/torch-conv-gradfix/build?logo=githubactions&logoColor=white)\n[![pypi](https://img.shields.io/pypi/v/torch-conv-gradfix.svg)](https://pypi.python.org/pypi/torch-conv-gradfix)\n[![codecov](https://img.shields.io/codecov/c/github/ppeetteerrs/torch-conv-gradfix?label=codecov&logo=codecov)](https://app.codecov.io/gh/ppeetteerrs/torch-conv-gradfix)\n[![docs](https://img.shields.io/github/deployments/ppeetteerrs/torch-conv-gradfix/github-pages?label=docs&logo=readthedocs)](https://ppeetteerrs.github.io/torch-conv-gradfix)\n\n## Installation\n\n`conda install torch-conv-gradfix -c ppeetteerrs`\n\n## Usage\n\nSee the `Example` tab.",
    'author': 'Peter Yuen',
    'author_email': 'ppeetteerrsx@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ppeetteerrs/torch-conv-gradfix',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
