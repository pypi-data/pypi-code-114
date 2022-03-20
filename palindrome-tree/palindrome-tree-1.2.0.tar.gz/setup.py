# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['palindrome_tree']

package_data = \
{'': ['*'], 'palindrome_tree': ['model/*']}

install_requires = \
['pandas>=1.3.5,<2.0.0',
 'requests>=2.26.0,<3.0.0',
 'scikit-learn>=1.0.2,<2.0.0',
 'xgboost>=1.5.1,<2.0.0']

setup_kwargs = {
    'name': 'palindrome-tree',
    'version': '1.2.0',
    'description': 'Gradient boosted decision tree palindrome predictor, used to locate regions for further investigation thru http://palindromes.ibp.cz/',
    'long_description': '# Palindrome tree\n\nPalindrome tree tool is used for analyzing inverted repeats in various DNA sequences using decision trees. This tool takes provided sequences and finds interesting parts in which there\'s high probability of palindrome occurrence using decision tree. This process filters a big portion of data. Interesting data are then analyzed using API from [Palindrome Analyzer](http://dx.doi.org/10.1016/j.bbrc.2016.09.015). DNA Analyser is a web-based server for nucleotide sequence analysis. It has been developed thanks to cooperation of Department of Informatics, Mendel’s University in Brno and Institute of Biophysics, Academy of Sciences of the Czech Republic. \n\n## Requirements\n\nPalindrome tree was built with Python 3.7+.\n\n## Installation\n\nTo install palindrome tree use [Pypi](https://pypi.org/project/palindrome-tree/) repository.\n\n```commandline\npip install palindrome-tree\n```\n\n## Usage\n\nUser has to initialize palindrome tree analyzer instance which is imported from main package `palindrome_tree`.\n\n```python\nfrom palindrome_tree import PalindromeTree\n\ntree = PalindromeTree()\n```\n\n### Predict regions (without API validation)\n\nTo predict regions with possible palindromes, run analyse without setting `check_with_api` paramether. \n\n```python\nsequence_file = open("/path/to/sequence/name.txt", "r")\n\nresults = tree.analyse(\n    sequence=sequence_file.read(),\n    check_with_api=False,\n)\n```\nThe results are then stored in results variable as `pd.DataFrame`. \n\n|    |   position | sequence                       |\n|---:|-----------:|:-------------------------------|\n|  0 |          8 | TTTGTAGAGACAGGGTCTTGCTGTGTTTCC |\n|  1 |         10 | TGTAGAGACAGGGTCTTGCTGTGTTTCCCA |\n|  2 |         49 | CGAACTCCTGGCCTCTAGGCAATCCTCCCA |\n|  3 |        102 | ATCCCACTCTTTTTTGAAAAATAAAATCTA |\n|  4 |        105 | CCACTCTTTTTTGAAAAATAAAATCTACCA |\n\n### Predict regions (with API validation)\n\nTo predict regions with possible palindromes and afterward validation, run analyse with `check_with_api` paramether set. \n\n```python\nsequence_file = open("/path/to/sequence/name.txt", "r")\n\nresults = tree.analyse(\n    sequence=sequence_file.read(),\n    check_with_api=True,\n)\n```\nThe results are also stored in results variable as `pd.DataFrame`. \n\n|    |   original_index | after   | before   |   mismatches | opposite   |   position | sequence   | signature   | spacer   | stability_NNModel                                                                |\n|---:|-----------------:|:--------|:---------|-------------:|:-----------|-----------:|:-----------|:------------|:---------|:---------------------------------------------------------------------------------|\n|  0 |                0 | CC      | TTTGT    |            2 | CTGTGTTT   |          5 | AGAGACAG   | 8-7-2       | GGTCTTG  | {\'cruciform\': -5.74, \'linear\': -27.590000000000003, \'delta\': 21.85}              |\n|  1 |                0 | TGCTG   | TTTGT    |            2 | GGGTCT     |          5 | AGAGAC     | 6-1-2       | A        | {\'cruciform\': -2.54, \'linear\': -13.84, \'delta\': 11.3}                            |\n|  2 |                0 | GTGTT   | TGTAG    |            2 | CTTGCT     |          7 | AGACAG     | 6-3-2       | GGT      | {\'cruciform\': -1.94, \'linear\': -17.509999999999998, \'delta\': 15.569999999999999} |\n|  3 |                0 | TTCC    | TAGAG    |            2 | CTGTGT     |          9 | ACAGGG     | 6-5-2       | TCTTG    | {\'cruciform\': -3.7399999999999998, \'linear\': -20.99, \'delta\': 17.25}             |\n|  4 |                1 | CCCA    | TGT      |            2 | CTGTGTTT   |          3 | AGAGACAG   | 8-7-2       | GGTCTTG  | {\'cruciform\': -5.74, \'linear\': -27.590000000000003, \'delta\': 21.85}              |\n\n## Dependencies\n\n* xgboost = "^1.5.1"\n* pandas = "^1.3.5"\n* scikit-learn = "^1.0.2"\n* requests = "^2.26.0"\n\n## Authors\n\n* **Patrik Kaura** - *Main developer* - [patrikkaura](https://gitlab.com/PatrikKaura/)\n\n* **Jaromir Kratochvil** - *Developer* - [jaromirkratochvil](https://github.com/kratjar)\n\n* **Jiří Šťastný** - *Supervisor*\n\n## License\n\nThis project is licensed under the MIT License - see the [\nLICENSE\n](\nLICENSE\n) file for details. \n\n',
    'author': 'jaromir.kratochvil',
    'author_email': '171433@vutbr.cz',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/patrikkaura/palindrome-tree',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
