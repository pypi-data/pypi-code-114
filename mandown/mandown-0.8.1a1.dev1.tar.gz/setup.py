# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mandown', 'mandown.sources']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.10.0,<5.0.0',
 'feedparser>=6.0.8,<7.0.0',
 'lxml>=4.7.1,<5.0.0',
 'natsort>=8.0.2,<9.0.0',
 'requests>=2.27.0,<3.0.0',
 'typer>=0.4.0,<0.5.0',
 'undetected-chromedriver>=3.1.5,<4.0.0']

extras_require = \
{'postprocessing': ['Pillow>=9.0.1,<10.0.0']}

entry_points = \
{'console_scripts': ['mandown = mandown.cli:main']}

setup_kwargs = {
    'name': 'mandown',
    'version': '0.8.1a1.dev1',
    'description': 'Command line application and library to download and convert comics from various sources',
    'long_description': '# mandown\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)\n[![Download from PyPI](https://img.shields.io/pypi/v/mandown)](https://pypi.org/project/mandown)\n[![Download from the AUR](https://img.shields.io/aur/version/mandown-git)](https://aur.archlinux.org/packages/mandown-git)\n[![Latest release](https://img.shields.io/github/v/release/potatoeggy/mandown?display_name=tag)](https://github.com/potatoeggy/mandown/releases/latest)\n[![License](https://img.shields.io/github/license/potatoeggy/mandown)](/LICENSE)\n\nComic downloader and converter to CBZ, EPUB, and/or PDF as a Python library and command line application.\n\n## Supported sites\n\nTo request a new site, please file a [new issue](https://github.com/potatoeggy/mandown/issues/new).\n\n- https://mangasee123.com\n- https://manganato.com\n- https://webtoons.com\n- https://mangadex.org\n- https://mangakakalot.com\n- https://readcomiconline.li\n\n## Installation\n\nInstall the package from PyPI:\n\n```\npip3 install mandown\n```\n\nOr, to build from source:\n\nMandown depends on [poetry](https://github.com/python-poetry/poetry) for building.\n\n```\ngit clone https://github.com/potatoeggy/mandown.git\npoetry install\npoetry build\npip3 install dist/mandown*.whl\n```\n\n## Usage\n\n```\nmandown download <URL>\n```\n\nTo convert the download contents to CBZ/EPUB, append the `--convert` option. To apply image processing to the downloaded images, append the `--process` option.\n\n```\nmandown download <URL> --convert epub --process rotate_double_pages\n```\n\nTo convert an existing folder without downloading anything except metadata (like a stripped-down version of https://github.com/ciromattia/kcc), use the `convert` command.\n\n```\nmandown convert <FORMAT> <PATH_TO_FOLDER>\n```\n\nRun `mandown --help` for more info.\n\n## Library usage\n\n```python\nimport os\nimport mandown\nfrom mandown.converter import Converter\n\ncomic = mandown.query(url_to_comic)\nprint(comic.metadata, comic.chapters)\nfor c in comic.chapters:\n    mandown.download_chapter(c, dest_folder=os.getcwd(), maxthreads=4)\n\nfolder_path = os.getcwd()\nmandown.process(folder_path, [ProcessOps.TRIM_BORDERS, ProcessOps.ROTATE_DOUBLE_PAGES])\n\nconverter = Converter(folder_path, metadata=comic.metadata)\nconverter.to_epub()\n```\n',
    'author': 'Daniel Chen',
    'author_email': 'danielchen04@hotmail.ca',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/potatoeggy/mandown',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
