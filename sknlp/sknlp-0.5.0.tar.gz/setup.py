# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sknlp',
 'sknlp.activations',
 'sknlp.callbacks',
 'sknlp.data',
 'sknlp.layers',
 'sknlp.layers.utils',
 'sknlp.losses',
 'sknlp.metrics',
 'sknlp.module',
 'sknlp.module.classifiers',
 'sknlp.module.generators',
 'sknlp.module.retrievers',
 'sknlp.module.taggers',
 'sknlp.module.text2vec',
 'sknlp.optimizers',
 'sknlp.typing',
 'sknlp.utils',
 'sknlp.vocab']

package_data = \
{'': ['*']}

install_requires = \
['igraph>=0.9.8,<0.10.0',
 'jieba>=0.42.1,<0.43.0',
 'keras-tuner>=1.0.2,<2.0.0',
 'pandas==1.3.1',
 'scikit-learn==1.0',
 'tabulate==0.8.9',
 'tensorflow-addons==0.15.0',
 'tensorflow-text==2.7.3',
 'tensorflow==2.7.1']

setup_kwargs = {
    'name': 'sknlp',
    'version': '0.5.0',
    'description': '',
    'long_description': None,
    'author': 'nanaya',
    'author_email': 'nanaya100@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.5,<3.10',
}


setup(**setup_kwargs)
