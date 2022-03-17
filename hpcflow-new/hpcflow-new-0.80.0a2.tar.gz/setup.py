# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hpcflow', 'hpcflow.data']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.4,<9.0.0',
 'ruamel.yaml>=0.17.20,<0.18.0',
 'valida>=0.2.0,<0.3.0',
 'zarr>=2.10.3,<3.0.0']

extras_require = \
{'pyinstaller': ['pyinstaller>=4.10,<5.0']}

entry_points = \
{'console_scripts': ['hpcflow = hpcflow.cli:cli']}

setup_kwargs = {
    'name': 'hpcflow-new',
    'version': '0.80.0a2',
    'description': 'Computational workflow management',
    'long_description': '<img src="docs/source/_static/images/logo-v2.png" width="250" alt="hpcFlow logo"/>\n\n**hpcFlow manages your scientific workflows**\n\nDocumentation: [https://hpcflow.github.io/docs](https://hpcflow.github.io/docs)\n\n## Acknowledgements\n\n\nhpcFlow was developed using funding from the [LightForm](https://lightform.org.uk/) EPSRC programme grant ([EP/R001715/1](https://gow.epsrc.ukri.org/NGBOViewGrant.aspx?GrantRef=EP/R001715/1))\n\n<img src="https://lightform-group.github.io/wiki/assets/images/site/lightform-logo.png" width="150"/>\n',
    'author': 'aplowman',
    'author_email': 'adam.plowman@manchester.ac.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
