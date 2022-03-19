# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['deeputilities']

package_data = \
{'': ['*']}

install_requires = \
['pytest-cov>=3.0.0,<4.0.0']

setup_kwargs = {
    'name': 'deeputilities',
    'version': '0.1.0',
    'description': 'A source-native, automated machine learning workflow',
    'long_description': '# DeepUtilities\n',
    'author': 'Ashia Lewis',
    'author_email': 'pantagruelspendulum@protonmail.com',
    'maintainer': 'Ashia Lewis',
    'maintainer_email': 'pantagruelspendulum@protonmail.com',
    'url': 'https://github.com/AeRabelais/DeepUtilities',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
