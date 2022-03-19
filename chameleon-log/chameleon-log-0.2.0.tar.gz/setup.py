# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chameleon_log']

package_data = \
{'': ['*']}

modules = \
['py']
install_requires = \
['logbook>=1.5.3,<2.0.0', 'single-version>=1.5.1,<2.0.0']

setup_kwargs = {
    'name': 'chameleon-log',
    'version': '0.2.0',
    'description': 'Python colored logging setup which adapts to environment',
    'long_description': '============\nChameleonLog\n============\n\nPython logging setup library which can choose the best available handler for an environment to produce colored message.\n\nFor example, if it detects that the application is running as service under systemd, it will route the logs to journald.\n',
    'author': 'Nguyễn Hồng Quân',
    'author_email': 'ng.hong.quan@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/AgriConnect/chameleon-log',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
