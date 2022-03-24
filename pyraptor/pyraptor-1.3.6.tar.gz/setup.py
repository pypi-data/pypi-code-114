# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyraptor', 'pyraptor.dao', 'pyraptor.gtfs', 'pyraptor.model']

package_data = \
{'': ['*']}

install_requires = \
['joblib>=1.0.1,<2.0.0', 'loguru>=0.6.0,<0.7.0', 'pandas>=1.4.0,<2.0.0']

setup_kwargs = {
    'name': 'pyraptor',
    'version': '1.3.6',
    'description': 'Journey planner with RAPTOR algorithm',
    'long_description': '# PyRaptor\n\nPython implementation of RAPTOR and McRAPTOR using GTFS data. Tested on Dutch GTFS data.\n\nThis repository contains four applications:\n\n1. `pyraptor/gtfs/timetable.py` - Extract the timetable information for one operator from a GTFS dataset and write it to an optimized format for querying with RAPTOR.\n2. `pyraptor/query_raptor.py` - Get the best journey for a given origin, destination and desired departure time using RAPTOR\n3. `pyraptor/query_range_raptor.py` - Get a list of the best journeys to all destinations for a given origin and desired departure time window using RAPTOR\n4. `pyraptor/query_mcraptor.py` - Get a list of the Pareto-optimal journeys to all destinations for a given origin and a departure time using McRAPTOR\n5. `pyraptor/query_range_mcraptor.py` - Get a list of Pareto-optimal journeys to all destinations for a given origin and a departure time window using McRAPTOR\n\n## Installation\n\nInstall from PyPi using `pip install pyraptor` or clone this repository and install from source using pip.\n\n## Example usage\n\n### 1. Create timetable from GTFS\n\n> `python pyraptor/gtfs/timetable.py -d "20211201" -a NS --icd`\n\n### 2. Run (range) queries on timetable\n\nQuering on the timetable to get the best journeys can be done using several implementations.\n\n#### RAPTOR query\n\nRAPTOR returns a single journey with the earliest arrival time given the query time.\n\n**Examples**\n\n> `python pyraptor/query_raptor.py -or "Arnhem Zuid" -d "Oosterbeek" -t "08:30:00"`\n\n> `python pyraptor/query_raptor.py -or "Breda" -d "Amsterdam Centraal" -t "08:30:00"`\n\n#### rRAPTOR query\n\nrRAPTOR returns a set of best journeys with a given query time range.\nJourneys that are dominated by other journeys in the time range are removed.\n\n**Examples**\n \n> `python pyraptor/query_range_raptor.py -or "Arnhem Zuid" -d "Oosterbeek" -st "08:00:00" -et "08:30:00"`\n\n> `python pyraptor/query_range_raptor.py -or "Breda" -d "Amsterdam Centraal" -st "08:00:00" -et "08:30:00"`\n\n#### McRaptor query\n\nMcRaptor returns a set of Pareto-optimal journeys given multiple criterions, i.e. earliest \narrival time, fare and number of trips.\n\n**Examples**\n\n> `python pyraptor/query_mcraptor.py -or "Breda" -d "Amsterdam Centraal" -t "08:30:00"`\n\n> `python pyraptor/query_mcraptor.py -or "Vlissingen" -d "Akkrum" -t "08:30:00"`\n\n> `python pyraptor/query_mcraptor.py -or "Obdam" -d "Akkrum" -t "08:30:00" -r 7`\n\n#### rMcRaptor query\n\nRange version of McRaptor, i.e. it returns a set of Pareto-optimal journeys within a departure time window.\n\n**Examples**\n\n> `python pyraptor/query_range_mcraptor.py -or "Breda" -d "Amsterdam Centraal" -st "08:15:00" -et "08:30:00"`\n\n> `python pyraptor/query_range_mcraptor.py -or "Vlissingen" -d "Akkrum" -st "08:15:00" -et "08:30:00"`\n\n> `python pyraptor/query_range_mcraptor.py -or "Obdam" -d "Akkrum" -st "08:00:00" -et "09:00:00"`\n\n# Notes\n\n- The current version doesn\'t implement target pruning as we are interested in efficiently querying all targets/destinations after running RAPTOR algorithm.\n\n# References\n\n[Round-Based Public Transit Routing](https://www.microsoft.com/en-us/research/wp-content/uploads/2012/01/raptor_alenex.pdf), Microsoft.com, Daniel Delling et al\n\n[Raptor, another journey planning algorithm](https://ljn.io/posts/raptor-journey-planning-algorithm), Linus Norton\n\n[Dutch GTFS feed](http://transitfeeds.com/p/ov/814), Transit Feeds\n',
    'author': 'Leo van der Meulen, Thom Hopmans',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/lmeulen/pyraptor',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
