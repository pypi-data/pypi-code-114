# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['c3d']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1,<2']

extras_require = \
{'gui': ['pyglet>=1.5.21,<2.0.0']}

entry_points = \
{'console_scripts': ['c3d-metatdata = scripts.c3d_metatdata:main()',
                     'c3d-viewer = scripts.c3d_viewer:main()',
                     'c3d2csv = scripts.c3d2csv:main()',
                     'c3d2npz = scripts.c3d2npz:main()']}

setup_kwargs = {
    'name': 'c3d',
    'version': '0.5.0',
    'description': 'A library for manipulating C3D binary files',
    'long_description': 'py-c3d\n======\n\nThis is a small library for reading and writing C3D binary files. C3D files are\na standard format for recording 3-dimensional time sequence data, especially\ndata recorded by a 3D motion tracking apparatus.\n\nInstalling\n----------\n\nInstall with pip::\n\n    pip install c3d\n\nOr if you\'d like to use the bleeding-edge version, just clone the github\nrepository and build and install using the normal Python setup process::\n\n    pip install git+https://github.com/EmbodiedCognition/py-c3d\n\nUsage\n-----\n\nTools\n~~~~~\n\nThis package includes a script for converting C3D motion data to CSV format\n(``c3d2csv``) and an OpenGL-based visualization tool for observing the motion\ndescribed by a C3D file (``c3d-viewer``).\n\nNote for the viewer you need to install `pyglet`.\nThis can be done by installing the gui extra of py-c3d::\n\n    pip install "c3d[gui]"\n\nLibrary\n~~~~~~~\n\nTo use the C3D library, just import the package and create a ``Reader`` or\n``Writer`` depending on your intended usage\n\n.. code-block:: python\n\n    import c3d\n\n    with open(\'data.c3d\', \'rb\') as handle:\n        reader = c3d.Reader(handle)\n        for i, (points, analog) in enumerate(reader.read_frames()):\n            print(\'Frame {}: {}\'.format(i, points.round(2)))\n\nYou can also get and set metadata fields using the library; see the `package\ndocumentation`_ for more details.\n\n.. _package documentation: http://c3d.readthedocs.org\n\nDeveloper Install\n~~~~~~~~~~~~~~~~~\n\nTo work on `c3d`, first install `poetry <https://python-poetry.org>`_ and then run::\n\n    git clone https://github.com/EmbodiedCognition/py-c3d\n    cd py-c3d\n    poetry install\n\nThis will create a new virtual environment with all the required dependency and `c3d` in develop mode.\n\nTests\n~~~~~\n\nTo run tests available in the test folder, following command can be run from the root of the package directory::\n\n    python -m unittest discover .\n\nTest scripts will automatically download test files from `c3d.org`_.\n\n.. _c3d.org: https://www.c3d.org/sampledata.html\n\nCaveats\n-------\n\nThis library is minimally effective, in the sense that the only motion tracking\nsystem I have access to (for testing) is a Phasespace system. If you try out the\nlibrary and find that it doesn\'t work with your motion tracking system, let me\nknow. Pull requests are also welcome!\n\nAlso, if you\'re looking for more functionality than just reading and writing C3D\nfiles, there are a lot of better toolkits out there that support a lot more file\nformats and provide more functionality, perhaps at the cost of increased\ncomplexity. The `biomechanical toolkit`_ is a good package for analyzing motion\ndata.\n\n.. _biomechanical toolkit: http://code.google.com/p/b-tk/\n',
    'author': 'UT Vision, Cognition, and Action Lab',
    'author_email': None,
    'maintainer': 'Leif Johnson',
    'maintainer_email': 'leif@cs.utexas.edu',
    'url': 'https://github.com/EmbodiedCognition/py-c3d',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
