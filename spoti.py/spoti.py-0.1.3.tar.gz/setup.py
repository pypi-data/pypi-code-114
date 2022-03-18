# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['spotipy', 'spotipy.objects', 'spotipy.typings']

package_data = \
{'': ['*']}

modules = \
['py']
install_requires = \
['aiohttp>=3.8.0,<4.0.0']

extras_require = \
{'docs': ['sphinx>=4.3.1,<5.0.0',
          'sphinxcontrib-trio>=1.1.2,<2.0.0',
          'sphinx-copybutton>=0.4.0,<0.5.0',
          'sphinxext-opengraph>=0.5.0,<0.6.0',
          'furo>=2021.11.23,<2022.0.0'],
 'speed': ['orjson>=3.6.4,<4.0.0']}

setup_kwargs = {
    'name': 'spoti.py',
    'version': '0.1.3',
    'description': 'An async wrapper for the Spotify Web API.',
    'long_description': '# spoti.py\nAn async wrapper for the [Spotify API](https://developer.spotify.com/documentation/web-api/) written in Python.\n\n## Support\n- [Documentation](https://spoti-py.readthedocs.io/)\n- [GitHub](https://github.com/Axelware/spoti.py)\n- [Discord](https://discord.com/invite/w9f6NkQbde)\n\n## Installation\n**Python 3.10 or later is required.**\n```shell\npip install -U spoti.py\n```\nTo get the development version:\n```shell\npip install -U git+https://github.com/Axelware/spoti.py\n```\n',
    'author': 'Axel',
    'author_email': 'axelancerr@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Axelware/spoti.py',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.10.0,<4.0.0',
}


setup(**setup_kwargs)
