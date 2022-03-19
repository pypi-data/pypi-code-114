from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dlist:
	"""Dlist commands group definition. 9 total commands, 1 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dlist", core, parent)

	@property
	def data(self):
		"""data commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:DM:DLISt:CATalog \n
		Snippet: value: List[str] = driver.source.bb.dm.dlist.get_catalog() \n
		Reads out the list files present in the default directory (see method RsSmcv.MassMemory.currentDirectory) .
			Table Header: List type / Command / File extension \n
			- Data list / ...:DLISt... / *.dm_iqd
			- Control list / ...:CLISt... / *.dm_iqc
			- User filter files / ...:FLISt... / *.vaf
			- User mapping lists / ...:MLISt... / *.vam
		Refer to 'Accessing files in the default or in a specified directory' for general information on file handling in the
		default and a specific directory. \n
			:return: catalog: 'filename1,filename2,...' Returns a string of file names separated by commas.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:DLISt:CATalog?')
		return Conversions.str_to_str_list(response)

	def copy(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:DLISt:COPY \n
		Snippet: driver.source.bb.dm.dlist.copy(filename = '1') \n
		Copies the selected data list (*.dm_iqd) / control list (*.dm_iqc) as a new list with name specified by <Filename>. If a
		list with the specified name exists, it is overwritten. If it does not yet exist, it is created. The source file has to
		be available in the default directory (see method RsSmcv.MassMemory.currentDirectory) . Refer to 'Accessing files in the
		default or in a specified directory' for general information on file handling in the default and a specific directory. \n
			:param filename: string
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:DLISt:COPY {param}')

	def delete(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:DLISt:DELete \n
		Snippet: driver.source.bb.dm.dlist.delete(filename = '1') \n
		Deletes the specified list from the default directory (see method RsSmcv.MassMemory.currentDirectory) or from the
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
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:DLISt:DELete {param}')

	def get_free(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DM:DLISt:FREE \n
		Snippet: value: int = driver.source.bb.dm.dlist.get_free() \n
		Queries the list free memory.
			Table Header: List type / Command / File extension \n
			- Data list / ...:DLISt... / *.dm_iqd
			- Control list / ...:CLISt... / *.dm_iqc
			- User filter files / ...:FLISt... / *.vaf
			- User mapping lists / ...:MLISt... / *.vam \n
			:return: free: integer Range: 0 to INT_MAX
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:DLISt:FREE?')
		return Conversions.str_to_int(response)

	def get_points(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DM:DLISt:POINts \n
		Snippet: value: int = driver.source.bb.dm.dlist.get_points() \n
		Defines the number of bits in the selected data list to be utilized. When a list is being filled with block data, this
		data is only ever sent in multiples of 8 bits. However the exact number of bits to be exploited can be set to a different
		figure. The superfluous bits in the list are then ignored. \n
			:return: points: integer Range: 0 to INT_MAX
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:DLISt:POINts?')
		return Conversions.str_to_int(response)

	def set_points(self, points: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:DLISt:POINts \n
		Snippet: driver.source.bb.dm.dlist.set_points(points = 1) \n
		Defines the number of bits in the selected data list to be utilized. When a list is being filled with block data, this
		data is only ever sent in multiples of 8 bits. However the exact number of bits to be exploited can be set to a different
		figure. The superfluous bits in the list are then ignored. \n
			:param points: integer Range: 0 to INT_MAX
		"""
		param = Conversions.decimal_value_to_str(points)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:DLISt:POINts {param}')

	def get_select(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:DM:DLISt:SELect \n
		Snippet: value: str = driver.source.bb.dm.dlist.get_select() \n
		Selects the specified list file from the default directory (see method RsSmcv.MassMemory.currentDirectory) or in the
		directory specified with the complete file path. If a list with the specified name does not yet exist, it is created. The
		file extension can be omitted. Refer to 'Accessing files in the default or in a specified directory' for general
		information on file handling in the default and a specific directory.
			Table Header: List type / Command / File extension \n
			- Data list / ...:DLISt... / *.dm_iqd
			- Control list / ...:CLISt... / *.dm_iqc
			- User standard / ...:ULISt... / *.dm_stu
			- User filter files / ...:FLISt... / *.vaf
			- User mapping lists / ...:MLISt... / *.vam \n
			:return: select: list name
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:DLISt:SELect?')
		return trim_str_response(response)

	def set_select(self, select: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:DLISt:SELect \n
		Snippet: driver.source.bb.dm.dlist.set_select(select = '1') \n
		Selects the specified list file from the default directory (see method RsSmcv.MassMemory.currentDirectory) or in the
		directory specified with the complete file path. If a list with the specified name does not yet exist, it is created. The
		file extension can be omitted. Refer to 'Accessing files in the default or in a specified directory' for general
		information on file handling in the default and a specific directory.
			Table Header: List type / Command / File extension \n
			- Data list / ...:DLISt... / *.dm_iqd
			- Control list / ...:CLISt... / *.dm_iqc
			- User standard / ...:ULISt... / *.dm_stu
			- User filter files / ...:FLISt... / *.vaf
			- User mapping lists / ...:MLISt... / *.vam \n
			:param select: list name
		"""
		param = Conversions.value_to_quoted_str(select)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:DLISt:SELect {param}')

	def get_tag(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:DM:DLISt:TAG \n
		Snippet: value: str = driver.source.bb.dm.dlist.get_tag() \n
		Queries the content of the specified tag in the selected file. \n
			:return: tag: control list,tag name Refer to 'Tags for waveforms, data and control lists' for description of the available tag formats.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:DLISt:TAG?')
		return trim_str_response(response)

	def clone(self) -> 'Dlist':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dlist(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
