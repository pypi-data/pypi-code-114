# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['goodhound']

package_data = \
{'': ['*']}

install_requires = \
['pandas==1.3.5', 'py2neo==2021.2.3']

entry_points = \
{'console_scripts': ['goodhound = goodhound:main']}

setup_kwargs = {
    'name': 'goodhound',
    'version': '1.1.2',
    'description': 'Attackers think in graphs, defenders think in actions, management think in charts.  GoodHound operationalises Bloodhound by determining the busiest paths to high value targets and creating actionable output to prioritise remediation of attack paths.',
    'long_description': '# GoodHound\n![PyPI - Downloads](https://img.shields.io/pypi/dm/goodhound)\n```\n   ______                ____  __                      __\n  / ____/___  ____  ____/ / / / /___  __  ______  ____/ /\n / / __/ __ \\/ __ \\/ __  / /_/ / __ \\/ / / / __ \\/ __  / \n/ /_/ / /_/ / /_/ / /_/ / __  / /_/ / /_/ / / / / /_/ /  \n\\____/\\____/\\____/\\__,_/_/ /_/\\____/\\__,_/_/ /_/\\__,_/   \n                                                         \n```\n> Attackers think in graphs, defenders think in actions, management think in charts.\n\nGoodHound operationalises Bloodhound by determining the busiest paths to high value targets and creating actionable output to prioritise remediation of attack paths.\n\n[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/B0B7AAAK2)  \n> I\'m lucky enough to do this for a living. Any donations will be passed on to my local foodbank, animal sanctuary and animal rescue centres.\n\n## Usage\n\n### Quick Start\nFor a very quick start with most of the default options, make sure you have your neo4j server running and loaded with SharpHound data and run:\n```\npip install goodhound\ngoodhound -p "neo4jpassword"\n```\nThis will process the data in neo4j and output 3 csv reports in the current working directory.\n\n![Demo](images/demo.gif)\n\n## Documentation\nAll documentation can be found in the [wiki](https://github.com/idnahacks/GoodHound/wiki)\n\n## Acknowledgments\n- The [py2neo](https://py2neo.org) project which makes this possible.\n- The [PlumHound](https://github.com/PlumHound/PlumHound) project which gave me the idea of creating something similar which suited my needs.\n- The [aclpwn](https://github.com/fox-it/aclpwn.py) for the idea around exploit cost.\n- The [Bloodhound Gang Slack channel](https://bloodhoundhq.slack.com) for Cypher help.\n- The [BloodHound project](https://bloodhound.readthedocs.io/en/latest/index.html) for changing the world and for continuing their support for the Open-Source community even when having a commercial offering.\n',
    'author': 'Andi Morris',
    'author_email': 'andi.morris@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/idnahacks/GoodHound',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
