# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ballchaser']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'ballchaser',
    'version': '0.4.1',
    'description': 'Unofficial Python API client for the ballchasing.com API.',
    'long_description': '# ballchaser ⚽️🚗\nUnofficial Python API client for the ballchasing.com API.\n\n# Getting Started\n```commandline\npip install ballchaser\n```\n\nAll API requests are exposed via the `BallChaser` class which is initialised with a [ballchasing.com API token](https://ballchasing.com/doc/api#header-authentication).\n\n```python\nimport os\nfrom ballchaser.client import BallChaser\n\nball_chaser = BallChaser(os.getenv("BALLCHASING_API_TOKEN"))\n\n# search and retrieve replay metadata\nreplays = [\n    replay\n    for replay in ball_chaser.get_replays(player_name="GarrettG", replay_count=10)\n]\n\n# retrieve replay statistics\nrelay_stats = [\n    ball_chaser.get_replay(replay["id"])\n    for replay in replays\n]\n```\n',
    'author': 'Tom Boyes-Park',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tom-boyes-park/ballchaser',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
