# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['valida']

package_data = \
{'': ['*']}

install_requires = \
['ruamel.yaml>=0.17.20,<0.18.0']

setup_kwargs = {
    'name': 'valida',
    'version': '0.2.1',
    'description': 'Comprehensive validation library for nested data structures.',
    'long_description': '<img src="valida.png" width="200" alt="Valida logo"/>\n\n**Validation for nested data structures**\n\n[![PyPI version](https://img.shields.io/pypi/v/valida "PyPI version")](https://pypi.org/project/valida)\n![Testing workflow](https://github.com/hpcflow/valida/actions/workflows/test.yml/badge.svg)\n[![Supported python versions](https://img.shields.io/pypi/pyversions/valida "Supported python versions")](https://pypi.org/project/valida)\n[![License](https://img.shields.io/github/license/hpcflow/valida "License")](https://github.com/hpcflow/valida/blob/main/LICENSE)\n[![DOI](https://zenodo.org/badge/446597552.svg)](https://zenodo.org/badge/latestdoi/446597552)\n\n## Installing\n\n`pip install valida`\n\n## A simple example\n\n```python\nfrom valida import Data, Value, Rule\n\n# Define some data that we want to validate:\nmy_data = Data({\'A\': 1, \'B\': [1, 2, 3], \'C\': {\'c1\': 8.2, \'c2\': \'hello\'}})\n\n# Define a rule as a path within the data and a condition at that path:\nrule = Rule(\n  path=(\'C\', \'c2\'),\n  condition=Value.dtype.equal_to(str),\n)\n\n# Test the rule\nrule.test(my_data).is_valid # `True` => The rule tested successfully\n\n```\n\n## Acknowledgements\n\nValida was developed using funding from the [LightForm](https://lightform.org.uk/) EPSRC programme grant ([EP/R001715/1](https://gow.epsrc.ukri.org/NGBOViewGrant.aspx?GrantRef=EP/R001715/1))\n\n<img src="https://lightform-group.github.io/wiki/assets/images/site/lightform-logo.png" width="150"/>\n\n',
    'author': 'Adam J. Plowman',
    'author_email': 'adam.plowman@manchester.ac.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
