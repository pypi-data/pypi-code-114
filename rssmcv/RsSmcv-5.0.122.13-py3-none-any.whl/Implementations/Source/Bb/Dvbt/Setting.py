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
		"""SCPI: [SOURce<HW>]:BB:DVBT:SETTing:CATalog \n
		Snippet: value: List[str] = driver.source.bb.dvbt.setting.get_catalog() \n
		Queries the files with settings in the default directory. Listed are files with the file extension *.dvbt.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:return: dvbt_cat_name: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:SETTing:CATalog?')
		return Conversions.str_to_str_list(response)

	def delete(self, delete: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:SETTing:DELete \n
		Snippet: driver.source.bb.dvbt.setting.delete(delete = '1') \n
		Deletes the selected file from the default or the specified directory. Deleted are files with extension *.dvbt. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:param delete: 'filename' Filename or complete file path; file extension can be omitted
		"""
		param = Conversions.value_to_quoted_str(delete)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:SETTing:DELete {param}')

	def get_load(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:DVBT:SETTing:LOAD \n
		Snippet: value: str = driver.source.bb.dvbt.setting.get_load() \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.dvbt. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:return: dvbt_recall: 'filename' Filename or complete file path; file extension can be omitted
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:SETTing:LOAD?')
		return trim_str_response(response)

	def set_load(self, dvbt_recall: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:SETTing:LOAD \n
		Snippet: driver.source.bb.dvbt.setting.set_load(dvbt_recall = '1') \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.dvbt. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:param dvbt_recall: 'filename' Filename or complete file path; file extension can be omitted
		"""
		param = Conversions.value_to_quoted_str(dvbt_recall)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:SETTing:LOAD {param}')

	def get_store(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:DVBT:SETTing:STORe \n
		Snippet: value: str = driver.source.bb.dvbt.setting.get_store() \n
		Saves the current settings into the selected file; the file extension (*.dvbt) is assigned automatically.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:return: dvbt_save: 'filename'
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:SETTing:STORe?')
		return trim_str_response(response)

	def set_store(self, dvbt_save: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:SETTing:STORe \n
		Snippet: driver.source.bb.dvbt.setting.set_store(dvbt_save = '1') \n
		Saves the current settings into the selected file; the file extension (*.dvbt) is assigned automatically.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:param dvbt_save: 'filename'
		"""
		param = Conversions.value_to_quoted_str(dvbt_save)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:SETTing:STORe {param}')
