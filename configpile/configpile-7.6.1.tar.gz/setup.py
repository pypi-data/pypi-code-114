# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['configpile']

package_data = \
{'': ['*']}

install_requires = \
['class-doc>=0.2.6,<0.3.0', 'typing-extensions>=4.1.1,<5.0.0']

extras_require = \
{'rich': ['rich>=11.2.0,<12.0.0']}

setup_kwargs = {
    'name': 'configpile',
    'version': '7.6.1',
    'description': 'Configuration from command line parameters, configuration files and environment variables',
    'long_description': 'ConfigPile\n==========\n\nA configuration library for Python\n',
    'author': 'Denis Rosset',
    'author_email': 'physics@denisrosset.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/denisrosset/configpile.git',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
