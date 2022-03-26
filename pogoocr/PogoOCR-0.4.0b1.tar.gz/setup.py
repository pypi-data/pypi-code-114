# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['PogoOCR', 'PogoOCR.images', 'PogoOCR.providers']

package_data = \
{'': ['*']}

install_requires = \
['babel>=2.0.0',
 'colormath>=3.0.0,<4.0.0',
 'colour>=0.1.5,<0.2.0',
 'google-cloud-vision>=2.7.1,<3.0.0',
 'numpy>=1.22.0',
 'pillow>=8.3.2',
 'python-dateutil>=2.8.2,<3.0.0',
 'requests>=2.27.1,<3.0.0']

extras_require = \
{'aiohttp': ['aiohttp>=3.8.1,<4.0.0']}

setup_kwargs = {
    'name': 'pogoocr',
    'version': '0.4.0b1',
    'description': 'A Python tool for running OCR on Pokemon Go Screenshots',
    'long_description': '[![Support Server](https://img.shields.io/discord/614101299197378571.svg?color=7289da&label=Support&logo=discord&style=flat)](https://discord.gg/pdxh7P)\n[![PyPi version](https://badgen.net/pypi/v/PogoOCR/)](https://pypi.com/project/PogoOCR)\n[![Maintenance](https://img.shields.io/static/v1?label=Maintained?&message=yes&color=success&style=flat)](#)\n[![wakatime](https://wakatime.com/badge/github/TrainerDex/PogoOCR.svg?style=flat)](https://wakatime.com/badge/github/TrainerDex/PogoOCR)\n[![codecov](https://codecov.io/gh/TrainerDex/PogoOCR/branch/develop/graph/badge.svg?token=LABKE6I5RL)](https://codecov.io/gh/TrainerDex/PogoOCR)\n\nA Python tool for running OCR on Pokémon Screenshots using Google Cloud Vision\n\n\nUsage:\n\n```py\nimport PogoOCR\nfrom google.oauth2 import service_account\n\ncredentials: service_account.Credentials\n\nclient = PogoOCR.OCRClient(credentials=credentials)\nscreenshot = PogoOCR.Screenshot.from_url(\n    url="...",\n    klass=PogoOCR.ScreenshotClass.ACTIVITY_VIEW,\n)\n\nrequest = client.open_request(screenshot, PogoOCR.Language.ENGLISH)\n\nresult = client.process_ocr(request)\n```\n',
    'author': 'Jay Turner',
    'author_email': 'jay@trainerdex.app',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/TrainerDex/PogoOCR',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8.2,<3.11',
}


setup(**setup_kwargs)
