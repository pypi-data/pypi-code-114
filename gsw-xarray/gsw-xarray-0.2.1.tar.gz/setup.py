# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gsw_xarray', 'gsw_xarray.tests']

package_data = \
{'': ['*']}

install_requires = \
['gsw>=3.4.0', 'xarray>=0.20.2']

extras_require = \
{'docs': ['Sphinx>=4.4.0', 'furo>=2022.1.2']}

setup_kwargs = {
    'name': 'gsw-xarray',
    'version': '0.2.1',
    'description': 'Drop in wrapper for gsw which adds CF standard name and units attributes to xarray results',
    'long_description': ".. |CI Status| image:: https://github.com/docotak/gsw-xarray/actions/workflows/ci.yml/badge.svg\n  :target: https://github.com/DocOtak/gsw-xarray/actions/workflows/ci.yml\n  :alt: CI Status\n.. |Documentation Status| image:: https://readthedocs.org/projects/gsw-xarray/badge/?version=latest\n  :target: https://gsw-xarray.readthedocs.io/en/latest/?badge=latest\n  :alt: Documentation Status\n\ngsw-xarray: Wrapper for gsw that adds CF attributes\n===================================================\n|CI Status| |Documentation Status|\n\ngsw-xarray is a wrapper for `gsw python <https://github.com/TEOS-10/GSW-python>`_\nthat will add CF attributes to xarray.DataArray outputs.\nIt is meant to be a drop in wrapper for the upstream GSW-Python library and will only add these attributes if one argument to a function is an xarray.DataArray.\n\nYou can find the documentation on `gsw-xarray.readthedocs.io <https://gsw-xarray.readthedocs.io/>`_.\n\nUsage\n-----\n\n.. code:: python\n\n   import gsw_xarray as gsw\n\n   # Create a xarray.Dataset\n   import numpy as np\n   import xarray as xr\n   ds = xr.Dataset()\n   id = np.arange(3)\n   ds['id'] = xr.DataArray(id, coords={'id':id})\n   ds['CT'] = ds['id'] * 10\n   ds['CT'].attrs = {'standard_name':'sea_water_conservative_temperature'}\n   ds['SA'] = ds['id'] * 0.1 + 34\n   ds['SA'].attrs = {'standard_name':'sea_water_absolute_salinity'}\n\n   # Apply gsw functions\n   sigma0 = gsw.sigma0(SA=ds['SA'], CT=ds['CT'])\n   print(sigma0.attrs)\n\nOutputs\n\n::\n\n   {'standard_name': 'sea_water_sigma_t', 'units': 'kg/m^3'}\n\nDon't worry about usage with non xarray array objects, just use in all places you would the upstream library:\n\n.. code:: python\n\n   sigma0 = gsw.sigma0(id * 10, id * 0.1 + 34)\n   print(type(sigma0), sigma0)\n\nOutputs\n\n::\n\n   <class 'numpy.ndarray'> [-5.08964499  2.1101098   9.28348219]\n\nInstallation\n------------\nPip\n...\n\n.. code:: bash\n\n    pip install gsw_xarray\n\n\nConda\n.....\n\nFor the moment gsw-xarray is not released in conda-forge, so you'll\nneed to install via pip: activate your conda environment, and then use ``pip install gsw_xarray``.\n\nPipenv\n......\n\nInside a pipenv environment: ``pipenv install gsw_xarray``.\n\n\nContributor guide\n-----------------\n\nAll contributions, bug reports, bug fixes, documentation improvements,\nenhancements, and ideas are welcome.\nIf you notice a bug or are missing a feature, fell free\nto open an issue in the `GitHub issues page <https://github.com/DocOtak/gsw-xarray/issues>`_.\n\nIn order to contribute to gsw-xarray, please fork the repository and\nsubmit a pull request. A good step by step tutorial for starting with git can be found in the\n`xarray contributor guide <https://xarray.pydata.org/en/stable/contributing.html#working-with-the-code>`_.\nA main difference is that we do not use conda as python environment, but poetry.\n\nSet up the environment\n......................\n\nYou will first need to `install poetry <https://python-poetry.org/docs/#installation>`_.\nThen go to your local clone of gsw-xarray and launch installation:\n\n.. code:: bash\n\n   cd /path/to/your/gsw-xarray\n   poetry install\n\nYou can then activate the environment by launching a shell\nwithin the virtual environment:\n\n.. code:: bash\n\n   poetry shell\n\nYou can check that the tests pass locally:\n\n.. code:: bash\n\n   pytest gsw_xarray/tests\n\nRelease (for maintainers only)\n..............................\n\nTODO...\n",
    'author': 'Andrew Barna',
    'author_email': 'abarna@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/DocOtak/gsw-xarray',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
