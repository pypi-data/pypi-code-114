from contextlib import suppress
from importlib import metadata

from torch_conv_gradfix.conv_gradfix import (conv2d, conv_transpose2d, enabled,
                                             no_weight_grad)

__author__ = "Peter Yuen"
__email__ = "ppeetteerrsx@gmail.com"
__version__ = "test"
with suppress(Exception):
    __version__ = metadata.version("torch_conv_gradfix")

__all__ = ["enabled", "no_weight_grad", "conv2d", "conv_transpose2d"]
