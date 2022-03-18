# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['deprecated_decorator']

package_data = \
{'': ['*']}

install_requires = \
['pylint>=2.12.2,<3.0.0']

setup_kwargs = {
    'name': 'pylint-deprecated-decorator',
    'version': '0.2.0',
    'description': 'A pylint checker to detect @deprecated decorators on classes and functions',
    'long_description': None,
    'author': 'withakay',
    'author_email': 'jack@fader.co.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
