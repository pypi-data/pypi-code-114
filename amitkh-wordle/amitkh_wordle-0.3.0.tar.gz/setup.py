# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['amitkh_wordle']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.22.3,<2.0.0',
 'scipy>=1.8.0,<2.0.0',
 'tqdm>=4.63.0,<5.0.0',
 'typer>=0.4.0,<0.5.0',
 'wordfreq>=3.0.0,<4.0.0']

entry_points = \
{'console_scripts': ['wordle = amitkh_wordle.wordle:app']}

setup_kwargs = {
    'name': 'amitkh-wordle',
    'version': '0.3.0',
    'description': 'Entropy based Wordle Solver (CLI). Inspired by 3 Blue 1 Brown',
    'long_description': '## Entropy based Wordle solver\n\nCLI built with Typer. Based on [this](https://www.youtube.com/watch?v=v68zYyaEmEA) video from 3 Blue 1 Brown\n\n\n\n## Installation\n```\npip install amitkh-wordle\n```\n## Quick Start\n1. The solver needs to generate a pattern dictionary containing all of the word and pattern combinations in order to run. To do this, run `wordle gen-pattern-dict`. This process will take around 10-15 minutes.\n    1. By default the dictionary will be compressed using bz2 to about 200 MB. You can also specify the `--no-compress` option which will save the pickle without compression and will result in quicker load times, but take about 800 MB of storage .\n2. To run the solver in interactive mode, run `wordle play`. This will be followed by roughly 2 minutes of setup time while the program loads in the pattern dictionary and calculates the initial guess.\n    1. For maximum speed, you can also add the `-s` flag, which runs the solver in time saving mode. This means instead of spending 1 minute or so calculating the first guess, which is always "tares", it simply assumes this to be the first guess and allows you to enter your pattern from "tares" straight away. \n3. After this, you will be presented with some information and prompted for a guess. The program will present you the top 10 guesses (though you can guess any word you would like), along with (from left to right) the expected score should you play that guess, the expected information that guess will provide in bits, and the probability that guess is the answer.\n    1. If there are under 20 words remaining, the program will also print out those remaining words along with the probability that they are a potential answer based on frequency (which is not the same as the probability that they are the answer to this game).\n4. From there, simply type in your guesses and the pattern that was returned to you according to the instructions, and repeat until solved.\n\n## Other Functions\n1. `wordle play-words`\n    1. This command allows you to pass in a word or list of words to be played by the solver, like so `wordle play-words snake cater abyss`\n2. `wordle test-all`\n    1. This command runs the wordle solver on all of the 2,315 answers to the additional wordle, tracking the number of guesses taken for each, and writing them as a JSON to the file name given as an argument\n3. `wordle --help`\n    1. Display a brief help message\n\n',
    'author': 'Amit Kumar',
    'author_email': 'amitkh@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/amit-kumarh/wordle-solver',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
