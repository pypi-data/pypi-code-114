# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['niaarm', 'niaarm.tests']

package_data = \
{'': ['*'], 'niaarm.tests': ['test_data/*']}

install_requires = \
['niapy>=2.0.1,<3.0.0']

extras_require = \
{':python_version >= "3.11" and python_version < "4.0"': ['numpy>=1.22.3,<2.0.0'],
 ':python_version >= "3.7" and python_version < "3.11"': ['numpy>=1.21.5,<2.0.0'],
 ':python_version >= "3.7.1" and python_version < "3.8"': ['pandas>=1.3.5,<2.0.0'],
 ':python_version >= "3.8" and python_version < "4.0"': ['pandas>=1.4.0,<2.0.0'],
 'docs': ['Sphinx>=4.4.0,<5.0.0',
          'sphinx-rtd-theme>=1.0.0,<2.0.0',
          'sphinxcontrib-bibtex>=2.4.1,<3.0.0']}

entry_points = \
{'console_scripts': ['niaarm = niaarm.cli:main']}

setup_kwargs = {
    'name': 'niaarm',
    'version': '0.1.4',
    'description': 'A minimalistic framework for numerical association rule mining',
    'long_description': '<p align="center">\n  <img width="300" src="https://raw.githubusercontent.com/firefly-cpp/NiaARM/main/.github/logo/logo.png">\n</p>\n\n---\n\n# NiaARM - A minimalistic framework for numerical association rule mining\n\n---\n[![PyPI Version](https://img.shields.io/pypi/v/niaarm.svg)](https://pypi.python.org/pypi/niaarm)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/niaarm.svg)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/niaarm.svg)\n[![GitHub license](https://img.shields.io/github/license/firefly-cpp/niaarm.svg)](https://github.com/firefly-cpp/NiaARM/blob/main/LICENSE)\n![GitHub commit activity](https://img.shields.io/github/commit-activity/w/firefly-cpp/niaarm.svg)\n[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/firefly-cpp/niaarm.svg)](http://isitmaintained.com/project/firefly-cpp/niaarm "Average time to resolve an issue")\n\n## General outline of the framework\nNiaARM is a framework for Association Rule Mining based on nature-inspired algorithms for optimization. The framework is written fully in Python and runs on all platforms. NiaARM allows users to preprocess the data in a transaction database automatically, to search for association rules and provide a pretty output of the rules found. This framework also supports numerical and real-valued types of attributes besides the categorical ones. Mining the association rules is defined as an optimization problem, and solved using the nature-inspired algorithms that come from the related framework called [NiaPy](https://github.com/NiaOrg/NiaPy).\n\n## Detailed insights\nThe current version includes (but is not limited to) the following functions:\n\n- loading datasets in CSV format,\n- preprocessing of data,\n- searching for association rules,\n- providing output of mined association rules,\n- generating statistics about mined association rules.\n\n## Installation\n\n### pip\n\nInstall NiaARM with pip:\n\n```sh\npip install niaarm\n```\n\nTo install NiaARM on Alpine Linux, please enable Testing repository and use:\n\n```sh\n$ apk add py3-niaarm\n```\n\n## Usage\n\n### Basic example\n\nIn this example we\'ll use Differential Evolution to mine association rules on the Abalone Dataset.\n\n```python\nfrom niaarm import NiaARM, Dataset\nfrom niapy.algorithms.basic import DifferentialEvolution\nfrom niapy.task import Task, OptimizationType\n\n\n# load and preprocess the dataset from csv\ndata = Dataset("datasets/Abalone.csv")\n\n# Create a problem:::\n# dimension represents the dimension of the problem;\n# features represent the list of features, while transactions depicts the list of transactions\n# metrics is a sequence of metrics to be taken into account when computing the fitness;\n# you can also pass in a dict of the shape {\'metric_name\': <weight of metric in range [0, 1]>};\n# when passing a sequence, the weights default to 1.\nproblem = NiaARM(data.dimension, data.features, data.transactions, metrics=(\'support\', \'confidence\'), logging=True)\n\n# build niapy task\ntask = Task(problem=problem, max_iters=30, optimization_type=OptimizationType.MAXIMIZATION)\n\n# use Differential Evolution (DE) algorithm from the NiaPy library\n# see full list of available algorithms: https://github.com/NiaOrg/NiaPy/blob/master/Algorithms.md\nalgo = DifferentialEvolution(population_size=50, differential_weight=0.5, crossover_probability=0.9)\n\n# run algorithm\nbest = algo.run(task=task)\n\n# sort rules\nproblem.rules.sort()\n\n# export all rules to csv\nproblem.rules.to_csv(\'output.csv\')\n```\n\n#### Simplified\n\nThe above example can be further simplified with the use of ``niaarm.mine.get_rules()``:\n\n```python\n\nfrom niaarm import Dataset, get_rules\nfrom niapy.algorithms.basic import DifferentialEvolution\n\n\ndata = Dataset("datasets/Abalone.csv")\nalgo = DifferentialEvolution(population_size=50, differential_weight=0.5, crossover_probability=0.9)\nmetrics = (\'support\', \'confidence\')\n\nrules, run_time = get_rules(data, algo, metrics, max_iters=30, logging=True)\n\nprint(rules)\nprint(f\'Run Time: {run_time}\')\nrules.to_csv(\'output.csv\')\n\n```\n\nFor a full list of examples see the [examples folder](examples/).\n\n### Command line interface\n\nWe provide a simple command line interface, which allows you to easily\nmine association rules on any input dataset, output them to a csv file and/or perform\na simple statistical analysis on them.\n\n```shell\nniaarm -h\n```\n\n```\nusage: niaarm [-h] [-v] -i INPUT_FILE [-o OUTPUT_FILE] -a ALGORITHM [-s SEED]\n              [--max-evals MAX_EVALS] [--max-iters MAX_ITERS] --metrics\n              METRICS [METRICS ...] [--weights WEIGHTS [WEIGHTS ...]] [--log]\n              [--show-stats]\n\nPerform ARM, output mined rules as csv, get mined rules\' statistics\n\noptions:\n  -h, --help            show this help message and exit\n  -v, --version         show program\'s version number and exit\n  -i INPUT_FILE, --input-file INPUT_FILE\n                        Input file containing a csv dataset\n  -o OUTPUT_FILE, --output-file OUTPUT_FILE\n                        Output file for mined rules\n  -a ALGORITHM, --algorithm ALGORITHM\n                        Algorithm to use (niapy class name, e.g.\n                        DifferentialEvolution)\n  -s SEED, --seed SEED  Seed for the algorithm\'s random number generator\n  --max-evals MAX_EVALS\n                        Maximum number of fitness function evaluations\n  --max-iters MAX_ITERS\n                        Maximum number of iterations\n  --metrics METRICS [METRICS ...]\n                        Metrics to use in the fitness function.\n  --weights WEIGHTS [WEIGHTS ...]\n                        Weights in range [0, 1] corresponding to --metrics\n  --log                 Enable logging of fitness improvements\n  --show-stats          Display stats about mined rules\n```\nNote: The CLI script can also run as a python module (`python -m niaarm ...`)\n\n## Reference Papers:\n\nIdeas are based on the following research papers:\n\n[1] I. Fister Jr., A. Iglesias, A. Gálvez, J. Del Ser, E. Osaba, I Fister. [Differential evolution for association rule mining using categorical and numerical attributes](http://www.iztok-jr-fister.eu/static/publications/231.pdf) In: Intelligent data engineering and automated learning - IDEAL 2018, pp. 79-88, 2018.\n\n[2] I. Fister Jr., V. Podgorelec, I. Fister. [Improved Nature-Inspired Algorithms for Numeric Association Rule Mining](https://link.springer.com/chapter/10.1007/978-3-030-68154-8_19). In: Vasant P., Zelinka I., Weber GW. (eds) Intelligent Computing and Optimization. ICO 2020. Advances in Intelligent Systems and Computing, vol 1324. Springer, Cham.\n\n[3] I. Fister Jr., I. Fister [A brief overview of swarm intelligence-based algorithms for numerical association rule mining](https://arxiv.org/abs/2010.15524). arXiv preprint arXiv:2010.15524 (2020).\n\n## License\n\nThis package is distributed under the MIT License. This license can be found online at <http://www.opensource.org/licenses/MIT>.\n\n## Disclaimer\n\nThis framework is provided as-is, and there are no guarantees that it fits your purposes or that it is bug-free. Use it at your own risk!\n',
    'author': 'Žiga Stupan',
    'author_email': 'ziga.stupan1@student.um.si',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
