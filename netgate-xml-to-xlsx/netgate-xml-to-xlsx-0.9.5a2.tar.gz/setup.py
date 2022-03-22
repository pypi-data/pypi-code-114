# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['netgate_xml_to_xlsx']

package_data = \
{'': ['*']}

install_requires = \
['openpyxl>=3.0.9,<4.0.0', 'xmltodict>=0.12.0,<0.13.0']

entry_points = \
{'console_scripts': ['netgate-xml-to-xlsx = netgate_xml_to_xlsx.main:main']}

setup_kwargs = {
    'name': 'netgate-xml-to-xlsx',
    'version': '0.9.5a2',
    'description': 'Translate Netgate firewall rules to spreadsheet for review.',
    'long_description': "# Netgate Firewall Converter\n\nThe `netgate-xml-to-xlsx` converts a standard Netgate firewall .xml configuration file to an .xlsx spreadsheet with multiple tabs.\n\n* Supports Python 3.10+.\n* This is an alpha version tested on a limited number of firewall files.\n* The specific spreadsheet tabs implemented address our (ASI's) immediate firewall review needs.\n* Tested only on Netgate firewall version 21.x files.\n\n\n## Installation\nRecommend installing this in a virtual environment.\n\n```\npython -m pip install netgate-xml-to-xlsx\n```\n\nOnce installed, the `netgate-xml-to-xlsx` command is available on your path.\n\n## Usage\n\n### Help\n```\n# Display help\nnetgate-xml-to-xlsx --help\n```\n\n### Sanitize Before Use\nNetgate configuration files contains sensitive information.\nSanitize the files before processing.\nOnly sanitized files can be processed.\nThe original (unsanitized) file is deleted.\n\n```\n# Sanitize Netgate configuration file(s) for review.\nnetgate-xml-to-xlsx --sanitize firewall-config.xml\nnetgate-xml-to-xlsx --sanitize dir/*\n```\n\n### Convert to Spreadsheet\n* By default, output is sent to the `./output` directory.\n* Use the `--output-dir` parameter to set a specific output directory.\n* The output filename is based on the `hostname` and `domain` elements of the XML `system` element.\n* Only sanitized files can generate a spreadsheet output.\n\n```\n# Convert a Netgate firewall configuration file.\nnetgate-xml-to-xlsx firewall-config.xml\n\n# Convert all files in a directory.\nnetgate-xml-to-xlsx ../source/*-sanitized.xml\n```\n\n## Notes\n\n### Using flakeheaven\nThe large collection of flakeheaven plugins is a bit overboard while I continue to find the best mixture of plugins that work best for my projects.\n",
    'author': 'Raymond GA Côté',
    'author_email': 'ray@AppropriateSolutions.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/appropriate-solutions-inc/netgate-xml-to-xlsx',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
