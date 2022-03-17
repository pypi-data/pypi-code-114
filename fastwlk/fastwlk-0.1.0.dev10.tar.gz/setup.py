# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastwlk', 'fastwlk.utils']

package_data = \
{'': ['*']}

install_requires = \
['networkx>=2.6.3,<3.0.0',
 'numpy>=1.22.1,<2.0.0',
 'pandas>=1.4.0,<2.0.0',
 'tqdm>=4.62.3,<5.0.0']

setup_kwargs = {
    'name': 'fastwlk',
    'version': '0.1.0.dev10',
    'description': 'fastwlk is a Python package that implements a fast version of the Weisfeiler-Lehman kernel.',
    'long_description': '=============================\nFastWLK\n=============================\n\nfastwlk is a Python package that implements a fast version of the Weisfeiler-Lehman kernel.\n',
    'author': 'Philip Hartout',
    'author_email': 'philip.hartout@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
