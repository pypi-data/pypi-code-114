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
		"""SCPI: [SOURce<HW>]:BB:TETRa:SETTing:CATalog \n
		Snippet: value: List[str] = driver.source.bb.tetra.setting.get_catalog() \n
		Queries the files with settings in the default directory. Listed are files with the file extension *.tetra.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:return: catalog: filename1,filename2,... Returns a string of file names separated by commas.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TETRa:SETTing:CATalog?')
		return Conversions.str_to_str_list(response)

	def delete(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SETTing:DELete \n
		Snippet: driver.source.bb.tetra.setting.delete(filename = '1') \n
		Deletes the selected file in the specified directory. Deleted are files with the file extension *.tetra. \n
			:param filename: file name file name or complete file path
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:SETTing:DELete {param}')

	def load(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SETTing:LOAD \n
		Snippet: driver.source.bb.tetra.setting.load(filename = '1') \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.tetra. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:param filename: string file name or complete file path
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:SETTing:LOAD {param}')

	def set_store(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SETTing:STORe \n
		Snippet: driver.source.bb.tetra.setting.set_store(filename = '1') \n
		Stores the current settings into the selected file; the file extension (*.tetra) is assigned automatically.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:param filename: string file name or complete file path
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:SETTing:STORe {param}')
