# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bilireq',
 'bilireq.auth',
 'bilireq.dynamic',
 'bilireq.live',
 'bilireq.login',
 'bilireq.user',
 'bilireq.utils']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.22.0,<0.23.0', 'rsa>=4.8,<5.0']

extras_require = \
{':extra == "qrcode"': ['qrcode[pil]>=7.3.1,<8.0.0']}

setup_kwargs = {
    'name': 'bilireq',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'SK-415',
    'author_email': '2967923486@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
