from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Setting:
	"""Setting commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("setting", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:C2K:SETTing:CATalog \n
		Snippet: value: List[str] = driver.source.bb.c2K.setting.get_catalog() \n
		Queries the files with settings in the default directory. Listed are files with the file extension *.cdma2k. For general
		information on file handling in the default and in a specific directory, see section 'MMEMory Subsystem' in the R&S SMW
		operating manual. \n
			:return: catalog: filename1,filename2,... Returns a string of filenames separated by commas.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:SETTing:CATalog?')
		return Conversions.str_to_str_list(response)

	def delete(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:SETTing:DELete \n
		Snippet: driver.source.bb.c2K.setting.delete(filename = '1') \n
		Deletes the selected file from the default or the specified directory. Deleted are files with extension *.cdma2k. \n
			:param filename: string
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:SETTing:DELete {param}')

	def load(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:SETTing:LOAD \n
		Snippet: driver.source.bb.c2K.setting.load(filename = '1') \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.cdma2k. \n
			:param filename: 'filename' Filename or complete file path; file extension can be omitted
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:SETTing:LOAD {param}')

	def set_store(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:SETTing:STORe \n
		Snippet: driver.source.bb.c2K.setting.set_store(filename = '1') \n
		Stores the current settings into the selected file; the file extension (*.cdma2k) is assigned automatically. \n
			:param filename: string Filename or complete file path
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:SETTing:STORe {param}')
