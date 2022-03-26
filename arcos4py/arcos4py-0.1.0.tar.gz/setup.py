# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['arcos4py', 'arcos4py.plotting', 'arcos4py.tools', 'tests']

package_data = \
{'': ['*'], 'tests': ['testdata/*']}

install_requires = \
['matplotlib>=3.3.4',
 'numpy>=1.21.5',
 'pandas>=1.3.5',
 'scikit-learn>=1.0.2',
 'scipy>=1.7.3']

extras_require = \
{'dev': ['tox>=3.20.1,<4.0.0',
         'virtualenv>=20.2.2,<21.0.0',
         'pip>=20.3.1,<21.0.0',
         'twine>=3.3.0,<4.0.0',
         'pre-commit>=2.12.0,<3.0.0',
         'toml>=0.10.2,<0.11.0',
         'bump2version>=1.0.1,<2.0.0'],
 'doc': ['mkdocs>=1.1.2,<2.0.0',
         'mkdocs-include-markdown-plugin>=1.0.0,<2.0.0',
         'mkdocs-material>=6.1.7,<7.0.0',
         'mkdocstrings>=0.15.2,<0.16.0',
         'mkdocs-autorefs>=0.2.1,<0.3.0',
         'Jinja2<3.0.3'],
 'test': ['black>=21.5b2,<22.0',
          'isort>=5.8.0,<6.0.0',
          'flake8>=3.9.2,<4.0.0',
          'flake8-docstrings>=1.6.0,<2.0.0',
          'mypy>=0.900,<0.901',
          'pytest>=6.2.4,<7.0.0',
          'pytest-cov>=2.12.0,<3.0.0',
          'PyYAML>=6.0,<7.0']}

setup_kwargs = {
    'name': 'arcos4py',
    'version': '0.1.0',
    'description': 'A python package to detect collective spatio-temporal phenomena.',
    'long_description': '# arcos4py\n\n\n[![pypi](https://img.shields.io/pypi/v/arcos4py.svg)](https://pypi.org/project/arcos4py/)\n[![python](https://img.shields.io/pypi/pyversions/arcos4py.svg)](https://pypi.org/project/arcos4py/)\n[![Build Status](https://github.com/bgraedel/arcos4py/actions/workflows/dev.yml/badge.svg)](https://github.com/bgraedel/arcos4py/actions/workflows/dev.yml)\n[![codecov](https://codecov.io/gh/bgraedel/arcos4py/branch/main/graphs/badge.svg)](https://codecov.io/github/bgraedel/arcos4py)\n\n\n\nA python package to detect collective Spatio-temporal phenomena\nPackage is currently in testing phase, i.e. additional features will be added such as additional plotting functionallity.\nThis also means that functionallity might change in the feature.\n\n* Documentation: <https://bgraedel.github.io/arcos4py>\n* GitHub: <https://github.com/bgraedel/arcos4py>\n* PyPI: <https://pypi.org/project/arcos4py/>\n* Free software: MIT\n\n\n## Features\n\nAutomated Recognition of Collective Signalling (arcos4py) is a python port of the R package ARCOS (https://github.com/dmattek/ARCOS\n) to identify collective spatial events in time series data.\nThe software identifies collective protein activation in 2- and 3D cell cultures over time. Such collective waves have been recently identified in various biological systems.\nThey have been demonstrated to play an important role in the maintenance of epithelial homeostasis (Gagliardi et al., 2020, Takeuchi et al., 2020, Aikin et al., 2020),\nin the acinar morphogenesis (Ender et al., 2020), osteoblast regeneration (De Simone et al., 2021), and in the coordination of collective cell migration (Aoki et al., 2017, Hino et al., 2020).\n\nDespite its focus on cell signaling, the framework can also be applied to other spatially correlated phenomena that occur over time.\n\n### Todo\'s\n- Add additionall plotting functions such as collective event duration, noodle plots for collective id tracks, measurment histogram etc.\n- Add additionall tests for binarization and de-biasing modules.\n- Add example processing to documentation with images of collective events.\n\nData Format\n-----------\nTime series should be arranged in "long format" where each row defines the object\'s location, time, and optionally the measurement value.\n\nARCOS defines an ARCOS object on which several class methods can be used to prepare the data and calculate collective events.\nOptionally the objects used in the ARCOS class can be used individually by importing them from arcos.tools\n\nInstallation\n------------\nThe arcos python package can be installed with:\n\n        pip install arcos4py\n\n## Credits\n\nMaciej Dobrzynski (https://github.com/dmattek) created the original ARCOS algorithm.\n\nThis package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage) project template.\n',
    'author': 'Benjamin Graedel',
    'author_email': 'benjamin.graedel@unibe.ch',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/bgraedel/arcos4py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)
