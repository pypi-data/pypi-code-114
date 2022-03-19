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
		"""SCPI: [SOURce<HW>]:BB:WLAD:SETTing:CATalog \n
		Snippet: value: List[str] = driver.source.bb.wlad.setting.get_catalog() \n
		Reads out the files with IEEE 802.11ad settings in the default directory. The default directory is set using the command
		method RsSmw.MassMemory.currentDirectory. Only files with the file extension *.wlanad are listed. \n
			:return: catalog: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:SETTing:CATalog?')
		return Conversions.str_to_str_list(response)

	def delete(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:SETTing:DELete \n
		Snippet: driver.source.bb.wlad.setting.delete(filename = '1') \n
		Deletes the selected file with IEEE 802.11ad settings. The directory is set using command method RsSmw.MassMemory.
		currentDirectory. A path can also be specified, in which case the files in the specified directory are read. The file
		extension may be omitted. Only files with the file extension *.wlanad are listed and can be deleted. \n
			:param filename: string
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:SETTing:DELete {param}')

	def load(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:SETTing:LOAD \n
		Snippet: driver.source.bb.wlad.setting.load(filename = '1') \n
		Loads the selected file with IEEE 802.11ad settings. The directory is set using the command method RsSmw.MassMemory.
		currentDirectory. A path can also be specified, in which case the files in the specified directory are read. The file
		extension may be omitted. Only files with the file extension *.wlanad are loaded.. \n
			:param filename: string
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:SETTing:LOAD {param}')

	def set_store(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:SETTing:STORe \n
		Snippet: driver.source.bb.wlad.setting.set_store(filename = '1') \n
		Stores the current IEEE 802.11ad settings into the selected file. The directory is set using the command method RsSmw.
		MassMemory.currentDirectory. A path can also be specified, in which case the files in the specified directory are read.
		Only the file name has to be entered. WLAD settings are stored as files with the specific file extensions *.wlanad. \n
			:param filename: string
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:SETTing:STORe {param}')
