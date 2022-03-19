# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_logo']

package_data = \
{'': ['*'],
 'nonebot_plugin_logo': ['templates/*',
                         'templates/fonts/*',
                         'templates/images/*']}

install_requires = \
['Jinja2>=3.0.0,<4.0.0',
 'imageio>=2.12.0,<3.0.0',
 'nonebot-adapter-onebot>=2.0.0-beta.1,<3.0.0',
 'nonebot-plugin-htmlrender>=0.0.4.1',
 'nonebot2>=2.0.0-beta.1,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-logo',
    'version': '0.2.1',
    'description': 'Nonebot2 plugin for making logo in PornHub or other styles',
    'long_description': None,
    'author': 'meetwq',
    'author_email': 'meetwq@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.3,<4.0.0',
}


setup(**setup_kwargs)
