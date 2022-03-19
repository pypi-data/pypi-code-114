from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Setting:
	"""Setting commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("setting", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:SETTing:CATalog \n
		Snippet: value: List[str] = driver.source.bb.radio.fm.setting.get_catalog() \n
		Queries the files with settings in the default directory. Listed are files with the file extension *.am/fm/rds. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:return: tx_audio_bc_fm_cat_name: filename1,filename2,... Returns a string of filenames separated by commas.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:SETTing:CATalog?')
		return Conversions.str_to_str_list(response)

	def delete(self, fm_del: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:SETTing:DELete \n
		Snippet: driver.source.bb.radio.fm.setting.delete(fm_del = '1') \n
		Deletes the selected file from the default or the specified directory. Deleted are files with extension *.am/fm/rds.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:param fm_del: 'filename' Filename or complete file path; file extension can be omitted
		"""
		param = Conversions.value_to_quoted_str(fm_del)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:SETTing:DELete {param}')

	def get_load(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:SETTing:LOAD \n
		Snippet: value: str = driver.source.bb.radio.fm.setting.get_load() \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.am/fm/rds. Refer
		to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in
		a specific directory. \n
			:return: fm_rcl: 'filename' Filename or complete file path; file extension can be omitted
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:SETTing:LOAD?')
		return trim_str_response(response)

	def set_load(self, fm_rcl: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:SETTing:LOAD \n
		Snippet: driver.source.bb.radio.fm.setting.set_load(fm_rcl = '1') \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.am/fm/rds. Refer
		to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in
		a specific directory. \n
			:param fm_rcl: 'filename' Filename or complete file path; file extension can be omitted
		"""
		param = Conversions.value_to_quoted_str(fm_rcl)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:SETTing:LOAD {param}')

	def get_store(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:SETTing:STORe \n
		Snippet: value: str = driver.source.bb.radio.fm.setting.get_store() \n
		Saves the current settings into the selected file; the file extension (*.am/fm/rds) is assigned automatically. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:return: fm_sav: 'filename' Filename or complete file path
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:SETTing:STORe?')
		return trim_str_response(response)

	def set_store(self, fm_sav: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:SETTing:STORe \n
		Snippet: driver.source.bb.radio.fm.setting.set_store(fm_sav = '1') \n
		Saves the current settings into the selected file; the file extension (*.am/fm/rds) is assigned automatically. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:param fm_sav: 'filename' Filename or complete file path
		"""
		param = Conversions.value_to_quoted_str(fm_sav)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:SETTing:STORe {param}')
