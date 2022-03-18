# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['toobigdatadoc']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=3.1.27,<4.0.0', 'argparse>=1.4.0,<2.0.0']

entry_points = \
{'console_scripts': ['too = src.toobigdatadoc.too:main']}

setup_kwargs = {
    'name': 'desertislandutils',
    'version': '0.1.0',
    'description': 'A collection of personal convenience utilities',
    'long_description': None,
    'author': 'mahiki',
    'author_email': 'mahiki@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
