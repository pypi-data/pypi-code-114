# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['adform']

package_data = \
{'': ['*']}

install_requires = \
['azure-storage-blob>=12.8.0,<13.0.0', 'requests>=2.25.1,<3.0.0']

setup_kwargs = {
    'name': 'odap-adform-downloader',
    'version': '1.0.2',
    'description': 'DataSentics adform zip downloader',
    'long_description': '# DataSentics Python package for downloading adform data\n\n**This package is distributed under the "DataSentics SW packages Terms of Use." See [license](https://github.com/DataSentics/odap-ga-downloader/blob/main/LICENSE)**\n\n## Downloads data from adform in zip files\n\nYou need to specify:\n  * Credentials (name, setup_id, client_id, secret)\n  * Optionally you can specify scope, which data from Adform you would like to download, dates and file directory\n\n```bash\n$ pip install adform-downloader\n\nfrom adform.Client import Client, FilePersistingHandler\nfrom adform.Credentials import Credentials\n\nsetup_id = ""\nclient_id = ""\nclient_secret = ""\n\n# optionally can be added into credentials. Written with default values\nfile = "/tmp/" # for state file\nscopes = [\n        "https://api.adform.com/scope/buyer.masterdata",\n        "https://api.adform.com/scope/eapi",\n        "https://api.adform.com/scope/buyer.rtb.lineitem",\n    ]\ntables = ["Click", "Event", "Impression", "Trackingpoint", "meta"]\nstart_day=today-8days, # format dd-mm-yyyy\nend_day=today,\nlanding_file = "/tmp/" # for data, can be same as file\n\npersisting_handler = FilePersistingHandler(location=file)\ncredentials = Credentials(setup_id=setup_id, client_id=client_id, client_secret=client_secret)\nclient = Client(credentials, persisting_handler)\nclient.download_masterdata_files_by_id()\n```\n',
    'author': 'Pavla',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/DataSentics/odap-adform-downloader',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
