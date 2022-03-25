# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_message_broker', 'django_message_broker.server']

package_data = \
{'': ['*']}

install_requires = \
['Django>=4.0,<5.0',
 'msgspec>=0.3.2,<0.4.0',
 'pyzmq>=22.3.0,<23.0.0',
 'tornado>=6.1,<7.0']

extras_require = \
{'docs': ['Sphinx>=4.3.2,<5.0.0',
          'sphinx_rtd_theme>=1.0.0,<2.0.0',
          'myst-parser>=0.16.1,<0.17.0']}

setup_kwargs = {
    'name': 'django-message-broker',
    'version': '0.2.1',
    'description': 'All-in-one message broker for Django supporting Channels, Celery and process workers',
    'long_description': '# Django Message Broker\n\n[![Documentation Status](https://readthedocs.org/projects/django-message-broker/badge/?version=latest)](https://django-message-broker.readthedocs.io/en/latest/?badge=latest)\n\n<img src="assets/DMB Ecosystem opt.svg"\n     alt="Django message broker ecosystem"\n     width=200\n     align="right"/>\n\nDjango Message Broker is a plugin written in Python for Django that provides an all-in-one\nmessage broker. It interfaces with Django Channels and Celery [1], and replaces the need\nfor separate message brokers such as Redis and RabbitMQ.\n\nThe motivating use case for Django Message Broker is small site solutions where it is\neasier to deploy a single server containing all the required functionality rather than a\nmulti-server solution. An example would be a small site running data science models, where\nexecuting the model is a long running process and needs to execute in the background so\nthat it doesn’t degrade the responsiveness of the user interface.\n\nPotential scenarios for Django Message Broker include:\n\n+ Prototyping, Testing, Training\n+ Data science projects where the model complexity exceeds the capabilities of packages such\n  as Shiny, Dash and Streamlit.\n+ Small systems with a low number of users.\n\nThe Django Message Broker is an installable component of the Django platform that provides\nan easy to install, all-in-one alternative for small scale solutions. It does not replace\nthe need for high volume message brokers where message volume and redundancy are important.\n\n**Note**\n\n1. The Celery interface is in development and not supported in this release. \n\n## Installation\n\nInstall latest stable version into your python environment using pip::\n\n    pip install django-message-broker\n\nOnce installed add ``django_message_broker`` to your ``INSTALLED_APPS`` in settings.py:\n\n    INSTALLED_APPS = (\n        \'django_message_broker\',\n        ...        \n    )\n\nDjango Message Broker should be installed as early as possible in the installed applications\nlist and ideally before other applications such as Channels and Celery. The message broker\nforks a background process which should occur before other applications create new threads in\nthe current process.\n\n## Configure Django Channels Layers\n\nTo configure the Django Message Broker as a Channels layer add the following to the ``CHANNEL_LAYERS``\nsetting in settings.py:\n\n    CHANNEL_LAYERS = {\n        \'default\': {\n            \'BACKEND\': \'django_message_broker.ChannelsServerLayer\',\n        },\n    }\n',
    'author': 'Tanzo Creative Ltd',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/django-message-broker/django-message-broker',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
