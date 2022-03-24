"""
Import all possible stuff that can be used.
"""


# start delvewheel patch
def _delvewheel_init_patch_0_0_20():
    import os
    import sys
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, '.'))
    if sys.version_info[:2] >= (3, 8):
        conda_workaround = sys.version_info[:3] < (3, 9, 9) and os.path.exists(os.path.join(sys.base_prefix, 'conda-meta'))
        if conda_workaround:
            # backup the state of the environment variable CONDA_DLL_SEARCH_MODIFICATION_ENABLE
            conda_dll_search_modification_enable = os.environ.get('CONDA_DLL_SEARCH_MODIFICATION_ENABLE')
            os.environ['CONDA_DLL_SEARCH_MODIFICATION_ENABLE'] = '1'
        os.add_dll_directory(libs_dir)
        if conda_workaround:
            # restore the state of the environment variable CONDA_DLL_SEARCH_MODIFICATION_ENABLE
            if conda_dll_search_modification_enable is None:
                os.environ.pop('CONDA_DLL_SEARCH_MODIFICATION_ENABLE', None)
            else:
                os.environ['CONDA_DLL_SEARCH_MODIFICATION_ENABLE'] = conda_dll_search_modification_enable
    else:
        from ctypes import WinDLL
        with open(os.path.join(libs_dir, '.load-order-pillow_heif-0.1.11')) as file:
            load_order = file.read().split()
        for lib in load_order:
            WinDLL(os.path.join(libs_dir, lib))


_delvewheel_init_patch_0_0_20()
del _delvewheel_init_patch_0_0_20
# end delvewheel patch




from ._lib_info import (
    have_decoder_for_format,
    have_encoder_for_format,
    libheif_info,
    libheif_version,
)
from ._options import options
from ._version import __version__
from .as_opener import HeifImageFile, check_heif_magic, register_heif_opener
from .constants import heif_filetype_maybe  # DEPRECATED
from .constants import heif_filetype_no  # DEPRECATED
from .constants import heif_filetype_yes_supported  # DEPRECATED
from .constants import heif_filetype_yes_unsupported  # DEPRECATED
from .constants import (
    HeifBrand,
    HeifChannel,
    HeifChroma,
    HeifColorProfileType,
    HeifColorspace,
    HeifCompressionFormat,
    HeifErrorCode,
    HeifFiletype,
)
from .error import HeifError
from .misc import reset_orientation

# pylint: disable=redefined-builtin
from .reader import (
    HeifFile,
    HeifThumbnail,
    UndecodedHeifFile,
    UndecodedHeifThumbnail,
    check,
    check_heif,
    get_file_mimetype,
    is_supported,
    open,
    open_heif,
    read,
    read_heif,
)
from .writer import write_heif