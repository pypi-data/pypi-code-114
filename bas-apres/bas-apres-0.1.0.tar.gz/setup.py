# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['apres']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.4.3,<4.0.0', 'netCDF4>=1.5.2,<2.0.0', 'numpy>=1.17.2,<2.0.0']

entry_points = \
{'console_scripts': ['apres_to_nc = apres.apres_to_nc:main',
                     'nc_to_apres = apres.nc_to_apres:main',
                     'plot_apres = apres.plot_apres:main',
                     'read_apres = apres.read_apres:main',
                     'write_apres = apres.write_apres:main']}

setup_kwargs = {
    'name': 'bas-apres',
    'version': '0.1.0',
    'description': 'Package for working with BAS ApRES files',
    'long_description': "# apres\n\nThis project enables ApRES .dat files to be read, rewritten, and converted.\n\n## The apres package\n\nThe apres package contains a number of classes for working with ApRES .dat files.\n\n* The `ApRESBurst` class manages reading/writing a single burst block (the textual header and the binary data) from/to an opened ApRES .dat file.\n* The `ApRESFile` class is a context manager for ApRES .dat files.  The class wraps the `ApRESBurst` class and can read a variable number of burst blocks from a file (i.e. a single burst file or a timeseries file).  It also contains methods for subsetting an ApRES file, and for converting the file to netCDF4.\n\n## Install\n\nThe package can be installed from PyPI (note the package distribution name):\n\n```bash\n$ pip install bas-apres\n```\n\n## Simple utility scripts\n\nThe package contains a number of scripts for converting from/to netCDF, plotting the data etc.  When installing the package (e.g., via `pip install`) then these scripts are available as commands and added to the `PATH`.  So for instance, you can just call `apres_to_nc`.  If running the scripts from a `clone` of the source code repository, then they need to be run as modules, e.g. `python -m apres.apres_to_nc`.\n\n### apres_to_nc.py\n\nThis script converts an ApRES .dat file to netCDF4.  The default output netCDF filename has the same name as the input .dat file, but with a .nc file suffix.  Optionally an alternative output netCDF filename can be explicitly given.\n\n```bash\npython3 -m apres.apres_to_nc filename.dat [outfile.nc]\n```\n\nThe conversion is a straightforward mapping, in that each burst becomes a netCDF4 group, where the header lines become group attributes, and the data are stored as a `NSubBursts` x `N_ADC_SAMPLES` 2D data array.\n\n### nc_to_apres.py\n\nThis script converts a previously converted netCDF4 file back to the original ApRES .dat file.  The default output ApRES .dat filename has the same name as the input netCDF file, but with a .dat file suffix.  Optionally an alternative output ApRES filename can be explicitly given.\n\n```bash\npython3 -m apres.nc_to_apres infile.nc [outfile.dat]\n```\n\nThe conversion is a straightforward reversal of the original conversion.  For the newer ApRES .dat file format version, this should be identical to the original file.  For the older ApRES .dat file format version, there will likely be small differences in the whitespace in the textual header.  Ignoring these insignificant changes in whitespace (e.g. `diff -awB orig.dat reconstructed.dat`), the files will be identical.\n\n### plot_apres.py\n\nThis script will plot the `N_ADC_SAMPLES` vs `NSubBursts` as a radargram, for each burst in the file (or group for converted netCDF files).  If the `Average` header item > 0 (and so each subburst has been aggregated), then the script will instead plot the first subburst as a single trace.  The file can be either an ApRES .dat file, or a converted netCDF file.\n\n```bash\npython3 -m apres.plot_apres [-h] [-r | -t] [-g GRID GRID] [-c CONTRAST] [-m CMAP]\n                            filename.{dat,nc}\n\nplot ApRES data, either from a .dat file, or a converted netCDF file\n\npositional arguments:\n  filename              filename\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -r, --radargram       plot a radargram\n  -t, --traces          plot individual traces\n  -g GRID GRID, --grid GRID GRID\n                        plot the first nrows x ncols traces\n  -c CONTRAST, --contrast CONTRAST\n                        contrast for the radargram\n  -m CMAP, --cmap CMAP  colour map for the radargram\n\nExamples\n\nPlot the given ApRES .dat file as a radargram:\n\npython3 -m apres.plot_apres filename.dat\n\nPlot the given converted netCDF file as a radargram:\n\npython3 -m apres.plot_apres filename.nc\n\nPlot the given ApRES file as a radargram, increasing the contrast:\n\npython3 -m apres.plot_apres -c 10 filename.dat\n\nSame as above, but with a blue-white-red colour map:\n\npython3 -m apres.plot_apres -c 10 -m bwr filename.dat\n\nPlot the first trace from the given ApRES file:\n\npython3 -m apres.plot_apres -t filename.dat\n\nPlot the first 6 traces, in a 3x2 grid:\n\npython3 -m apres.plot_apres -t -g 3 2 filename.dat\n```\n\n### read_apres.py\n\nThis script will read the given ApRES .dat file, and for each burst, print the results of parsing the header, such as the dimensions of the data array, and the parsed header dictionary.  It will also *head* the data section (by default the first 10 samples of the first 10 subbursts), to give an initial simple look at the data.\n\nThe script's primary purpose is as a simple example of how to use the `ApRESFile` class to read an ApRES .dat file.\n\n```bash\npython3 -m apres.read_apres filename.dat\n```\n\n### write_apres.py\n\nThis script will read the given input ApRES .dat file, and for each burst, write the header and data to the given output ApRES .dat file.  Optionally a subset of bursts can be written out, specified as the first `bursts` bursts of the input file.  In addition a subset of each burst can be written out, specified as the first `subbursts` subbursts, and the first `samples` ADC samples of these subbursts.  If `bursts`, `subbursts` and `samples` are not specified, then the output file is identical to the input file.\n\nThe script's primary purpose is as a simple example of how to use the `ApRESFile` class to rewrite an ApRES .dat file.\n\n```bash\npython3 -m apres.write_apres [-b BURSTS] [-u SUBBURSTS] [-s SAMPLES] infile.dat outfile.dat\n```\n\n",
    'author': 'Paul Breen',
    'author_email': 'pbree@bas.ac.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/antarctica/bas-apres',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
