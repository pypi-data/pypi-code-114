# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['gibbs_sampler']

package_data = \
{'': ['*']}

install_requires = \
['bio>=1.3.3,<2.0.0', 'numpy>=1.22.3,<2.0.0', 'weblogo>=3.7.9,<4.0.0']

entry_points = \
{'console_scripts': ['gibbs_sampler = gibbs_sampler.gibbs_sampler:main']}

setup_kwargs = {
    'name': 'gibbs-sampler',
    'version': '0.2.0',
    'description': 'Gibbs Sampler for motif discovery',
    'long_description': '## Gibbs_Sampler\n\nThis program runs the Gibbs Sampler algorithm for\nde novo motif discovery. Given a set of sequences, the program\nwill calculate the most likely motif instance as well as \nthe position weight matrix and position specific scoring matrix\n(the log2 normalized frequency scores).\n\nThe input sequence file should be provided in fasta format. Output is written to the console. \nA eps file containing the weblogo of the motif is also created.\n#Getting Started\n##Prerequisites\nPython 3.8 or later is required.\n##Installation\nThe program can be installed with pip by running the following command:\n```bash\n$ pip install gibbs_sampler\n```\n\n## Usage\n\nTo run, simply call gibbs_sampler from the command line along with \nthe path to the sequence file and expected width of the motif.\n\n````bash\n$ gibbs_sampler <primary sequence file> <width>\n````\nOptional arguments for the title of the weblogo file and number of \niterations of the sampler can be specified using the -t and -n flags respectively.\n\n## License\n\n`gibbs_sampler` was created by Monty Python. It is licensed under the terms of the CC0 v1.0 Universal license.\n\n## Credits\nThank you to Professor Hendrix for teaching me how to use python to investigate biologically relevant questions.\n',
    'author': 'Monty Python',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
