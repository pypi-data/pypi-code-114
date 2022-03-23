# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hl7000']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.4.1,<2.0.0']

setup_kwargs = {
    'name': 'hl7000',
    'version': '0.1.0',
    'description': 'Processing toolkit for Seba HL7000',
    'long_description': "# HL7000\n\nThis library is made to help consolidate measurements from the SebaKMT HL7000 acoustic logger.\n\nThe goal is to centralize the data into measurement folders, provide an index for your measurement folders and to prevent duplicate records being saved.\n\n## Install\n\n    pip install HL7000\n\n## Usage\n\nThe format will be a single depth folder structure, in which each folder name will be a uuid to prevent collision.\n\nAn index file will be created after saving a measurement, and can be rebuilt/saved using `save_index()`\n\nAll files will be copied from the source folder (likely off the HL7000) to the target folder when saving.\n\n\n### Single Measurement usage\n\nTo read and process a single measurement\n\n```\nfrom HL7000 import Measurement\n\nmeasurement = Measurement('/path/to/measurement')\n\n# view dataframe\nmeasurement.data\n\n#save to folder\nmeasurement.save_measurement('/path/to/save/folder')\n```\n\n### Multiple Measurement usage\n\nTo save multiple items, simply pass the source folder and target folders\n\n```\nfrom HL7000 import load_folder\n\nload_folder('/path/to/source/folder', '/path/to/target/folder')\n```\n\n### Rebuilding index\n\nIndex can be rebuilt for a folder if any error or deletion occurs\n\n```\nfrom HL7000 import save_index\n\nsave_index('/path/to/folder')\n```\n\n### Import Folder from command line\n\n```\npython -m HL7000 /path/to/source/folder /path/to/target/folder\n```\n\n\n## Future Plans\n\n* Companion GIS library for processing GIS data\n* Visulization Components\n    * FFT of each measurements\n    * Time series of each measurement\n    * Overlays of multiple measurements\n",
    'author': 'Cody Scott',
    'author_email': 'jcodyscott@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
