# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bibchk']

package_data = \
{'': ['*']}

install_requires = \
['argparse>=1.4.0,<2.0.0', 'habanero>=1.0.0,<2.0.0', 'isbnlib>=3.10.10,<4.0.0']

setup_kwargs = {
    'name': 'bibchk',
    'version': '0.1.0',
    'description': 'Simple command line program to return the BibTeX string of a given DOI or ISBN.',
    'long_description': '# bibchk\n\nSimple program to return the BibTeX string of a given DOI(s) or ISBN(s).\n\nAn example with a DOI and DOI URL:\n\n```bash\n$ bibchk 10.1002/2016JC011857 https://doi.org/10.1002/2016JC011857\n@article{Houpert_2016,\n\tdoi = {10.1002/2016jc011857},\n\turl = {https://doi.org/10.1002%2F2016jc011857},\n\tyear = 2016,\n\tmonth = {nov},\n\tpublisher = {American Geophysical Union ({AGU})},\n\tvolume = {121},\n\tnumber = {11},\n\tpages = {8139--8171},\n\tauthor = {L. Houpert and X. Durrieu de Madron and P. Testor and A. Bosse and F. D{\\textquotesingle}Ortenzio and M. N. Bouin and D. Dausse and H. Le Goff and S. Kunesch and M. Labaste and L. Coppola and L. Mortier and P. Raimbault},\n\ttitle = {Observations of open-ocean deep convection in the northwestern Mediterranean Sea: Seasonal and interannual variability of mixing and deep water masses for the 2007-2013 Period},\n\tjournal = {Journal of Geophysical Research: Oceans}\n}\n\n@article{Houpert_2016,\n\tdoi = {10.1002/2016jc011857},\n\turl = {https://doi.org/10.1002%2F2016jc011857},\n\tyear = 2016,\n\tmonth = {nov},\n\tpublisher = {American Geophysical Union ({AGU})},\n\tvolume = {121},\n\tnumber = {11},\n\tpages = {8139--8171},\n\tauthor = {L. Houpert and X. Durrieu de Madron and P. Testor and A. Bosse and F. D{\\textquotesingle}Ortenzio and M. N. Bouin and D. Dausse and H. Le Goff and S. Kunesch and M. Labaste and L. Coppola and L. Mortier and P. Raimbault},\n\ttitle = {Observations of open-ocean deep convection in the northwestern Mediterranean Sea: Seasonal and interannual variability of mixing and deep water masses for the 2007-2013 Period},\n\tjournal = {Journal of Geophysical Research: Oceans}\n}\n```\n\nor with an ISBN:\n\n```bash\n$ bibchk 0-486-60061-0\n@book{9780486600611,\n     title = {Fundamentals Of Astrodynamics},\n    author = {Roger R. Bate and Donald D. Mueller and Jerry E. White},\n      isbn = {9780486600611},\n      year = {1971},\n publisher = {Courier Corporation}\n}\n```\n',
    'author': 'Doug Keller',
    'author_email': 'dg.kllr.jr@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/BibTheque/bibchk.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
