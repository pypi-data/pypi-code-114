# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['mtv_dl']
install_requires = \
['PyYAML>=6.0,<7.0',
 'beautifulsoup4>=4.10.0,<5.0.0',
 'certifi>=2021.10.8,<2022.0.0',
 'docopt>=0.6.2,<0.7.0',
 'durationpy==0.5',
 'ijson>=3.1.4,<4.0.0',
 'iso8601>=1.0.2,<2.0.0',
 'pydash>=5.1.0,<6.0.0',
 'rfc6266>=0.0.4,<0.0.5',
 'rich>=12.0.0,<13.0.0']

entry_points = \
{'console_scripts': ['mtv_dl = mtv_dl:main']}

setup_kwargs = {
    'name': 'mtv-dl',
    'version': '0.21.3',
    'description': 'MediathekView Downloader',
    'long_description': 'Command line tool to download videos from sources available through MediathekView.\n',
    'author': 'Frank Epperlein',
    'author_email': 'frank+mtv_dl@epperle.in',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fnep/mtv_dl',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
