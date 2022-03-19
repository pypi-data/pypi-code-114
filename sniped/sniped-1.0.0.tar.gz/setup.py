# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sniped']

package_data = \
{'': ['*']}

install_requires = \
['typer[all]>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['sniped = sniped.__main__:app']}

setup_kwargs = {
    'name': 'sniped',
    'version': '1.0.0',
    'description': 'Turn snippets of code into beautiful images.',
    'long_description': '# sniped\n\n`sniped` is a CLI tool that helps you turn code snippets into beautiful images.\n',
    'author': 'Rodrigo Girão Serrão',
    'author_email': '5621605+RodrigoGiraoSerrao@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
