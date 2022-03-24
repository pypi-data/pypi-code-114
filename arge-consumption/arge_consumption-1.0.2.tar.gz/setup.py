# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['arge_consumption']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.9.0,<2.0.0', 'requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'arge-consumption',
    'version': '1.0.2',
    'description': 'Python Client zum Abruf unterjähriger Verbrauchsinformationen über die *ARGE consumption-data API*.',
    'long_description': '# ARGE Consumption Data Client\nPython Client zum Abruf unterjähriger Verbrauchsinformationen über die *ARGE consumption-data API*.\n\n## Hintergrund\n\nIm Rahmen der [EED](https://de.wikipedia.org/wiki/Richtlinie_2012/27/EU_(Energieeffizienz-Richtlinie)) veröffentlicht die [ARGE HeiWaKo](https://arge-heiwako.de/) einen Webservice mit dem monatliche Verbrauchsdaten auf Nutzeinheitenebene vom Wärmedienstunternehmen abgerufen werden können.\n\nDieser Service solle es der Wohnungswirtschaft ermöglichen, Nutzern/Bewohnern eine unterjährige Verbrauchsinformation im Rahmen der EED in eigenen IT-Systemen bereitzustellen.\n\nMehr Infos hier: [ARGE HEIWAKO: Datenaustausch](https://arge-heiwako.de/veroeffentlichungen/datenaustausch/)\n',
    'author': 'Moritz Duchêne',
    'author_email': '2857237+Debakel@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Debakel/arge-consumption',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
