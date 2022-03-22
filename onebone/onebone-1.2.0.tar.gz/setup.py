# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['onebone',
 'onebone.feature',
 'onebone.math',
 'onebone.preprocessing',
 'onebone.signal',
 'onebone.utils']

package_data = \
{'': ['*']}

install_requires = \
['PyWavelets==1.1.1',
 'matplotlib>=3.3.4',
 'numpy>=1.19.5',
 'pandas>=1.1.5',
 'scipy>=1.5.4',
 'sklearn>=0.0,<0.1']

setup_kwargs = {
    'name': 'onebone',
    'version': '1.2.0',
    'description': 'An Open Source Signal Processing Library for Sensor Signals about vibration, current, etc.',
    'long_description': None,
    'author': 'Kyunghwan Kim',
    'author_email': 'kyunghwan.kim@onepredict.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.5,<3.11',
}


setup(**setup_kwargs)
