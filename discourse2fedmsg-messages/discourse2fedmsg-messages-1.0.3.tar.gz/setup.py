# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['discourse2fedmsg_messages', 'discourse2fedmsg_messages.tests']

package_data = \
{'': ['*']}

install_requires = \
['fedora-messaging>=2.0.1']

entry_points = \
{'fedora.messages': ['discourse.event.v1 = '
                     'discourse2fedmsg_messages:DiscourseMessageV1']}

setup_kwargs = {
    'name': 'discourse2fedmsg-messages',
    'version': '1.0.3',
    'description': 'A schema package for messages sent by discourse2fedmsg',
    'long_description': '# discourse2fedmsg messages\n\nA schema package for [discourse2fedmsg](http://github.com/fedora-infra/discourse2fedmsg).\n\nSee the [detailed documentation](https://fedora-messaging.readthedocs.io/en/latest/messages.html) on packaging your schemas.\n',
    'author': 'Fedora Infrastructure Team',
    'author_email': 'infrastructure@lists.fedoraproject.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fedora-infra/discourse2fedmsg-messages',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.7,<4.0.0',
}


setup(**setup_kwargs)
