# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['rpa', 'rpa.recognition']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.19.3,<2.0.0',
 'opencv-python-headless>=4.5.2,<5.0.0',
 'pillow>=8.4.0,<9.0.0',
 'pytesseract>=0.3.6,<0.4.0',
 'rpaframework-core>=7.0.0,<8.0.0']

setup_kwargs = {
    'name': 'rpaframework-recognition',
    'version': '2.0.0',
    'description': 'Core utilities used by RPA Framework',
    'long_description': 'rpaframework-recognition\n========================\n\nThis library enablous various recognition features with `RPA Framework`_\nlibraries, such as image template matching.\n\n.. _RPA Framework: https://rpaframework.org\n',
    'author': 'RPA Framework',
    'author_email': 'rpafw@robocorp.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://rpaframework.org/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
