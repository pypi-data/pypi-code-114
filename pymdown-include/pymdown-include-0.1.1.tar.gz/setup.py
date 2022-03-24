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
    'version': '0.1.1',
    'description': 'Pymdown include plugin',
    'long_description': '# Pymdown-Include\n\nI tried hard to make the base name of the file to be included in the search\npath, but I couldn\'t figure out how to do that. During the "preprocessor"\nphase, I have no information about the file being processed. I just have the\ncontent of the file as an array of lines.\n\n## Some useful comands for developing\n\n```\npoetry install\npoetry build\npoetry run pytest\npoetry run pytest --cov=pymdown_include\n```',
    'author': 'Jacques Supcik',
    'author_email': 'jacques.supcik@hefr.ch',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/supcik/pymdown-include/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
