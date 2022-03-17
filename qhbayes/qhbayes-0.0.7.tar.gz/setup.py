# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qhbayes',
 'qhbayes.app',
 'qhbayes.data',
 'qhbayes.gp',
 'qhbayes.stats',
 'qhbayes.utilities']

package_data = \
{'': ['*'],
 'qhbayes': ['QHBayes.egg-info/*', 'qhbayes.egg-info/*'],
 'qhbayes.app': ['assets/*']}

install_requires = \
['Pint>=0.18,<0.19',
 'argparse>=1.4.0,<2.0.0',
 'arviz>=0.11.4,<0.12.0',
 'dash-bootstrap-components>=1.0.3,<2.0.0',
 'dash-extensions>=0.0.71,<0.0.72',
 'dash>=2.3.0,<3.0.0',
 'matplotlib>=3.5.1,<4.0.0',
 'numpy>=1.15.0,<1.22.2',
 'odfpy>=1.4.1,<2.0.0',
 'openpyxl>=3.0.9,<4.0.0',
 'pandas>=1.4.1,<2.0.0',
 'plotly>=5.6.0,<6.0.0',
 'pymc3>=3.11.5,<4.0.0',
 'scipy>=1.7.3,<1.8.0',
 'seaborn>=0.11.2,<0.12.0',
 'setuptools>=60.10.0,<61.0.0']

setup_kwargs = {
    'name': 'qhbayes',
    'version': '0.0.7',
    'description': 'Bayesian methods for inferring mass eruption rate for column height (or vice versa) for volcanic eruptions',
    'long_description': None,
    'author': 'markwoodhouse',
    'author_email': 'mark.woodhouse@bristol.ac.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
