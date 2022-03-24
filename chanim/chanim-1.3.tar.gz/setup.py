# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chanim']

package_data = \
{'': ['*']}

install_requires = \
['manim']

entry_points = \
{'manim.plugins': ['chanim = chanim']}

setup_kwargs = {
    'name': 'chanim',
    'version': '1.3',
    'description': 'Manim extension for making chemistry videos',
    'long_description': '# Chanim\nThis is an extension to [Manim](https://www.github.com/ManimCommunity/manim) library (initially created by [3Blue1Brown](https://github.com/3b1b/manim)),\nfor making videos regarding chemistry.\n\n> A Hindi version of this README is available [here](https://github.com/raghavg123/chanim/blob/master/README-%E0%A4%B9%E0%A4%BF%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A5%80.md).\n\n## Installation (pip)\n`pip install chanim`\n\n## Installation (Source)\n1. Install the external dependencies for manim as described [here](https://docs.manim.community/en/latest/installation.html) according to your OS.\n2. Clone the contents of this repository.\n3. Open a terminal in the cloned directory and run `pip install -e .`, or if you prefer to use [poetry](https://python-poetry.org) instead, `poetry install`. This\'ll install `manim` for you as well if you don\'t already have it installed. (you\'ll still need to setup the external dependencies though)\n\nThat\'s about it. You can now do `from chanim import <*|object_name>` like any regular Python package. \n\n## Usage\n\nHere\'s a little example of it working.\n\n```py\nfrom chanim import *\n\nclass ChanimScene(Scene):\n    def construct(self):\n        ## ChemWithName creates a chemical diagram with a name label\n        chem = ChemWithName("*6((=O)-N(-CH_3)-*5(-N=-N(-CH_3)-=)--(=O)-N(-H_3C)-)", "Caffeine")\n\n        self.play(chem.creation_anim())\n        self.wait()\n```\n\nType this into a python (`.py`) file. I\'ll assume you named it `chem.py`\n\nIn your command prompt/terminal write this (assuming you\'re in your project directory):\n\n```sh\nmanim -p -qm chem.py ChanimScene\n```\nThis\'ll render your Scene and `p`review it in your default player (in `m`edium `q`uality).\n\n\nhttps://user-images.githubusercontent.com/65204531/124297601-dcafcf80-db78-11eb-936b-cdc913c91f25.mp4\n\n\nCongrats! You\'ve written and played your first animation with chanim (or "chanimation" should I say)\n\nExplore the code and docs (coming soon!) for more on how to use chanim.\n\n## Abilities\nCurrently chanim only supports drawing compounds and reactions along with a few chemfig commands (such as coordinate bonds and complexes etc.) but more is to come! If you have a suggestion, file an issue with a proper tag.\n\n## A Quick Note\nThere may be some faulty code and a lot of this may not be well made/documented. Feel free to file an issue if something doesn\'t work properly.\n',
    'author': 'kilacoda',
    'author_email': 'kilacoda@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/raghavg123/chanim',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
