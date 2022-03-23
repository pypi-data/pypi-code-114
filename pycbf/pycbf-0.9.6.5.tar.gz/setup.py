# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pycbf']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.17']

setup_kwargs = {
    'name': 'pycbf',
    'version': '0.9.6.5',
    'description': 'An API for CBF/imgCIF Crystallographic Binary Files',
    'long_description': "# `pycbf` - CBFlib for python\n\n[![PyPI release](https://img.shields.io/pypi/v/pycbf.svg)](https://pypi.python.org/pypi/pycbf)\n[![Supported Python versions](https://img.shields.io/pypi/pyversions/pycbf.svg)](https://pypi.org/project/pycbf)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)]( https://github.com/ambv/black)\n\nThis repository builds the `pycbf` portion only of Paul J Ellis and Herbert J\nBernstein's [CBFlib], as a [manylinux] binary wheel installable through `pip\ninstall pycbf`.\n\nIn order to do this, it has some limitations compared to the full build of CBFlib:\n\n-   No HDF5 bindings\n-   No (custom) libTiff bindings\n-   No CBF regex capabilities\n-   No header files included - this is not intended to be used as a linking\n    target\n\nIn addition to the base 0.9.6, this has the following significant alterations:\n\n| Version     | Changes                                                                                             |\n| ----------- | --------------------------------------------------------------------------------------------------- |\n| 0.9.6.0     | Regenerated SWIG bindings for Python 3 compatibility. Compiled with `SWIG_PYTHON_STRICT_BYTE_CHAR`. |\n| 0.9.6.2     | Drop python 2.7. Accept both `bytes` and `str`. Add `read_buffer` method, and `libimg` bindings.    |\n| 0.9.6.4     | Windows support, type annotations for `pycbf.Img`, and [dials-data] regression tests. |\n\nFor details, please see the [CHANGELOG](CHANGELOG.rst).\n\n[cbflib]: https://github.com/yayahjb/cbflib\n[manylinux]: https://www.python.org/dev/peps/pep-0571/\n[`yayahjb/cbflib#19`]: https://github.com/yayahjb/cbflib/pull/19\n[dials-data]: https://github.com/dials/data",
    'author': 'Herbert J. Bernstein',
    'author_email': 'yaya@bernstein-plus-sons.com',
    'maintainer': 'Nicholas Devenish',
    'maintainer_email': 'ndevenish@gmail.com',
    'url': 'http://www.bernstein-plus-sons.com/software/CBF/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
