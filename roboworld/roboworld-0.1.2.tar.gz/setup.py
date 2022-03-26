# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
    ['roboworld']

install_requires = \
    ['matplotlib', 'numpy']

package_data = \
    {'': ['*']}

keywords = ['education', 'gamification', 'cellular automaton', 'roboter', 'learning', 'beginners', 'computational thinking']

#long_description=long_description,
#long_description_content_type='text/x-rst',

long_description="""
``roboworld`` is an educational ``Python``-package designed for students to learn basic programming concepts, such as,

+ variables,
+ function calls,
+ conditionals, 
+ loops and
+ recursion.

Students have to navigate ``Robo`` (a roboter) through different two-dimensional discrete ``Worlds``.
``Robo`` represents a very simplistic machine that can only deal with very basic instructions, i.e., method calls.
Therefore, students have to extend the missing functionality step by step.
By this process they learn

1. to divde a problem into smaller pieces,
2. to abstract,
3. to recoginze pattern, and 
4. to design and implement algorithms.
"""

setup_kwargs = {
    'name': 'roboworld',
    'version': '0.1.2',
    'description': 'Educational roboter world for learning the basic programming concepts.',
    'long_description': long_description,
    'author': 'Benedikt Zoennchen',
    'author_email': 'benedikt.zoennchen@web.de',
    'maintainer': 'BZoennchen',
    'maintainer_email': 'benedikt.zoennchen@web.de',
    'url': 'https://github.com/BZoennchen/robo-world',
    'packages': packages,
    'install_requires': install_requires,
    'python_requires': '>=3.7.0,<4.0.0',
    'keywords': keywords
}

setup(**setup_kwargs)
