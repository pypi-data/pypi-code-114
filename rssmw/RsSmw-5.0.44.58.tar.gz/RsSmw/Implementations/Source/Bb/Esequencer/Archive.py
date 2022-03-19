from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Archive:
	"""Archive commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("archive", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:ARCHive:CATalog \n
		Snippet: value: List[str] = driver.source.bb.esequencer.archive.get_catalog() \n
		Queries the available extended sequencer archive files in the default directory. Listed are files with the file extension
		*.ps_arc. Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in
		the default and in a specific directory. \n
			:return: catalog: string Returns a string of file names separated by commas.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ESEQuencer:ARCHive:CATalog?')
		return Conversions.str_to_str_list(response)

	def load(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:ARCHive:LOAD \n
		Snippet: driver.source.bb.esequencer.archive.load(filename = '1') \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.ps_arc. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:param filename: string File name or complete file path; file extension can be omitted
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:ARCHive:LOAD {param}')

	def set_store(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:ARCHive:STORe \n
		Snippet: driver.source.bb.esequencer.archive.set_store(filename = '1') \n
		Stores the current user mode configuration in the selected file, including all used extended sequencer files. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:param filename: string File name or complete file path
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:ARCHive:STORe {param}')
