# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['skyrouter']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.10.0,<5.0.0', 'furl>=2.1.3,<3.0.0', 'httpx>=0.22.0,<0.23.0']

setup_kwargs = {
    'name': 'skyrouter',
    'version': '0.1.0',
    'description': 'Python API Client for Sky Routers (Sky Hubs)',
    'long_description': '# skyrouter\nPython API Client for Sky Routers (Sky Hubs)\n',
    'author': 'Tom Bulled',
    'author_email': '26026015+tombulled@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tombulled/skyrouter',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
