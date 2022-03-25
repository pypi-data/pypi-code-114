# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['slck']

package_data = \
{'': ['*']}

install_requires = \
['fire>=0.4.0,<0.5.0', 'python-dotenv>=0.19.2,<0.20.0', 'slack-sdk>=3.0']

entry_points = \
{'console_scripts': ['slck = slck.cli:main']}

setup_kwargs = {
    'name': 'slck-cli',
    'version': '0.2.0',
    'description': 'Simple cli tool to manage your slack workspace',
    'long_description': '# slck-cli: Simple cli tool to manage your slack workspace\n\n![PyPI](https://img.shields.io/pypi/v/slck-cli?style=flat-square)\n[![GitHub license](https://img.shields.io/github/license/joe-yama/slck-cli?style=flat-square)](https://github.com/joe-yama/slck-cli/blob/main/LICENSE)\n\n## Basic Usage\n\n```bash\n# listing all users in workspace\n$ slck user list\nUser(id=\'U031L3JNBKS\', name=\'taro\', real_name=\'Taro Yamada\')\nUser(id=\'U036NS9S6HL\', name=\'jiro\', real_name=\'Jiro Tanaka\')\nUser(id=\'U032SU3SKBS\', name=\'hanako\', real_name=\'Hanako Suzuki\')\n\n# user search by real_name (or name or id)\n$ slck user find --real_name "Taro Yamada"\nUser(id=\'U031L3JNBKS\', name=\'taro\', real_name=\'Taro Yamada\')\n\n# channel list (filtered by prefix)\n$ slck channel list --prefix general\nChannel(id=\'C02AFAUOK33\', name=\'general\')\n\n# most reacted post in the channel\n$ slck message popular general\nMessage(message_type=\'message\', user=User(id=\'U031L3JNBKS\', name=\'taro\', real_name=\'Taro Yamada\'), channel=Channel(id=\'C02AFAUOK33\', name=\'general\'), ts=\'1647648476.156199\', text=\'テスト\', num_reply=0, num_replyuser=0, num_reaction=3, permalink=\'https://foo.slack.com/archives/C02AFAUOK33/p23471289471123\')\n```\n\n## Installation\n\n```bash\npip install slck-cli\n```\n\n## License\n\nThis software is released under the MIT License, see LICENSE.\n',
    'author': 'joe-yama',
    'author_email': 's1r0mqme@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/joe-yama/slck-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
