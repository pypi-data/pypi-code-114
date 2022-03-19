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
		"""SCPI: [SOURce<HW>]:BB:ISDBt:SETTing:CATalog \n
		Snippet: value: List[str] = driver.source.bb.isdbt.setting.get_catalog() \n
		No command help available \n
			:return: isdbt_cat_name: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:SETTing:CATalog?')
		return Conversions.str_to_str_list(response)

	def get_delete(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:SETTing:DELete \n
		Snippet: value: str = driver.source.bb.isdbt.setting.get_delete() \n
		Deletes the selected file from the default or the specified directory. Deleted are files with extension *.isdbt. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:return: delete: 'filename' Filename or complete file path; file extension can be omitted
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:SETTing:DELete?')
		return trim_str_response(response)

	def set_delete(self, delete: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:SETTing:DELete \n
		Snippet: driver.source.bb.isdbt.setting.set_delete(delete = '1') \n
		Deletes the selected file from the default or the specified directory. Deleted are files with extension *.isdbt. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:param delete: 'filename' Filename or complete file path; file extension can be omitted
		"""
		param = Conversions.value_to_quoted_str(delete)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:SETTing:DELete {param}')

	def get_load(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:SETTing:LOAD \n
		Snippet: value: str = driver.source.bb.isdbt.setting.get_load() \n
		Accesses the 'Save/Recall' dialog, that is the standard instrument function for saving and recalling the complete
		dialog-related settings in a file. The provided navigation possibilities in the dialog are self-explanatory. The settings
		are saved in a file with predefined extension. You can define the filename and the directory, in that you want to save
		the file. . \n
			:return: isdbt_recall: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:SETTing:LOAD?')
		return trim_str_response(response)

	def set_load(self, isdbt_recall: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:SETTing:LOAD \n
		Snippet: driver.source.bb.isdbt.setting.set_load(isdbt_recall = '1') \n
		Accesses the 'Save/Recall' dialog, that is the standard instrument function for saving and recalling the complete
		dialog-related settings in a file. The provided navigation possibilities in the dialog are self-explanatory. The settings
		are saved in a file with predefined extension. You can define the filename and the directory, in that you want to save
		the file. . \n
			:param isdbt_recall: string
		"""
		param = Conversions.value_to_quoted_str(isdbt_recall)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:SETTing:LOAD {param}')

	def get_store(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:SETTing:STORe \n
		Snippet: value: str = driver.source.bb.isdbt.setting.get_store() \n
		Accesses the 'Save/Recall' dialog, that is the standard instrument function for saving and recalling the complete
		dialog-related settings in a file. The provided navigation possibilities in the dialog are self-explanatory. The settings
		are saved in a file with predefined extension. You can define the filename and the directory, in that you want to save
		the file. . \n
			:return: isdbt_save: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:SETTing:STORe?')
		return trim_str_response(response)

	def set_store(self, isdbt_save: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:SETTing:STORe \n
		Snippet: driver.source.bb.isdbt.setting.set_store(isdbt_save = '1') \n
		Accesses the 'Save/Recall' dialog, that is the standard instrument function for saving and recalling the complete
		dialog-related settings in a file. The provided navigation possibilities in the dialog are self-explanatory. The settings
		are saved in a file with predefined extension. You can define the filename and the directory, in that you want to save
		the file. . \n
			:param isdbt_save: string
		"""
		param = Conversions.value_to_quoted_str(isdbt_save)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:SETTing:STORe {param}')
