# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['storage_bucket']

package_data = \
{'': ['*']}

install_requires = \
['google-cloud-storage>=1.42.3,<2.0.0']

setup_kwargs = {
    'name': 'storage-bucket',
    'version': '3.0.0',
    'description': 'Easy to work with Google Cloud Platform Storage Bucket wrapper',
    'long_description': "# Storage Bucket\n\nMakes working with GCP Storage bucket a breeze\n\n___\n![test](https://github.com/thomasborgen/storage-bucket/workflows/test/badge.svg)\n[![codecov](https://codecov.io/gh/thomasborgen/storage-bucket/branch/master/graph/badge.svg)](https://codecov.io/gh/thomasborgen/storage-bucket)\n[![Python Version](https://img.shields.io/pypi/pyversions/storage-bucket.svg)](https://pypi.org/project/storage-bucket/)\n[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)\n___\n\n**[Documentation](https://thomasborgen.github.io/storage-bucket/) |\n[Source Code](https://github.com/thomasborgen/storage-bucket) |\n[Issue Tracker](https://github.com/thomasborgen/storage-bucket/issues)**\n\nThe goal of this package is to make it easy to work with GCP Storage Bucket. We felt that using googles package(google-cloud-storage) was a horrible experience and we believe that this package abstracts away the object oriented approach taken by google and introduces a more functional approach.\n\n## Quickstart\n\nGet the package\n```sh\npip install storage-bucket\n```\n\nOr better with `poetry`\n```sh\npoetry add storage-bucket\n```\n\nDownload your keyfile and save it as key.json and point to it with env var:\n\n```sh\ngcloud iam service-accounts keys create key.json --iam-account your_service_account@your_project.iam.gserviceaccount.com\n```\n\n```sh\nexport GOOGLE_APPLICATION_CREDENTIALS='key.json'\n```\n\n\n### Download\n```python\nfrom storage_bucket import download_file\n\nfile_data = download_file('bucket', 'filename')\n\nprint(file_data)\n```\n\n### Upload\n```python\nfrom storage_bucket import upload_file\n\nupload_file(b'data', 'bucket_name', 'filename')\n```\n\n### Supported operations - File\n\n`Download`, `Upload`, `List`, `Delete`\n\n### Supported operations - Bucket\n\n`Create`, `Delete`, `List`\n\n### Check [Usage](https://thomasborgen.github.io/storage-bucket/usage).\n\n## Contribution\n\nLike the library and want to help us, check: [contributing](https://thomasborgen.github.io/storage-bucket/contrib/contributing/)\n",
    'author': 'Thomas Borgen',
    'author_email': 'thomas@borgenit.no',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/thomasborgen/storage-bucket',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
