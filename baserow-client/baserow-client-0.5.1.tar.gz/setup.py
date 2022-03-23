# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['baserow', 'baserow.orm']

package_data = \
{'': ['*']}

install_requires = \
['databind.core>=1.2.1,<2.0.0',
 'databind.json>=1.2.1,<2.0.0',
 'requests>=2.26.0,<3.0.0',
 'typing-extensions>=3.0.0']

setup_kwargs = {
    'name': 'baserow-client',
    'version': '0.5.1',
    'description': 'Client for the baserow.io API.',
    'long_description': '# baserow-client\n\nA Python client for [Baserow.io](https://baserow.io/) with simple ORM capabilities.\n\n> __Note__: This package is currently under development. Some APIs may break without prior notice.\n\n__Installation__\n\n    $ pip install baserow-client\n',
    'author': 'Niklas Rosenstein',
    'author_email': 'rosensteinniklas@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
