# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['starship']

package_data = \
{'': ['*']}

install_requires = \
['anyio>=3.4.0,<5', 'starlette>=0.17.1,<1']

extras_require = \
{':python_version < "3.9"': ['typing-extensions>=3']}

setup_kwargs = {
    'name': 'starship',
    'version': '0.1.0',
    'description': 'A performant HTTP router for Starlette',
    'long_description': '# starship\n',
    'author': 'Adrian Garcia Badaracco',
    'author_email': 'adrian@adriangb.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/adriangb/starship',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
