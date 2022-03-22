# This file is used to configure the behavior of pytest when using the Astropy
# test infrastructure.

from astropy.version import version as astropy_version
if astropy_version < '3.0':
    # With older versions of Astropy, we actually need to import the pytest
    # plugins themselves in order to make them discoverable by pytest.
    from astropy.tests.pytest_plugins import *
    del pytest_report_header
else:
    # As of Astropy 3.0, the pytest plugins provided by Astropy are
    # automatically made available when Astropy is installed. This means it's
    # not necessary to import them here, but we still need to import global
    # variables that are used for configuration.
    from pytest_astropy_header.display import PYTEST_HEADER_MODULES, TESTED_VERSIONS

from astropy.tests.helper import enable_deprecations_as_exceptions

## Uncomment the following line to treat all DeprecationWarnings as
## exceptions. For Astropy v2.0 or later, there are 2 additional keywords,
## as follow (although default should work for most cases).
## To ignore some packages that produce deprecation warnings on import
## (in addition to 'compiler', 'scipy', 'pygments', 'ipykernel', and
## 'setuptools'), add:
##     modules_to_ignore_on_import=['module_1', 'module_2']
## To ignore some specific deprecation warning messages for Python version
## MAJOR.MINOR or later, add:
##     warnings_to_ignore_by_pyver={(MAJOR, MINOR): ['Message to ignore']}
# enable_deprecations_as_exceptions()

## Uncomment and customize the following lines to add/remove entries from
## the list of packages for which version numbers are displayed when running
## the tests. Making it pass for KeyError is essential in some cases when
## the package uses other astropy affiliated packages.
# try:
#     PYTEST_HEADER_MODULES['Astropy'] = 'astropy'
#     PYTEST_HEADER_MODULES['scikit-image'] = 'skimage'
#     del PYTEST_HEADER_MODULES['h5py']
# except (NameError, KeyError):  # NameError is needed to support Astropy < 1.0
#     pass

# Uncomment the following lines to display the version number of the
# package rather than the version number of Astropy in the top line when
# running the tests.

# new variant of the above
# def pytest_configure(config):

#     config.option.astropy_header = True

#     PYTEST_HEADER_MODULES.pop('Pandas', None)
#     PYTEST_HEADER_MODULES['scikit-image'] = 'skimage'

#     from .version import version, astropy_helpers_version
#     packagename = os.path.basename(os.path.dirname(__file__))
#     TESTED_VERSIONS[packagename] = version
#     TESTED_VERSIONS['astropy_helpers'] = astropy_helpers_version


import os

# This is to figure out the package version, rather than
# using Astropy's
try:
    from .version import version
except ImportError:
    version = 'dev'

try:
    pycraf_gui = os.path.basename(os.path.dirname(__file__))
    TESTED_VERSIONS[pycraf] = version
except NameError:   # Needed to support Astropy <= 1.0.0
    pass


# want the following two fixtures in multiple sub-packages

import pytest
from pycraf import pathprof

# this only works if pytest is started in project directory and not
# with --pyargs pycraf_gui from anywhere else :-(
# see also https://github.com/pytest-dev/pytest/issues/1596
def pytest_addoption(parser):
    parser.addoption(
        '--dogui', action='store_true', default=False,
        help='Do GUI tests.'
        )


def pytest_configure(config):
    config.addinivalue_line("markers", "gui: mark as gui test")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--dogui"):
        # do-gui-tests given in cli: do gui tests
        return
    skip_gui = pytest.mark.skip(reason="need --dogui option to run")
    for item in items:
        if "gui" in item.keywords:
            item.add_marker(skip_gui)

# @pytest.fixture
# def do_gui_tests(request):
#     return request.config.getoption("--do-gui-tests")


# def pytest_runtest_setup(item):
#     if 'do_gui_tests' in item.keywords and not item.config.getoption('--do-gui-tests'):
#         pytest.skip('GUI tests are only executed if user provides "--do-gui-tests" command line option')


@pytest.fixture(scope='session')
def srtm_temp_dir(tmpdir_factory, create_mock_data=True):

    tdir = tmpdir_factory.mktemp('srtmdata')

    if create_mock_data:
        import numpy as np
        from astropy.utils.misc import NumpyRNGContext

        with NumpyRNGContext(0):
            tile = np.int16(np.random.normal(200, 50, (1201, 1201)))
            hgt_file = tdir / "N50E006.hgt"
            np.ascontiguousarray(tile, dtype='>i2').tofile(hgt_file)
            tile = np.int16(np.random.normal(200, 50, (1201, 1201)))
            hgt_file = tdir / "N50E005.hgt"
            np.ascontiguousarray(tile, dtype='>i2').tofile(hgt_file)

    return str(tdir)


@pytest.fixture(scope='class')
def srtm_handler(srtm_temp_dir):
    print("srtm_handler")

    with pathprof.srtm.SrtmConf.set(
            srtm_dir=srtm_temp_dir,
            download='never',
            interp='linear',
            ):

        yield
