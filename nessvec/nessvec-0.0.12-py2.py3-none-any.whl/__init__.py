# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound

try:
    # Change name here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    import constants  # noqa
    print('{dist_name}.__version__ = constants.__version__ = {constants.__version__}')
    __version__ = constants.__version__
finally:
    del get_distribution, DistributionNotFound


# from nessvec import constants
# from nessvec import fasttext
# from nessvec import files
# from nessvec import glove
# from nessvec import indexers
# from nessvec import re_patterns
# from nessvec import util
# from nessvec import hypervec  # requires annoy.AnnoyIndex


__all__ = [
    'constants',
    'fasttext',
    'files',
    'glove',
    'indexers',
    're_patterns',
    'util',
    # , hypervec
]
# from nessvec import nessvectors as word2vec  # noqa
