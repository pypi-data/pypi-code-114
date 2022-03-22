# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['clive']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.4,<0.5.0',
 'requests>=2.27.1,<3.0.0',
 'websocket-client>=1.3.1,<2.0.0']

entry_points = \
{'console_scripts': ['clive = clive.cli:run']}

setup_kwargs = {
    'name': 'clive',
    'version': '0.1.2',
    'description': 'Follow Reddit live feeds from the comfort of the CLIS',
    'long_description': 'CLIVE\n=====\n\n[![PyPI Version](https://img.shields.io/pypi/v/clive)](https://pypi.python.org/pypi/CLIve)\n[![PyPI](https://img.shields.io/pypi/l/clive)](https://pypi.python.org/pypi/CLIve)\n\nWhen following a Reddit live feed, who wants to have a big ugly webpage open\nall the time? Not me, and perhaps not you either.\n\nSo I started to write a command line interface that prints messages\nas they arrive. It\'s still a **little** rough as I put this together in a few\nhours, so consider it a work in progress. Contributions and suggestions\nwelcome and encouraged.\n\nIf you are wondering why *clive*, it\'s a  blend of *cli* and *live*.\n\n\nInstallation\n------------\n\n    $ pip install clive\n\nUsage\n-----\n\n    $ clive wmk50bsm9vt3\n\nWhere `wmk50bsm9vt3` is the last part of the live feed URL from Reddit.\n\nLicense\n-------\n\nThe MIT License (MIT)\nCopyright (c) 2016 Sven Steinbauer\n\nPermission is hereby granted, free of charge, to any person obtaining a copy \nof this software and associated documentation files (the "Software"), to deal \nin the Software without restriction, including without limitation the rights \nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell \ncopies of the Software, and to permit persons to whom the Software is \nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, \nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE \nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER \nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE \nSOFTWARE.\n\n\n',
    'author': 'Sven Steinbauer',
    'author_email': 'sven@unlogic.co.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://svenito.github.io/clive/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
