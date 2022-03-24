# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['readmetester']

package_data = \
{'': ['*']}

install_requires = \
['Pygments>=2.8.1,<3.0.0',
 'object-colors>=2.0.0,<3.0.0',
 'pyproject-parser>=0.4.3,<0.5.0']

entry_points = \
{'console_scripts': ['readmetester = readmetester:main']}

setup_kwargs = {
    'name': 'readmetester',
    'version': '1.2.0',
    'description': 'Parse, test, and assert RST code-blocks',
    'long_description': None,
    'author': 'jshwi',
    'author_email': 'stephen@jshwisolutions.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
