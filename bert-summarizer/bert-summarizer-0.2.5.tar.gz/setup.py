# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['bert_summarizer',
 'bert_summarizer.config',
 'bert_summarizer.data',
 'bert_summarizer.data.datasets',
 'bert_summarizer.models',
 'bert_summarizer.models.bertsum',
 'bert_summarizer.models.bertsum.abs',
 'bert_summarizer.tokenizers',
 'bert_summarizer.trainers',
 'bert_summarizer.utils']

package_data = \
{'': ['*']}

install_requires = \
['ginza>=4.0.5,<5.0.0', 'transformers[torch,ja]>=4.0.0']

extras_require = \
{'onmt': ['OpenNMT-py>=2.0.1']}

setup_kwargs = {
    'name': 'bert-summarizer',
    'version': '0.2.5',
    'description': 'Text Summarization Library based on transformers',
    'long_description': '**BERT-based text summarizers**\n\n[![Python Versions](https://img.shields.io/pypi/pyversions/bert-summarizer.svg)](https://pypi.org/project/bert-summarizer/)\n[![](https://img.shields.io/pypi/v/bert-summarizer)](https://pypi.org/project/bert-summarizer/)\n![](https://img.shields.io/pypi/l/bert-summarizer)\n[![Test](https://github.com/k-tahiro/bert-summarizer/actions/workflows/python-package.yml/badge.svg)](https://github.com/k-tahiro/bert-summarizer/actions/workflows/python-package.yml)\n[![codecov](https://codecov.io/gh/k-tahiro/bert-summarizer/branch/main/graph/badge.svg)](https://codecov.io/gh/k-tahiro/bert-summarizer)\n\n## Table of Contents\n\n- [Table of Contents](#table-of-contents)\n- [About the Project](#about-the-project)\n- [Getting started](#getting-started)\n- [Usage](#usage)\n- [Roadmap](#roadmap)\n- [Contributing](#contributing)\n- [License](#license)\n- [Contact](#contact)\n- [Acknowledgements](#acknowledgements)\n\n## About the Project\n\n- This repository will provide various summarization models using BERT.\n\n## Getting started\n\nTBW\n\n## Usage\n\nTBW\n\n## Roadmap\n\n- BertSumExt\n\n## Contributing\n\nTBW\n\n## License\n\nDistributed under the MIT License. See `LICENSE` for more information.\n\n## Contact\n\nKeisuke Hirota - [@rad0717](https://twitter.com/rad0717) - tahiro.k.ad[at]gmail.com\n\nProject Link: [https://github.com/k-tahiro/bert-summarizer](https://github.com/k-tahiro/bert-summarizer)\n\n## Acknowledgements\n\n- EMNLP 2019 paper [Text Summarization with Pretrained Encoders](https://arxiv.org/abs/1908.08345)\n  - [nlpyang/PreSumm](https://github.com/nlpyang/PreSumm)\n',
    'author': 'k-tahiro',
    'author_email': 'tahiro.k.ad@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/k-tahiro/bert-summarizer',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.2,<3.9',
}


setup(**setup_kwargs)
