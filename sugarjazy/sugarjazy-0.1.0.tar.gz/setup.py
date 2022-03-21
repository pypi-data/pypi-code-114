# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sugarjazy']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['mongars = sugarjazy.cli:main']}

setup_kwargs = {
    'name': 'sugarjazy',
    'version': '0.1.0',
    'description': 'Parse json logs output from uber-go/zap library nicely',
    'long_description': None,
    'author': 'Chmouel Boudjnah',
    'author_email': 'chmouel@chmouel.com',
    'maintainer': 'Chmouel Boudjnah',
    'maintainer_email': 'chmouel@chmouel.com',
    'url': 'https://github.com/chmouel/sugarjazy',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
