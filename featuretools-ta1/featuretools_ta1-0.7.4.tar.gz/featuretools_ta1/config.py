from d3m import utils as d3m_utils
from d3m.metadata import base as metadata_base
from pathlib import Path


AUTHOR = "MIT_FeatureLabs"
CONTACT = "mailto:alice.r.yepremyan@jpl.nasa.gov"


mode = 'PYPI'
if mode == 'PYPI':
    INSTALLATION = [{
        'type': metadata_base.PrimitiveInstallationType.PIP,
        'package': 'featuretools-ta1',
        'version': '0.7.4',
    }]
else:
    _git_commit = d3m_utils.current_git_commit(Path(__file__).parents[1])
    INSTALLATION = [{
        'type': metadata_base.PrimitiveInstallationType.PIP,
        'package_uri': 'git+https://gitlab.com/datadrivendiscovery/contrib/featuretools_ta1.git@{git_commit}#egg=featuretools_ta1'.format(
            git_commit=_git_commit),
    }]
