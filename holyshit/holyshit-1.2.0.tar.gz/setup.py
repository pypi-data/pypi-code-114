# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['holyshit']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.6.0']

setup_kwargs = {
    'name': 'holyshit',
    'version': '1.2.0',
    'description': 'Asynchronous experimental wrapper for the holyshit.wtf API',
    'long_description': '# holyshit.py\n\nAn experimental wrapper for the holyshit API.  \nThis is asynchronous, meaning that you can use it within your Discord bot without making blocking calls\n\n## Installation\nPyPi wheel (stable)\n```bash\n$ python3.8 -m pip install holyshit # requires Python 3.8+ for aiohttp compatibility\n```\n\nGit source (unstable)\n```bash\n$ python3.8 -m pip install git+https://github.com/cobaltgit/holyshit # requires Python 3.8+ for aiohttp compatibility\n```\n\n## Examples\n\nSee the [examples](https://github.com/cobaltgit/holyshit/tree/main/examples) for some examples on how to use this library\n',
    'author': 'cobaltgit',
    'author_email': 'criterion@chitco.co.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
