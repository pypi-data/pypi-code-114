# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pymdown_include']

package_data = \
{'': ['*']}

install_requires = \
['Markdown>=3.3.6,<4.0.0']

entry_points = \
{'markdown.extensions': ['include = pymdown_include:PymdownInclude']}

setup_kwargs = {
    'name': 'pymdown-include',
    'version': '0.1.0',
    'description': 'Pymdown include plugin',
    'long_description': '# Pymdown-Include\n\npoetry install\npoetry build\npoetry run pytest\npoetry run pytest --cov=pymdown_include',
    'author': 'Jacques Supcik',
    'author_email': 'jacques.supcik@hefr.ch',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/supcik/pymdown-include/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
