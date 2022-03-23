# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['genesis']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'genesis',
    'version': '0.3.4',
    'description': 'Implementation of FreeSWITCH Event Socket protocol with asyncio',
    'long_description': '# What is Genesis?\n\nGenesis is a python library designed to build applications (with asyncio) that work with freeswitch through ESL.\n\n[![Gitpod badge](https://img.shields.io/badge/Gitpod-ready%20to%20code-908a85?logo=gitpod)](https://gitpod.io/#https://github.com/Otoru/Genesis)\n[![Tests badge](https://github.com/Otoru/Genesis/actions/workflows/tests.yml/badge.svg)](https://github.com/Otoru/Genesis/actions/workflows/tests.yml)\n[![Build badge](https://github.com/Otoru/Genesis/actions/workflows/pypi.yml/badge.svg)](https://github.com/Otoru/Genesis/actions/workflows/pypi.yml)\n[![License badge](https://img.shields.io/github/license/otoru/Genesis.svg)](https://github.com/Otoru/Genesis/blob/master/LICENSE.md)\n[![Pypi Version badge](https://img.shields.io/pypi/v/Genesis)](https://pypi.org/project/genesis/)\n[![Pypi python version badge](https://img.shields.io/pypi/pyversions/Genesis)](https://pypi.org/project/genesis/)\n[![Pypi wheel badge](https://img.shields.io/pypi/wheel/Genesis)](https://pypi.org/project/genesis/)\n\n## What is FreeSwitch?\n\nFreeSWITCH is a free and open-source application server for real-time communication, WebRTC, telecommunications, video and Voice over Internet Protocol (VoIP). Multiplatform, it runs on Linux, Windows, macOS and FreeBSD. It is used to build PBX systems, IVR services, videoconferencing with chat and screen sharing, wholesale least-cost routing, Session Border Controller (SBC) and embedded communication appliances. It has full support for encryption, ZRTP, DTLS, SIPS. It can act as a gateway between PSTN, SIP, WebRTC, and many other communication protocols. Its core library, libfreeswitch, can be embedded into other projects. It is licensed under the Mozilla Public License (MPL), a free software license.\n\nBy [wikipedia](https://en.wikipedia.org/wiki/FreeSWITCH).\n\n## What is ESL?\n\nESL is a way to communicate with FreeSwitch. See more details [here](https://freeswitch.org/confluence/display/FREESWITCH/Event+Socket+Library).\n\n## Why asyncio?\n\nAsynchronous programming is a type of parallel programming in which a unit of work is allowed to run separately from the primary application thread. When the work is complete, it notifies the main thread about completion or failure of the worker thread. There are numerous benefits to using it, such as improved application performance and enhanced responsiveness. We adopted this way of working, as integrating genesis with other applications is simpler, since you only need to deal with python\'s native asynchronous programming interface.\n\n## Docs\n\nThe project documentation is in [here](https://github.com/Otoru/Genesis/wiki).\n\n## How to contribute?\n\nIf you are thinking of contributing in any way to the project, you will be very welcome. Whether it\'s improving existing documentation, suggesting new features or running existing bugs, it\'s only by working together that the project will grow.\n\nDo not forget to see our [Contributing Guide][2] and our [Code of Conduct][3] to always be aligned with the ideas of the project.\n\n[2]: https://github.com/Otoru/Genesis/blob/master/CONTRIBUTING.md\n[3]: https://github.com/Otoru/Genesis/blob/master/CODE_OF_CONDUCT.md\n\n## Contributors\n\nWill be welcome ❤️\n\n## Author\n\n| [<img src="https://avatars0.githubusercontent.com/u/26543872?v=3&s=115"><br><sub>@Otoru</sub>](https://github.com/Otoru) |\n| :----------------------------------------------------------------------------------------------------------------------: |\n',
    'author': 'Vitor',
    'author_email': 'contato@vitoru.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Otoru/Genesis#readme',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
