# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sigma', 'sigma.backends.splunk', 'sigma.pipelines.splunk']

package_data = \
{'': ['*']}

install_requires = \
['pysigma>=0.4.2,<0.5.0']

setup_kwargs = {
    'name': 'pysigma-backend-splunk',
    'version': '0.2.2',
    'description': 'pySigma Splunk backend',
    'long_description': None,
    'author': 'Thomas Patzke',
    'author_email': 'thomas@patzke.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
