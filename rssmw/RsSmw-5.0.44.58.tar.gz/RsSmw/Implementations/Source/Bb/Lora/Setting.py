from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Setting:
	"""Setting commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("setting", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:LORA:SETTing:CATalog \n
		Snippet: value: List[str] = driver.source.bb.lora.setting.get_catalog() \n
		Queries the files with settings in the default directory. Listed are files with the file extension *.lora.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:return: catalog: filename1,filename2,... Returns a string of filenames separated by commas.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:LORA:SETTing:CATalog?')
		return Conversions.str_to_str_list(response)

	def get_delete(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:LORA:SETTing:DELete \n
		Snippet: value: str = driver.source.bb.lora.setting.get_delete() \n
		Deletes the selected file from the default or the specified directory. Deleated are files with extension *.lora. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:return: filename: 'filename' Filename or complete file path; file extension can be omitted
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:LORA:SETTing:DELete?')
		return trim_str_response(response)

	def set_delete(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:LORA:SETTing:DELete \n
		Snippet: driver.source.bb.lora.setting.set_delete(filename = '1') \n
		Deletes the selected file from the default or the specified directory. Deleated are files with extension *.lora. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:param filename: 'filename' Filename or complete file path; file extension can be omitted
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:LORA:SETTing:DELete {param}')

	def get_load(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:LORA:SETTing:LOAD \n
		Snippet: value: str = driver.source.bb.lora.setting.get_load() \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.lora. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:return: filename: 'filename' Filename or complete file path; file extension can be omitted
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:LORA:SETTing:LOAD?')
		return trim_str_response(response)

	def set_load(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:LORA:SETTing:LOAD \n
		Snippet: driver.source.bb.lora.setting.set_load(filename = '1') \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.lora. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:param filename: 'filename' Filename or complete file path; file extension can be omitted
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:LORA:SETTing:LOAD {param}')

	def set_store(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:LORA:SETTing:STORe \n
		Snippet: driver.source.bb.lora.setting.set_store(filename = '1') \n
		Saves the current settings into the selected file; the file extension (*.lora) is assigned automatically.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:param filename: 'filename' Filename or complete file path
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:LORA:SETTing:STORe {param}')
