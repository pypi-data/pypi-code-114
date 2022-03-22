# -*- coding: utf-8 -*-

try:
    from el_validator.validator import validators, checkers, errors
    from el_validator.__version__ import __version__
except ImportError:
    from .validator import validators, checkers, errors
    from .__version__ import __version__
