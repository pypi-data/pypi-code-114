# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nlhappy',
 'nlhappy.callbacks',
 'nlhappy.configs',
 'nlhappy.datamodules',
 'nlhappy.layers',
 'nlhappy.layers.attention',
 'nlhappy.layers.classifier',
 'nlhappy.layers.embedding',
 'nlhappy.layers.loss',
 'nlhappy.layers.normalization',
 'nlhappy.metrics',
 'nlhappy.models',
 'nlhappy.models.sentence_pair_classification',
 'nlhappy.models.span_classification',
 'nlhappy.models.text_classification',
 'nlhappy.models.text_multi_classification',
 'nlhappy.models.token_classification',
 'nlhappy.models.triple_extraction',
 'nlhappy.preprocess',
 'nlhappy.spacy_components',
 'nlhappy.tricks',
 'nlhappy.utils']

package_data = \
{'': ['*'],
 'nlhappy.configs': ['callbacks/*',
                     'datamodule/*',
                     'experiment/*',
                     'hparams_search/*',
                     'logger/*',
                     'mode/*',
                     'model/*',
                     'trainer/*']}

install_requires = \
['datasets>=1.18.3,<2.0.0',
 'hydra-colorlog>=1.1.0,<2.0.0',
 'hydra-core>=1.1.1,<2.0.0',
 'jieba>=0.42.1,<0.43.0',
 'oss2>=2.15.0,<3.0.0',
 'pkuseg>=0.0.25,<0.0.26',
 'pytorch-lightning>=1.5.10,<2.0.0',
 'rich>=12.0.0,<13.0.0',
 'scikit-learn>=1.0.2,<2.0.0',
 'spacy>=3.2.2,<4.0.0',
 'torch>=1.10.2,<2.0.0',
 'tqdm>=4.63.0,<5.0.0',
 'transformers>=4.16.2,<5.0.0']

entry_points = \
{'console_scripts': ['nlhappy = nlhappy.run:train'],
 'spacy_factories': ['span_classifier = nlhappy.spacy_components:make_spancat']}

setup_kwargs = {
    'name': 'nlhappy',
    'version': '0.1.11',
    'description': '一款致力于SOTA的中文自然语言处理库',
    'long_description': None,
    'author': 'wangmengdi',
    'author_email': '790990241@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
