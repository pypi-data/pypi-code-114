# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ranzen',
 'ranzen.hydra',
 'ranzen.pl',
 'ranzen.torch',
 'ranzen.torch.optimizers',
 'ranzen.torch.transforms']

package_data = \
{'': ['*']}

extras_require = \
{'all': ['pytorch-lightning>=1.4.2,<2.0.0',
         'hydra-core>=1.1.0,<2.0.0',
         'neoconfigen>=2.0.0,<3.0.0',
         'pandas>=1.3.1,<2.0.0',
         'wandb>=0.12.0,<0.13.0'],
 'hydra': ['hydra-core>=1.1.0,<2.0.0', 'neoconfigen>=2.0.0,<3.0.0'],
 'pl': ['pytorch-lightning>=1.4.2,<2.0.0', 'tqdm>=4.62.0,<5.0.0'],
 'torch': ['torch>=1.8,<2.0', 'numpy>=1.20.3,<2.0.0'],
 'wandb': ['pandas>=1.3.1,<2.0.0', 'wandb>=0.12.0,<0.13.0']}

setup_kwargs = {
    'name': 'ranzen',
    'version': '1.2.1',
    'description': 'A toolkit facilitating machine-learning experimentation.',
    'long_description': '# ranzen 🎒\n\nA python toolkit facilitating machine-learning experimentation.\n\n[Documentation](https://wearepal.github.io/ranzen/)\n\n## Install\n\nRun\n```\npip install ranzen\n```\n\nor install directly from GitHub:\n```\npip install git+https://github.com/predictive-analytics-lab/ranzen.git@main\n```\n',
    'author': 'PAL',
    'author_email': 'info@predictive-analytics-lab.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/predictive-analytics-lab/ranzen',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
