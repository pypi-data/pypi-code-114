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
		"""SCPI: [SOURce<HW>]:IQ:DPD:SETTing:CATalog \n
		Snippet: value: List[str] = driver.source.iq.dpd.setting.get_catalog() \n
		Queries the files with digital predistortion setting in the default directory. Listed are files with the file extension *.
		dpd. Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the
		default and in a specific directory. \n
			:return: catalog: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DPD:SETTing:CATalog?')
		return Conversions.str_to_str_list(response)

	def delete(self, filename: str) -> None:
		"""SCPI: [SOURce]:IQ:DPD:SETTing:DELete \n
		Snippet: driver.source.iq.dpd.setting.delete(filename = '1') \n
		Deletes the selected file from the default or specified directory. Deleted are files with the file extension *.dpd. Refer
		to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in
		a specific directory. \n
			:param filename: 'filename' Filename or complete file path
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce:IQ:DPD:SETTing:DELete {param}')

	def load(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DPD:SETTing:LOAD \n
		Snippet: driver.source.iq.dpd.setting.load(filename = '1') \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.dpd.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:param filename: 'filename' Filename or complete file path
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DPD:SETTing:LOAD {param}')

	def set_store(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DPD:SETTing:STORe \n
		Snippet: driver.source.iq.dpd.setting.set_store(filename = '1') \n
		Stores the current settings into the selected file; the file extension (*.dpd) is assigned automatically.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:param filename: 'filename' Filename or complete file path
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DPD:SETTing:STORe {param}')
