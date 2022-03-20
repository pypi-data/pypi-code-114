# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pacup']

package_data = \
{'': ['*'],
 'pacup': ['.mypy_cache/*',
           '.mypy_cache/3.8/*',
           '.mypy_cache/3.8/_typeshed/*',
           '.mypy_cache/3.8/attr/*',
           '.mypy_cache/3.8/click/*',
           '.mypy_cache/3.8/collections/*',
           '.mypy_cache/3.8/ctypes/*',
           '.mypy_cache/3.8/email/*',
           '.mypy_cache/3.8/html/*',
           '.mypy_cache/3.8/importlib/*',
           '.mypy_cache/3.8/json/*',
           '.mypy_cache/3.8/logging/*',
           '.mypy_cache/3.8/os/*',
           '.mypy_cache/3.8/pacup/*',
           '.mypy_cache/3.8/rich/*',
           '.mypy_cache/3.8/urllib/*']}

install_requires = \
['httpx>=0.22.0,<0.23.0',
 'packaging>=21.3,<22.0',
 'rich>=12.0.0,<13.0.0',
 'typer>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['pacup = pacup.__main__:main']}

setup_kwargs = {
    'name': 'pacup',
    'version': '0.1.1',
    'description': 'Help maintainers update pacscripts',
    'long_description': None,
    'author': 'Sourajyoti Basak',
    'author_email': 'wiz28@protonmail.com',
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
