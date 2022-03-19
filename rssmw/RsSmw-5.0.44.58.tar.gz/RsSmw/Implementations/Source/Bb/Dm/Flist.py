from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Flist:
	"""Flist commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("flist", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:DM:FLISt:CATalog \n
		Snippet: value: List[str] = driver.source.bb.dm.flist.get_catalog() \n
		Reads out the list files present in the default directory (see method RsSmw.MassMemory.currentDirectory) .
			Table Header: List type / Command / File extension \n
			- Data list / ...:DLISt... / *.dm_iqd
			- Control list / ...:CLISt... / *.dm_iqc
			- User filter files / ...:FLISt... / *.vaf
			- User mapping lists / ...:MLISt... / *.vam
		Refer to 'Accessing files in the default or in a specified directory' for general information on file handling in the
		default and a specific directory. \n
			:return: catalog: 'filename1,filename2,...' Returns a string of file names separated by commas.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:FLISt:CATalog?')
		return Conversions.str_to_str_list(response)

	def delete(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:FLISt:DELete \n
		Snippet: driver.source.bb.dm.flist.delete(filename = '1') \n
		Deletes the specified list from the default directory (see method RsSmw.MassMemory.currentDirectory) or from the
		directory specified with the complete file path. Refer to 'Accessing files in the default or in a specified directory'
		for general information on file handling in the default and a specific directory.
			Table Header: List type / Command / File extension \n
			- Data list / ...:DLISt... / *.dm_iqd
			- Control list / ...:CLISt... / *.dm_iqc
			- User standard / ...:ULISt... / *.dm_stu
			- User filter files / ...:FLISt... / *.vaf
			- User mapping lists / ...:MLISt... / *.vam \n
			:param filename: string
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:FLISt:DELete {param}')

	def get_free(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DM:FLISt:FREE \n
		Snippet: value: int = driver.source.bb.dm.flist.get_free() \n
		Queries the list free memory.
			Table Header: List type / Command / File extension \n
			- Data list / ...:DLISt... / *.dm_iqd
			- Control list / ...:CLISt... / *.dm_iqc
			- User filter files / ...:FLISt... / *.vaf
			- User mapping lists / ...:MLISt... / *.vam \n
			:return: free: integer Range: 0 to INT_MAX
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:FLISt:FREE?')
		return Conversions.str_to_int(response)

	def get_points(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DM:FLISt:POINts \n
		Snippet: value: int = driver.source.bb.dm.flist.get_points() \n
		Queries the user modulation mapping/user filter list length. \n
			:return: points: integer Range: max
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:FLISt:POINts?')
		return Conversions.str_to_int(response)

	def get_select(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:DM:FLISt:SELect \n
		Snippet: value: str = driver.source.bb.dm.flist.get_select() \n
		Selects the specified list file from the default directory (see method RsSmw.MassMemory.currentDirectory) or in the
		directory specified with the complete file path. If a list with the specified name does not yet exist, it is created. The
		file extension can be omitted. Refer to 'Accessing files in the default or in a specified directory' for general
		information on file handling in the default and a specific directory.
			Table Header: List type / Command / File extension \n
			- Data list / ...:DLISt... / *.dm_iqd
			- Control list / ...:CLISt... / *.dm_iqc
			- User standard / ...:ULISt... / *.dm_stu
			- User filter files / ...:FLISt... / *.vaf
			- User mapping lists / ...:MLISt... / *.vam \n
			:return: filename: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:FLISt:SELect?')
		return trim_str_response(response)

	def set_select(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:FLISt:SELect \n
		Snippet: driver.source.bb.dm.flist.set_select(filename = '1') \n
		Selects the specified list file from the default directory (see method RsSmw.MassMemory.currentDirectory) or in the
		directory specified with the complete file path. If a list with the specified name does not yet exist, it is created. The
		file extension can be omitted. Refer to 'Accessing files in the default or in a specified directory' for general
		information on file handling in the default and a specific directory.
			Table Header: List type / Command / File extension \n
			- Data list / ...:DLISt... / *.dm_iqd
			- Control list / ...:CLISt... / *.dm_iqc
			- User standard / ...:ULISt... / *.dm_stu
			- User filter files / ...:FLISt... / *.vaf
			- User mapping lists / ...:MLISt... / *.vam \n
			:param filename: list name
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:FLISt:SELect {param}')
