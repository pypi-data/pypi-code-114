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
		"""SCPI: [SOURce<HW>]:BB:J83B:SETTing:CATalog \n
		Snippet: value: List[str] = driver.source.bb.j83B.setting.get_catalog() \n
		Queries the files with settings in the default directory. Listed are files with the file extension *.J83B.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:return: catalog: filename1,filename2,... Returns a string of filenames separated by commas.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:J83B:SETTing:CATalog?')
		return Conversions.str_to_str_list(response)

	def delete(self, delete: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:J83B:SETTing:DELete \n
		Snippet: driver.source.bb.j83B.setting.delete(delete = '1') \n
		Deletes the selected file from the default or the specified directory. Deleted are files with extension *.J83B. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:param delete: 'filename' Filename or complete file path; file extension can be omitted
		"""
		param = Conversions.value_to_quoted_str(delete)
		self._core.io.write(f'SOURce<HwInstance>:BB:J83B:SETTing:DELete {param}')

	def get_load(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:J83B:SETTing:LOAD \n
		Snippet: value: str = driver.source.bb.j83B.setting.get_load() \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.J83B. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:return: recall: 'filename' Filename or complete file path; file extension can be omitted.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:J83B:SETTing:LOAD?')
		return trim_str_response(response)

	def set_load(self, recall: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:J83B:SETTing:LOAD \n
		Snippet: driver.source.bb.j83B.setting.set_load(recall = '1') \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.J83B. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:param recall: 'filename' Filename or complete file path; file extension can be omitted.
		"""
		param = Conversions.value_to_quoted_str(recall)
		self._core.io.write(f'SOURce<HwInstance>:BB:J83B:SETTing:LOAD {param}')

	def get_store(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:J83B:SETTing:STORe \n
		Snippet: value: str = driver.source.bb.j83B.setting.get_store() \n
		Saves the current settings into the selected file; the file extension (*.J83B) is assigned automatically.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:return: save: 'filename' Filename or complete file path
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:J83B:SETTing:STORe?')
		return trim_str_response(response)

	def set_store(self, save: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:J83B:SETTing:STORe \n
		Snippet: driver.source.bb.j83B.setting.set_store(save = '1') \n
		Saves the current settings into the selected file; the file extension (*.J83B) is assigned automatically.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:param save: 'filename' Filename or complete file path
		"""
		param = Conversions.value_to_quoted_str(save)
		self._core.io.write(f'SOURce<HwInstance>:BB:J83B:SETTing:STORe {param}')
