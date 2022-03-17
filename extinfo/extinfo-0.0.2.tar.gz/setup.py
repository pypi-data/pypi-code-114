# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['extinfo', 'extinfo.extractors']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.10.0,<5.0.0',
 'click>=8.0.3,<9.0.0',
 'deal>=4.19.1,<5.0.0',
 'requests>=2.27.1,<3.0.0']

entry_points = \
{'console_scripts': ['extinfo = extinfo.cli:cli']}

setup_kwargs = {
    'name': 'extinfo',
    'version': '0.0.2',
    'description': 'Scrape information about file extensions from web sources',
    'long_description': "extinfo\n======================\n|LANGUAGE| |VERSION| |LICENSE| |MAINTAINED| |STYLE|\n\n.. |LICENSE| image:: https://img.shields.io/badge/license-Apache%202.0-informational\n   :target: https://www.apache.org/licenses/LICENSE-2.0.txt\n.. |MAINTAINED| image:: https://img.shields.io/maintenance/yes/2022?logoColor=informational\n.. |VERSION| image:: https://img.shields.io/pypi/v/extinfo\n   :target: https://pypi.org/project/extinfo\n.. |STYLE| image:: https://img.shields.io/badge/code%20style-black-000000.svg\n   :target: https://github.com/psf/black\n.. |LANGUAGE| image:: https://img.shields.io/pypi/pyversions/extinfo\n\nGiven a file extension, extinfo will scrape web sources for information about\nwhat type of file is usually named with that extension.\n\nIf you want to know what's in an actual file you have on disk, you should use\nthe file command or another tool that leverages libmagic.\n\nInstallation\n------------\n\n.. code-block :: console\n\n    pip3 install extinfo\n\nUsage\n-----\n\n.. code-block :: console\n\n    $ extinfo jpeg | fmt\n    From https://fileinfo.com/extension/jpeg\n\n    # JPEG Image\n\n    A JPEG file is an image saved in a compressed graphic format standardized\n    by the Joint Photographic Experts Group (JPEG). It supports up to 24-bit\n    color and is compressed using lossy compression, which may noticeably\n    reduce the image quality if high amounts of compression are used. JPEG\n    files are commonly used for storing digital photos and web graphics.\n\n\n    # What is a JPEG file?\n\n    JPEG file open in Microsoft Windows Photos\n\n    In the early 1980s, no technology existed that allowed users to easily\n    compress and share digital images with one another. In 1982, the JPEG\n    workgroup began designing a compression standard that could be used to\n    reduce image files' size, making them easier to share, while retaining\n    as much of their quality as possible.\n\n    In 1992, the workgroup created the JPEG file format. JPEG files are images\n    created using a lossy compression algorithm, which actually destroys some\n    data contained within the original image file. However, this data loss is\n    mostly unnoticeable to the human eye. Because the JPEG standard continues\n    to allows users to produce sharable, high-quality image files, and because\n    it is so embedded within technologies used to create and share images,\n    it is still the most common image compression standard in use today.\n\n    NOTE: A JPEG file also contains metadata that describes the contents of\n    its file, such as the color space, color profile, and image dimension\n    information. Image files saved in the JPEG format are more commonly\n    appended with the .JPG extension than the JPEG extension.\n\n============\nDevelopment\n============\n\nTo install development dependencies, you will need `poetry <https://docs.pipenv.org/en/latest/>`_\nand `pre-commit <https://pre-commit.com/>`_.\n\n.. code-block :: console\n\n    pre-commit install --install-hooks\n    poetry install && poetry shell\n\n`direnv <https://direnv.net/>`_ is optional, but recommended for convenience.\n",
    'author': 'Ryan Delaney',
    'author_email': 'ryan.patrick.delaney@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/extinfo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
