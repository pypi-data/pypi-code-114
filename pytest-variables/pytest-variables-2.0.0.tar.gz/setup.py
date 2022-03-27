# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pytest_variables']

package_data = \
{'': ['*']}

install_requires = \
['pytest>=3.0.0,<8.0.0']

extras_require = \
{'hjson': ['hjson'], 'toml': ['toml'], 'yaml': ['PyYAML']}

entry_points = \
{'pytest11': ['variables = pytest_variables.plugin']}

setup_kwargs = {
    'name': 'pytest-variables',
    'version': '2.0.0',
    'description': 'pytest plugin for providing variables to tests/fixtures',
    'long_description': 'pytest-variables\n================\n\npytest-variables is a plugin for pytest_ that provides variables to\ntests/fixtures as a dictionary via a file specified on the command line.\n\n.. image:: https://img.shields.io/badge/license-MPL%202.0-blue.svg\n   :target: https://github.com/pytest-dev/pytest-variables/blob/master/LICENSE\n   :alt: License\n.. image:: https://img.shields.io/pypi/v/pytest-variables.svg\n   :target: https://pypi.python.org/pypi/pytest-variables/\n   :alt: PyPI\n.. image:: https://img.shields.io/travis/pytest-dev/pytest-variables.svg\n   :target: https://travis-ci.org/pytest-dev/pytest-variables/\n   :alt: Travis\n.. image:: https://img.shields.io/github/issues-raw/pytest-dev/pytest-variables.svg\n   :target: https://github.com/pytest-dev/pytest-variables/issues\n   :alt: Issues\n.. image:: https://img.shields.io/requires/github/pytest-dev/pytest-variables.svg\n   :target: https://requires.io/github/pytest-dev/pytest-variables/requirements/?branch=master\n   :alt: Requirements\n\nRequirements\n------------\n\nYou will need the following prerequisites in order to use pytest-variables:\n\n- Python 3.7+ or PyPy3\n\nInstallation\n------------\n\nTo install pytest-variables:\n\n.. code-block:: bash\n\n  $ pip install pytest-variables\n\nAdditional formats\n------------------\n\nThe following optional formats are supported, but must be explicitly installed\nas they require additional dependencies:\n\nHuman JSON\n~~~~~~~~~~\n\n`Human JSON`_ is a configuration file format that caters to humans and helps\nreduce the errors they make. To install Human JSON support:\n\n.. code-block:: bash\n\n  $ pip install pytest-variables[hjson]\n\nYAML\n~~~~\n\nYAML_ is a human friendly data serialization standard for all programming\nlanguages. To install YAML support:\n\n.. code-block:: bash\n\n  $ pip install pytest-variables[yaml]\n\nYAML Loader\n^^^^^^^^^^^\n\nYou can specify which loader to use by setting ``yaml_loader`` in ``pytest.ini`` (or similar file)\nto one of the following:\n\n  * BaseLoader\n  * SafeLoader\n  * FullLoader (default)\n  * UnsafeLoader\n\n.. code-block:: ini\n\n  [pytest]\n  yaml_loader = BaseLoader\n\n**Note** that loader is case-sensitive.\n\nTo learn more about the loader, see `here <https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation>`_\n\nTOML\n~~~~~~~~~~\n\nTOML_ aims to be a minimal configuration file format that\'s easy to read due to obvious semantics. TOML is designed to map unambiguously to a hash table.\nTo install TOML support:\n\n.. code-block:: bash\n\n  $ pip install pytest-variables[toml]\n\nContributing\n------------\n\nWe welcome contributions.\n\nTo learn more, see `Development <https://github.com/pytest-dev/pytest-variables/blob/master/development.rst>`_\n\nSpecifying variables\n--------------------\n\nUse the `--variables` command line option one or more times to specify paths to\nfiles containing your variables:\n\n.. code-block:: bash\n\n  $ pytest --variables firefox-53.json --variables windows-10.json\n\n\nwith the following contents for the ``firefox-53.json`` file:\n\n.. code-block:: json\n\n  {\n    "capabilities": {\n      "browser": "Firefox",\n      "browser_version": "53.0"\n    }\n  }\n\nand another file named ``windows-10.json`` with:\n\n.. code-block:: json\n\n  {\n    "capabilities": {\n      "os": "Windows",\n      "os_version": "10",\n      "resolution": "1280x1024"\n    }\n  }\n\nyou\'ll get the merged version of your variables:\n\n.. code-block:: json\n\n  {\n    "capabilities": {\n      "browser": "Firefox",\n      "browser_version": "53.0",\n      "os": "Windows",\n      "os_version": "10",\n      "resolution": "1280x1024"\n    }\n  }\n\nIf multiple files are specified then they will be applied in the order they\nappear on the command line. When duplicate keys with non dictionary_ values\nare encountered, the last to be applied will take priority.\n\nAccessing variables\n-------------------\n\nWith a JSON variables file such as:\n\n.. code-block:: json\n\n  {\n    "foo": "bar",\n    "bar": "foo"\n  }\n\nSpecify the `variables` funcarg to make the variables available to your tests.\nThe contents of the files are made available as a dictionary_:\n\n.. code-block:: python\n\n  def test_foo(self, variables):\n      assert variables[\'foo\'] == \'bar\'\n      assert variables.get(\'bar\') == \'foo\'\n      assert variables.get(\'missing\') is None\n\nResources\n---------\n\n- `Release Notes`_\n- `Issue Tracker`_\n- Code_\n\n.. _pytest: http://pytest.org\n.. _Human JSON: http://hjson.org\n.. _YAML: http://yaml.org\n.. _TOML: https://github.com/toml-lang/toml\n.. _dictionary: https://docs.python.org/tutorial/datastructures.html#dictionaries\n.. _Release Notes:  http://github.com/pytest-dev/pytest-variables/blob/master/CHANGES.rst\n.. _Issue Tracker: http://github.com/pytest-dev/pytest-variables/issues\n.. _Code: http://github.com/pytest-dev/pytest-variables\n',
    'author': 'Dave Hunt',
    'author_email': 'dhunt@mozilla.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pytest-dev/pytest-variables',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
