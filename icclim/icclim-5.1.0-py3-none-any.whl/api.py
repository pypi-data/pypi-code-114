# # keep imports below to expose api in `icclim` namespace
# from __future__ import annotations
# from icclim.main import index, list_indices
# from .pre_processing.rechunk import create_optimized_zarr_store
#
#
# import logging
# import time
# from datetime import datetime
# from typing import Callable, Dict, List, Optional, Tuple, Union
# from warnings import warn
#
# import xarray as xr
# import xclim
# from xarray.core.dataarray import DataArray
# from xarray.core.dataset import Dataset
#
# from icclim.ecad_functions import IndexConfig
# from icclim.icclim_exceptions import InvalidIcclimArgumentError
#
#
# def indice(*args, **kwargs):
#     """
#     Deprecated proxy for `icclim.index` function.
#     To be deleted in a futur version.
#     """
#     from icclim.icclim_logger import IcclimLogger, Verbosity
#     log: IcclimLogger = IcclimLogger.get_instance(Verbosity.LOW)
#     log.deprecation_warning(old="icclim.indice", new="icclim.index")
#     return index(*args, **kwargs)
#
# def list_indices() -> list[str]:
#     """
#     List the available indices.
#
#     Returns
#     -------
#         A list of indices to be used as input of icclim.index `index_name` parameter.
#     """
#     from icclim.models.ecad_indices import EcadIndex
#     return [f"{i.short_name}: {i.definition}" for i in EcadIndex]
