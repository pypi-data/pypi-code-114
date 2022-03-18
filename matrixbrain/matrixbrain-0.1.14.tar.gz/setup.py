# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['matrixbrain']

package_data = \
{'': ['*'], 'matrixbrain': ['UNKNOWN.egg-info/*']}

install_requires = \
['farm-haystack>=1.2.0,<2.0.0',
 'genanki>=0.13.0,<0.14.0',
 'tqdm>=4.63.0,<5.0.0']

entry_points = \
{'console_scripts': ['matrixbrain = matrixbrain.matrixbrain:main']}

setup_kwargs = {
    'name': 'matrixbrain',
    'version': '0.1.14',
    'description': 'Use machine learning to transform documents ( pdf, txt, doc ) in anki decks.',
    'long_description': None,
    'author': 'Huggyturd',
    'author_email': 'cloura.dev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
