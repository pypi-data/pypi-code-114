# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['skit_auth']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.5.3,<0.6.0',
 'requests-mock>=1.9.3,<2.0.0',
 'requests>=2.27.1,<3.0.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['skit-auth = skit_auth.cli:main']}

setup_kwargs = {
    'name': 'skit-auth',
    'version': '0.1.3',
    'description': "Authorization for skit.ai's platform.",
    'long_description': None,
    'author': 'ltbringer',
    'author_email': 'amresh.venugopal@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/skit-ai/skit-auth',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
