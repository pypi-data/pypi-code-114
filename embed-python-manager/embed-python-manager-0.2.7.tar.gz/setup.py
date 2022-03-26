# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['embed_python_manager']

package_data = \
{'': ['*'], 'embed_python_manager': ['source_list/*']}

install_requires = \
['lk-logger>=5.0.1,<6.0.0', 'lk-utils>=2.2.0,<3.0.0', 'pyyaml']

setup_kwargs = {
    'name': 'embed-python-manager',
    'version': '0.2.7',
    'description': 'Download and manage embedded python versions.',
    'long_description': "# Install\n\n```\npip install embed-python-manager\n```\n\n# Basic Usages\n\n```python\nfrom embed_python_manager import EmbedPythonManager\n\nmanager = EmbedPythonManager('python39')\n\n# Internet connection required.\nmanager.deploy(add_pip_suits=True, add_tk_suits=False)\n#   Now the embedded Python folder is ready to call, copy, move and more.\n\nmanager.copy_to(input('Target venv folder: '))\n# manager.move_to(input('Target venv folder: '))\n\n```\n\n# Advanced Usages\n\n*TODO*\n",
    'author': 'Likianta',
    'author_email': 'likianta@foxmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
