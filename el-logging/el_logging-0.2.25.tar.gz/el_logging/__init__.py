# -*- coding: utf-8 -*-

try:
    from el_logging.logging import logger
    from el_logging.__version__ import __version__
except ImportError:
    from .logging import logger
    from .__version__ import __version__
