# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['deploy_k8s_cli']

package_data = \
{'': ['*'],
 'deploy_k8s_cli': ['infrastructure/vagrant/*',
                    'infrastructure/vagrant/scripts/*']}

install_requires = \
['ansible-runner>=2.1.2,<3.0.0']

setup_kwargs = {
    'name': 'deploy-k8s-cli',
    'version': '0.1.0',
    'description': 'Command line interface to deploy a Kubernetes cluster on OpenStack',
    'long_description': None,
    'author': 'Alexis Janero Moliner',
    'author_email': 'ajanerom@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
