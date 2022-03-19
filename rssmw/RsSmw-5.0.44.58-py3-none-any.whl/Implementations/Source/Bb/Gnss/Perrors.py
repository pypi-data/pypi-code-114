from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Perrors:
	"""Perrors commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("perrors", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:GNSS:PERRors:CATalog \n
		Snippet: value: List[str] = driver.source.bb.gnss.perrors.get_catalog() \n
		Queries the names of the pseudorange errors files in the default or in a specific directory. Listed are files with the
		file extension *.rs_perr. Refer to 'Accessing Files in the Default or Specified Directory' for general information on
		file handling in the default and in a specific directory. \n
			:return: gnss_sv_pseudorange_cat_names: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:PERRors:CATalog?')
		return Conversions.str_to_str_list(response)
