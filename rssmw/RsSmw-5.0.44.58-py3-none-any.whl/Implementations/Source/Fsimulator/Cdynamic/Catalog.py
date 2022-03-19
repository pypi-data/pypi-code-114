from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def get_user(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:FSIMulator:CDYNamic:CATalog:USER \n
		Snippet: value: List[str] = driver.source.fsimulator.cdynamic.catalog.get_user() \n
		Queries the files with user-defined customized dynamic fading settings in the default directory. Listed are files with
		the file extension *.fad_udyn. Refer to 'Accessing Files in the Default or Specified Directory' for general information
		on file handling in the default and in a specific directory. \n
			:return: filenames: filename1,filename2,... Returns a string of filenames separated by commas.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:CDYNamic:CATalog:USER?')
		return Conversions.str_to_str_list(response)

	def get_value(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:FSIMulator:CDYNamic:CATalog \n
		Snippet: value: List[str] = driver.source.fsimulator.cdynamic.catalog.get_value() \n
		Queries the predefined files with customized dynamic fading settings. Listed are files with the file extension *.fad_udyn. \n
			:return: filenames: filename1,filename2,... Returns a string of filenames separated by commas.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:CDYNamic:CATalog?')
		return Conversions.str_to_str_list(response)
