from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Predefined:
	"""Predefined commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("predefined", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:NOISe:PHASenoise:SHAPe:PREDefined:CATalog \n
		Snippet: value: List[str] = driver.source.noise.phasenoise.shape.predefined.get_catalog() \n
		Queries the files with predefined settings. Listed are files with the file extension *.fcf. Refer to 'Accessing files in
		the default or in a specified directory' for general information on file handling in the default and in a specific
		directory. \n
			:return: nois_phas_ssb_shap_pre_def_cat_nam: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:NOISe:PHASenoise:SHAPe:PREDefined:CATalog?')
		return Conversions.str_to_str_list(response)
