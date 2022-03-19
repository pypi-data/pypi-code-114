# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kosmorrolib']

package_data = \
{'': ['*']}

install_requires = \
['python-dateutil>=2.8,<3.0', 'skyfield-data>=3,<5', 'skyfield>=1.21,<2.0']

setup_kwargs = {
    'name': 'kosmorrolib',
    'version': '1.0.6',
    'description': 'A library to computes the ephemerides.',
    'long_description': "# Kosmorrolib - a library to compute your ephemerides!\n\n[![Coverage Status](https://coveralls.io/repos/github/Kosmorro/lib/badge.svg?branch=main)](https://coveralls.io/github/Kosmorro/lib?branch=main) [![Version on PyPI](https://img.shields.io/pypi/v/kosmorrolib)](https://pypi.org/project/kosmorrolib)  [![IRC: #kosmorro on Libera.Chat](https://img.shields.io/badge/Libera.Chat-%23kosmorro-blueviolet)](https://web.libera.chat/?nick=Astronaut?#kosmorro)\n\n[![Stand with Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner2-direct.svg)](https://github.com/vshymanskyy/StandWithUkraine/blob/main/docs/README.md)\n\n## Installation\n\n### Requirements\n\nKosmorrolib requires the following software to work:\n\n- Python ≥ 3.7.0\n\nAnd that's all!\n\n### Production environment\n\nKosmorrolib is available [on PyPI](https://pypi.org/project/kosmorrolib/). To use it, invoke `pip install kosmorrolib`.\n\n### Development environment\n\nTo contribute to Kosmorrolib, you will need [Poetry](https://python-poetry.org), a software to manage the project from development to publishing.\n\nClone this repository and run `poetry install` to install the dependencies.\nAnd that's all, your development environment is ready for the fight! 👏\n\n## Documentation\n\nAll the documentation can be found [on the website](https://kosmorro.space/lib/doc).\n",
    'author': 'Jérôme Deuchnord',
    'author_email': 'jerome@deuchnord.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://kosmorro.space/lib',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
