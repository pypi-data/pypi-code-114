# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poc_dependency_gob',
 'poc_dependency_gob.one',
 'poc_dependency_gob.three',
 'poc_dependency_gob.two']

package_data = \
{'': ['*']}

extras_require = \
{'skinny': ['sklearn>=0.0,<0.1'],
 'standard': ['torch>=1.11.0,<2.0.0', 'matplotlib>=3.5.1,<4.0.0']}

setup_kwargs = {
    'name': 'poc-dependency-gob',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@gobsingh.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
