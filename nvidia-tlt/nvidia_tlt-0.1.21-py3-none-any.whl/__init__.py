# Copyright (c) 2017-2021, NVIDIA CORPORATION.  All rights reserved.

"""Python package for the TAO Toolkit Launcher."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import warnings

from tlt.version import __version__  # noqa pylint: disable=unused-import

warnings.simplefilter('always', DeprecationWarning)

message = (
    "\nThe `nvidia-tlt` package will be deprecated soon. "\
    "Going forward please migrate to using the `nvidia-tao` package.\n"
)

warnings.warn(message, DeprecationWarning)