# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cfdtools',
 'cfdtools.gmsh',
 'cfdtools.ic3',
 'cfdtools.meshbase',
 'cfdtools.physics']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.15,<2.0']

entry_points = \
{'console_scripts': ['cfdinfo = cfdtools._cli:info',
                     'cfdwrite_ic3v2 = cfdtools._cli:write_ic3v2',
                     'cfdwrite_ic3v3 = cfdtools._cli:write_ic3v3',
                     'ic3brief = cfdtools._cli:ic3brief']}

setup_kwargs = {
    'name': 'cfdtools',
    'version': '0.2.0',
    'description': 'Tools for mesh and solution management in CFD',
    'long_description': None,
    'author': 'j.gressier',
    'author_email': 'jeremie.gressier@isae-supaero.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jgressier/cfdtools',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
