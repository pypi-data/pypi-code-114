from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Setting:
	"""Setting commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("setting", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:SETTing:CATalog \n
		Snippet: value: List[str] = driver.source.bb.arbitrary.mcarrier.setting.get_catalog() \n
		Queries the available settings files in the specified default directory. Only files with the file extension *.
		arb_multcarr are listed. \n
			:return: catalog: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:MCARrier:SETTing:CATalog?')
		return Conversions.str_to_str_list(response)

	def load(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:SETTing:LOAD \n
		Snippet: driver.source.bb.arbitrary.mcarrier.setting.load(filename = '1') \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.arb_multcarr.
		Refer to 'Accessing files in the default or in a specified directory' for general information on file handling in the
		default and in a specific directory. \n
			:param filename: 'filename' Filename or complete file path; file extension can be omitted
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:SETTing:LOAD {param}')

	def set_store(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:SETTing:STORe \n
		Snippet: driver.source.bb.arbitrary.mcarrier.setting.set_store(filename = '1') \n
		Stores the current settings into the selected file; the file extension (*.arb_multcarr) is assigned automatically. Refer
		to 'Accessing files in the default or in a specified directory' for general information on file handling in the default
		and in a specific directory. \n
			:param filename: string Filename or complete file path
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:SETTing:STORe {param}')
