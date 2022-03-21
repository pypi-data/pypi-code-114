import os
from d3m import utils

D3M_API_VERSION = "2021.12.19" #d3m.__version__
VERSION = "1.0.0"

REPOSITORY = "https://gitlab.com/datadrivendiscovery/contrib/realML"
PACKAGE_NAME_GRAPHS = "dsbox-graphs"

D3M_PERFORMER_TEAM = 'ISI'


INSTALLATION_TYPE = 'PYPI'
if INSTALLATION_TYPE == 'PYPI':
    INSTALLATION = {
        "type" : "PIP",
        "package": PACKAGE_NAME_GRAPHS,
        "version": VERSION
    }
else:
    TAG_NAME = utils.current_git_commit(os.path.dirname(__file__))
    PACKAGE_URI_GRAPHS = "git+" + REPOSITORY + "@" + TAG_NAME + "#egg=" + PACKAGE_NAME_GRAPHS

    INSTALLATION = {
        "type" : "PIP",
        "package_uri": PACKAGE_URI_GRAPHS,
    }
