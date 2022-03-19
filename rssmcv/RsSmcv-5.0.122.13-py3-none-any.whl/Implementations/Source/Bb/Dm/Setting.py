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
		"""SCPI: [SOURce<HW>]:BB:DM:SETTing:CATalog \n
		Snippet: value: List[str] = driver.source.bb.dm.setting.get_catalog() \n
		Queries the files with digital modulation respectively user standard settings in the default directory. Listed are files
		with the file extension *.dm and *.dm_stu. Refer to 'Accessing files in the default or in a specified directory' for
		general information on file handling in the default and a specific directory. \n
			:return: catalog: 'filename1,filename2,...' Returns a string of file names separated by commas.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:SETTing:CATalog?')
		return Conversions.str_to_str_list(response)

	def delete(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:SETTing:DELete \n
		Snippet: driver.source.bb.dm.setting.delete(filename = '1') \n
		Deletes the selected file from the default or specified directory. Deleted are files with the file extension *.
		dm respectively *.dm_stu. Refer to 'Accessing files in the default or in a specified directory' for general information
		on file handling in the default and a specific directory. \n
			:param filename: string
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:SETTing:DELete {param}')

	def load(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:SETTing:LOAD \n
		Snippet: driver.source.bb.dm.setting.load(filename = '1') \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.dm respectively *.
		dm_stu. Refer to 'Accessing files in the default or in a specified directory' for general information on file handling in
		the default and a specific directory. \n
			:param filename: string
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:SETTing:LOAD {param}')

	def set_store(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:SETTing:STORe \n
		Snippet: driver.source.bb.dm.setting.set_store(filename = '1') \n
		Stores the current settings into the selected file; the file extension (*.dm respectively *.
		dm_stu) is assigned automatically. Refer to 'Accessing files in the default or in a specified directory' for general
		information on file handling in the default and a specific directory. \n
			:param filename: string
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:SETTing:STORe {param}')
