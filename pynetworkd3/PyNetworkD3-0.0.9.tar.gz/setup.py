# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['PyNetworkD3']

package_data = \
{'': ['*'],
 'PyNetworkD3': ['templates/*',
                 'templates/adjacency matrix/*',
                 'templates/arc diagram/*',
                 'templates/force graph/*',
                 'templates/js utils/*',
                 'templates/radial diagram/*']}

install_requires = \
['pyserial>=3.5,<4.0']

entry_points = \
{'console_scripts': ['PyNetworkD3 = PyNetworkD3.cli.core:dispatcher']}

setup_kwargs = {
    'name': 'pynetworkd3',
    'version': '0.0.9',
    'description': 'Create D3 visualization networks with Python',
    'long_description': '<h1 align="center">PyNetworkD3</h1>\n\n<p align="center">\n    <em>\n        Create D3 visualization networks with Python\n    </em>\n</p>\n\n<p align="center">\n<a target="_blank" href="https://colab.research.google.com/drive/1AwtW-FDAaTh_RMBKj4CJYcyKP2xnOanK?usp=sharing"><img src="https://img.shields.io/badge/example-Open%20in%20colab-hsl(30%2C%20100%25%2C%2048%25)?logo=googlecolab" /></a>\n\n<a href="https://pypi.org/project/pynetworkd3/" target="_blank">\n    <img src="https://img.shields.io/pypi/v/pynetworkd3?label=version&logo=python&logoColor=%23fff&color=306b9c" alt="PyPI - Version">\n</a>\n\n<a href="https://github.com/hernan4444/pynetworkd3/actions?query=workflow%3Atests" target="_blank">\n    <img src="https://img.shields.io/github/workflow/status/hernan4444/pynetworkd3/tests?label=tests&logo=python&logoColor=%23fff" alt="Tests">\n</a>\n\n<a href="https://github.com/hernan4444/pynetworkd3/actions?query=workflow%3Alinters" target="_blank">\n    <img src="https://img.shields.io/github/workflow/status/hernan4444/pynetworkd3/linters?label=linters&logo=github" alt="Linters">\n</a> \n\n<!-- \n<a href="https://codecov.io/gh/daleal/iic2343" target="_blank">\n    <img src="https://img.shields.io/codecov/c/gh/daleal/iic2343?label=coverage&logo=codecov&logoColor=ffffff" alt="Coverage">\n</a>\n-->\n</p>\n\n## Installation\n\nInstall using `pip`!\n\n```sh\n$ pip install pynetworkd3\n```\n\n## Input JSON syntax\n\n```\n{\n    "nodes": [\n        {\n          "id": "id1",\n          "attribute 1": "value attribute 1",\n          "attribute 2": "value attribute 2",\n          (...)\n          "attribute N": "value attribute N",\n        },\n        {\n          "id": "id2",\n          "attribute 1": "value attribute 1",\n          "attribute 2": "value attribute 2",\n          (...)\n          "attribute N": "value attribute N",\n        },\n        (...)\n    ],\n    "links": [\n        {\n            "source": "id1",\n            "target": "id2",\n            "attribute 1": "value attribute 1",\n            "attribute 2": "value attribute 2",\n            (...)\n            "attribute N": "value attribute N",\n        },\n        (...)\n    ]\n}\n```\n\n- Every dictionary in "nodes" must have the _id_ key. The other keys are optionals.\n\n- Every dictionary in "links" must have the _source_ and _target_ key. The other keys are optionals. Also, each id in source and target must redirect to an existing node in "nodes".\n\n\n## Usage\n\nTo use the library, import the `Graph` object directly and use the `export` method\nto create a `.html` with the visualization. \n\n\n```python\nfrom PyNetworkD3 import Graph\n\ndataset = {\n    "nodes": [{"id": 1},{"id": 2},{"id": 3},{"id": 4},{"id": 5}],\n    "links": [\n        {"source": 1, "target": 3},\n        {"source": 2, "target": 3},\n        {"source": 1, "target": 3},\n        {"source": 5, "target": 3},\n        {"source": 4, "target": 1},\n    ]\n}\n\ngraph = Graph(dataset, width=300, height=200, radio=10, tooltip=["id"])\n\ngraph.export("output.html)\n```\n\nAlso you can write the instance in the last line of the notebook\'s cell (ckeck the <a href="https://colab.research.google.com/drive/1AwtW-FDAaTh_RMBKj4CJYcyKP2xnOanK?usp=sharing"> example in colab</a>) to view the visualization.\n\n\n## Developing\n\nThis library uses `PyTest` as the test suite runner, and `PyLint`, `Flake8`, `Black`, `ISort` and `MyPy` as linters. It also uses `Poetry` as the default package manager.\n\nThe library includes a `Makefile` that has every command you need to start developing. If you don\'t have it, install `Poetry` using:\n\n```sh\nmake get-poetry\n```\n\nThen, create a virtualenv to use throughout the development process, using:\n\n```sh\nmake build-env\n```\n\nActivate the virtualenv using:\n\n```sh\n. .venv/bin/activate\n```\n\nDeactivate it using:\n\n```sh\ndeactivate\n```\n\nTo add a new package, use `Poetry`:\n\n```sh\npoetry add <new-package>\n```\n\nTo run the linters, you can use:\n\n```sh\n# The following commands auto-fix the code\nmake black!\nmake isort!\n\n# The following commands just review the code\nmake black\nmake isort\nmake flake8\nmake mypy\nmake pylint\n```\n\nTo run the tests, you can use:\n\n```sh\nmake tests\n```\n\n## Releasing\n\nTo make a new release of the library, `git switch` to the `master` branch and execute:\n\n```sh\nmake bump! minor\n```\n\nThe word `minor` can be replaced with `patch` or `major`, depending on the type of release. The `bump!` command will bump the versions of the library, create a new branch, add and commit the changes. Then, just _merge_ that branch to `master`. Finally, execute a _merge_ to the `stable` branch. Make sure to update the version before merging into `stable`, as `PyPi` will reject packages with duplicated versions. \n',
    'author': 'Hernán Valdivieso',
    'author_email': 'hfvaldivieso@uc.cl',
    'maintainer': 'Hernán Valdivieso',
    'maintainer_email': 'hfvaldivieso@uc.cl',
    'url': 'https://github.com/Hernan4444/PyNetworkD3',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
