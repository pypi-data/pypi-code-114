# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['WatchUI', 'WatchUI.Ibasic', 'WatchUI.keywords']

package_data = \
{'': ['*']}

install_requires = \
['Pillow',
 'PyMuPDF',
 'imutils',
 'numpy',
 'opencv-python',
 'pandas',
 'pytesseract',
 'robotframework',
 'scikit-image',
 'scikit-learn']

entry_points = \
{'console_scripts': ['docs = tasks:docs', 'test = tasks:test']}

setup_kwargs = {
    'name': 'watchui',
    'version': '2.0.5',
    'description': 'RobotFramework library package for automated visual testing.',
    'long_description': '# WatchUI\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n## [Documentation](https://tesena-smart-testing.github.io/WatchUI/) | [Tesena](https://www.tesena.com/) | [Pypi](https://pypi.org/project/WatchUI/)\n\n## Important notice for users\n\nWatchUI 2.0 brings breaking changes. Dev team decided to streamline the library and focus it solely on the image and text comparison. This allows us to remove the implicit dependency on browser automation libraries - namely SeleniumLibrary, which was implicit part of the library via RF `BuiltIn()` import of the SeleniumLibrary instance.\n\nThis is no longer the case - user of the WatchUI therefore **can and have to choose, what UI automation library will use** and provide screenshots to the WatchUI keywords to be compared. It could be now used with SeleniumLibrary, Browser library, Sikuli, Appium or any other UI library where visual validation is required.\n\nVersion 1.x.x is no longer supported, but it is still available on [Pypi](pip install WatchUI==1.0.11).\n\n### Basic Info\n\nCustom library for works with image, pdf and tesseract with RF.\n\n### Folder structure\n\n```\nWatchUI\n└── .github/workflows           # Folder with CI for github actions\n└── assets                      # Folder with images used for documantation as well as test data\n└── test                        # Folder with example how to write rf test.\n│    └── unit_tests             # Pytest unit test cases\n│    └── test.robot             # File with simeple Robot Framework TCs\n└── WatchUI                     # Folder with WatchUI library\n│    └── WatchUI.py             # Main library file\n│    └── IBasics                # Basic utilities and error handling\n│    └── Keywords               # Keywords for working with images, PDFs and text(tesseract)\n└── README.MD                   # Here you are :-)\n└── setup.py                    # File for easy setup use with pip install .\n```\n\n### Install\n\nYou can find detail in [Documentation](https://procesor2017.github.io/WatchUI/) but basically use pip:\n\n```\npip install WatchUI\n```\n\nor some python dependencies management tools, like [pipenv](https://pipenv.pypa.io/en/latest/) or [poetry](https://python-poetry.org/) and their respective methods of libraries installation.\n\n### Sample results\n\n_Image where the differences are stored + You can see two black box in left corner. These black box are ignored during comparison._\n\n<img src="assets/example-ignore-areas.png">\n\n_The red rectangles outlining missing elements on compared screens_\n\n<img src="assets/example-difference.jpg">\n',
    'author': 'Jan Egermaier',
    'author_email': 'jan.egermaier@tesena.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Tesena-smart-testing/WatchUI',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
