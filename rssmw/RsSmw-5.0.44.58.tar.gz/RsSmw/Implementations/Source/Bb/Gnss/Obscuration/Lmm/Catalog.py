from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def get_predefined(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:GNSS:OBSCuration:LMM:CATalog:PREDefined \n
		Snippet: value: List[str] = driver.source.bb.gnss.obscuration.lmm.catalog.get_predefined() \n
		Queries the names of predefined files in the system directory.
			INTRO_CMD_HELP: Listed are only the following file types: \n
			- Obstacles description files (*.rs_obst)
			- Roadside buildings description files (*.rs_buil)
			- Land mobile multipath (LMM) files (*.lmm)  \n
			:return: gnss_obsc_lmm_cat_names: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:OBSCuration:LMM:CATalog:PREDefined?')
		return Conversions.str_to_str_list(response)

	def get_user(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:GNSS:OBSCuration:LMM:CATalog:USER \n
		Snippet: value: List[str] = driver.source.bb.gnss.obscuration.lmm.catalog.get_user() \n
		Queries the names of the user-defined files in the default directory. The default directory is set using command method
		RsSmw.MassMemory.currentDirectory.
			INTRO_CMD_HELP: Listed are the following file types: \n
			- Obstacles description files (*.rs_obst)
			- Roadside buildings description files (*.rs_buil)
			- Land mobile multipath (LMM) files (*.lmm)  \n
			:return: gnss_obsc_lmm_user_cat_names: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:OBSCuration:LMM:CATalog:USER?')
		return Conversions.str_to_str_list(response)
