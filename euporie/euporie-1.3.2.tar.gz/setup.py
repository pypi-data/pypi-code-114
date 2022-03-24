# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['euporie',
 'euporie.app',
 'euporie.commands',
 'euporie.convert',
 'euporie.convert.formats',
 'euporie.key_binding',
 'euporie.key_binding.bindings',
 'euporie.markdown',
 'euporie.markdown.blocks',
 'euporie.menu',
 'euporie.output']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.0,<10.0',
 'aenum>=3.1,<4.0',
 'appdirs>=1.4,<2.0',
 'flatlatex>=0.15,<0.16',
 'imagesize>=1.3.0,<2.0.0',
 'jsonschema>=4.4,<5.0',
 'jupyter-client>=7.1,<8.0',
 'nbformat>=5,<6',
 'prompt-toolkit>=3.0,<4.0',
 'pyperclip>=1.8,<2.0',
 'rich>=11,<12',
 'timg>=1.1,<2.0']

extras_require = \
{'all': ['mtable>=0.1,<0.2',
         'html5lib>=1.1,<2.0',
         'CairoSVG>=2.5,<3.0',
         'black>=19.3b0'],
 'formatters': ['black>=19.3b0',
                'isort>=5.10.1,<6.0.0',
                'ssort>=0.11.4,<0.12.0'],
 'html-mtable': ['mtable>=0.1,<0.2', 'html5lib>=1.1,<2.0'],
 'images-img2unicode': ['img2unicode>=0.1a8,<0.1'],
 'latex-sympy': ['sympy>=1.9,<2.0', 'antlr4-python3-runtime>=4.9,<5.0'],
 'svg-cairosvg': ['CairoSVG>=2.5,<3.0']}

entry_points = \
{'console_scripts': ['euporie = euporie.__main__:main']}

setup_kwargs = {
    'name': 'euporie',
    'version': '1.3.2',
    'description': 'Euporie is a text-based user interface for running and editing Jupyter notebooks',
    'long_description': '.. image:: https://user-images.githubusercontent.com/12154190/159142921-77e710d8-823a-46d0-917a-8703048a43b7.svg\n\n#######\neuporie\n#######\n\n|PyPI| |RTD| |PyVer| |License| |Binder| |Stars|\n\n.. content_start\n\n**Euporie is a terminal app for running and editing Jupyter notebooks.**\n\nThe text-based interface is inspired by JupyterLab / Jupyter Notebook, and runs entirely in the terminal.\n\n.. figure:: https://user-images.githubusercontent.com/12154190/151821363-9176faac-169f-4b12-a83f-8a4004e5b9bb.png\n   :target: https://user-images.githubusercontent.com/12154190/151821363-9176faac-169f-4b12-a83f-8a4004e5b9bb.png\n\n   `View more screenshots here <https://euporie.readthedocs.io/en/latest/pages/gallery.html>`_\n\n----\n\n*******\nInstall\n*******\n\nYou can install euporie with `pipx <https://pipxproject.github.io/>`_ (recommended) or ``pip``:\n\n.. code-block:: console\n\n   $ pipx install euporie\n   $ # OR\n   $ python -m pip install --user euporie\n\nYou can also try euporie online `here <https://mybinder.org/v2/gh/joouha/euporie-binder/HEAD?urlpath=%2Feuporie%2F>`_.\n\n*****\nUsage\n*****\n\nOpen a notebook by passing the notebook\'s file path as a command line argument:\n\n.. code-block:: console\n\n   $ euporie notebook.ipynb\n\nAlternatively, launch ``euporie`` and open a notebook file by selecting "Open" from the file menu (*Ctrl+o*).\n\nFor more information about the available command line flags, run:\n\n.. code-block:: console\n\n   $ euporie --help\n\n\n*************\nDocumentation\n*************\n\nView the online documentation at: `https://euporie.readthedocs.io/ <https://euporie.readthedocs.io/>`_\n\nThe code is available on GitHub at: `https://github.com/joouha/euporie <https://github.com/joouha/euporie>`_\n\n********\nFeatures\n********\n\n* Edit and run notebooks in the terminal\n* Displays rich cell outputs, including markdown, tables, images, LaTeX, HTML, SVG, & PDF\n* Print formatted notebooks to the terminal or pager\n* Open multiple notebooks side-by-side\n* Hightly configurable\n* Code completion\n* Line completions from history\n* Display contextual help\n* Automatic code formatting\n\n*************\nCompatibility\n*************\n\nEuporie requires Python 3.8 or later. It works on Linux, Windows and MacOS\n\n\n\n.. |PyPI| image:: https://img.shields.io/pypi/v/euporie.svg\n    :target: https://pypi.python.org/project/euporie/\n    :alt: Latest Version\n\n.. |RTD| image:: https://readthedocs.org/projects/euporie/badge/\n    :target: https://euporie.readthedocs.io/en/latest/\n    :alt: Documentation\n\n.. |PyVer| image:: https://img.shields.io/pypi/pyversions/euporie\n    :target: https://pypi.python.org/project/euporie/\n    :alt: Supported Python versions\n\n.. |Binder| image:: https://mybinder.org/badge_logo.svg\n   :target: https://mybinder.org/v2/gh/joouha/euporie-binder/HEAD?urlpath=%2Feuporie%2F\n   :alt: Launch with Binder\n\n.. |License| image:: https://img.shields.io/github/license/joouha/euporie.svg\n    :target: https://github.com/joouha/euporie/blob/main/LICENSE\n    :alt: View license\n\n.. |Stars| image:: https://img.shields.io/github/stars/joouha/euporie\n    :target: https://github.com/joouha/euporie/stargazers\n    :alt: ⭐\n',
    'author': 'Josiah Outram Halstead',
    'author_email': 'josiah@halstead.email',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/joouha/euporie',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
