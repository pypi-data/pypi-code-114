# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['fuzzy_graph_coloring']
install_requires = \
['matplotlib>=3.5.1,<4.0.0',
 'networkx>=2.6.3,<3.0.0',
 'numpy>=1.22.2,<2.0.0',
 'pygad>=2.16.3,<3.0.0']

setup_kwargs = {
    'name': 'fuzzy-graph-coloring',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Ferdinand Koenig',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
