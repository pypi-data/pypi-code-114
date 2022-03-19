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
		"""SCPI: [SOURce<HW>]:BB:EVDO:SETTing:CATalog \n
		Snippet: value: List[str] = driver.source.bb.evdo.setting.get_catalog() \n
		Queries the files with 1xEV-DO settings (file extension *.1xevdo) in the default or the specified directory. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and a
		specific directory. \n
			:return: catalog: 'filename1,filename2,...' Returns a string of filenames separated by commas.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EVDO:SETTing:CATalog?')
		return Conversions.str_to_str_list(response)

	def delete(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:SETTing:DELete \n
		Snippet: driver.source.bb.evdo.setting.delete(filename = '1') \n
		Deletes the selected file from the default or specified directory. Deleted are files with the file extension *.1xevdo.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and a specific directory. \n
			:param filename: string
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:SETTing:DELete {param}')

	def load(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:SETTing:LOAD \n
		Snippet: driver.source.bb.evdo.setting.load(filename = '1') \n
		Loads the selected file from the default or the specified directory. Loads are files with extension *.1xevdo. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and a
		specific directory. \n
			:param filename: string
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:SETTing:LOAD {param}')

	def set_store(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:SETTing:STORe \n
		Snippet: driver.source.bb.evdo.setting.set_store(filename = '1') \n
		Stores the current settings into the selected file; the file extension *.1xevdo is assigned automatically.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and a specific directory. \n
			:param filename: string
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:SETTing:STORe {param}')
