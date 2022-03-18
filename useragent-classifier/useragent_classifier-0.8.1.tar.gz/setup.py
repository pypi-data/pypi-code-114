# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['useragent_classifier', 'useragent_classifier.custom_transformers']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.4,<9.0.0',
 'dash>=2.3.0,<3.0.0',
 'pandas>=1.4.1,<2.0.0',
 'plotly>=5.6.0,<6.0.0',
 'scikit-learn>=1.0.2,<2.0.0']

entry_points = \
{'console_scripts': ['useragent_classifier = '
                     'useragent_classifier:main.ua_clustering']}

setup_kwargs = {
    'name': 'useragent-classifier',
    'version': '0.8.1',
    'description': '',
    'long_description': '# Useragent_classifier\n\n## Installation \n\n```\npip install useragent_classifier\n```\n\n## Basic Usage\n\n### Text\n```\nuseragent_classifier -f /tmp/mylist_of_User_agent.csv\n```\n\nWhere mylist_of_User_agent.csv file is in the following format, one user agent by row, with no header\n|                                                                          |\n|--------------------------------------------------------------------------|\n| Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko     |\n| Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0 |\n| Opera/6.11 (Linux 2.4.18-bf2.4 i686; U)  [en]                            |\n\nIt will produce a two files:\n- a file with cluster number attributed to each User agent\n- a file usefull to explain cluster with the most important word or set of word in this cluster\n\n### Graphical analysis of cluster    \n\n```\nuseragent_classifier -f /tmp/mylist_of_User_agent.csv --graphical-explanation\n```\n\nLaunch a graphical analysis of cluster on local host on port 8050\n\n\n![](https://gitlab.com/thibaultB/image_user_agent_classifier/-/raw/main/example_dashboard.png?inline=false)\n\n\n## More advanced Usage\n\nTo display the help\n```\nuseragent_classifier --help\n```\n\n',
    'author': 'thibaultB',
    'author_email': 'thibault.blanc@yahoo.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
