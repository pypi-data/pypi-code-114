from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Types import DataType
from ...Internal.Utilities import trim_str_response
from ...Internal.ArgSingleList import ArgSingleList
from ...Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MassMemory:
	"""MassMemory commands group definition. 14 total commands, 4 Subgroups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("massMemory", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import Catalog
			self._catalog = Catalog(self._core, self._cmd_group)
		return self._catalog

	@property
	def dcatalog(self):
		"""dcatalog commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_dcatalog'):
			from .Dcatalog import Dcatalog
			self._dcatalog = Dcatalog(self._core, self._cmd_group)
		return self._dcatalog

	@property
	def load(self):
		"""load commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_load'):
			from .Load import Load
			self._load = Load(self._core, self._cmd_group)
		return self._load

	@property
	def store(self):
		"""store commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_store'):
			from .Store import Store
			self._store = Store(self._core, self._cmd_group)
		return self._store

	def get_current_directory(self) -> str:
		"""SCPI: MMEMory:CDIRectory \n
		Snippet: value: str = driver.massMemory.get_current_directory() \n
		Changes the default directory for mass memory storage. The directory is used for all subsequent MMEM commands if no path
		is specified with them. \n
			:return: directory: directory_name String containing the path to another directory. The path can be relative or absolute. To change to a higher directory, use two dots '..' .
		"""
		response = self._core.io.query_str('MMEMory:CDIRectory?')
		return trim_str_response(response)

	def set_current_directory(self, directory: str) -> None:
		"""SCPI: MMEMory:CDIRectory \n
		Snippet: driver.massMemory.set_current_directory(directory = '1') \n
		Changes the default directory for mass memory storage. The directory is used for all subsequent MMEM commands if no path
		is specified with them. \n
			:param directory: directory_name String containing the path to another directory. The path can be relative or absolute. To change to a higher directory, use two dots '..' .
		"""
		param = Conversions.value_to_quoted_str(directory)
		self._core.io.write(f'MMEMory:CDIRectory {param}')

	def copy(self, source_file: str, destination_file: str) -> None:
		"""SCPI: MMEMory:COPY \n
		Snippet: driver.massMemory.copy(source_file = '1', destination_file = '1') \n
		Copies an existing file to a new file. Instead of just a file, this command can also be used to copy a complete directory
		together with all its files. \n
			:param source_file: string String containing the path and file name of the source file
			:param destination_file: string String containing the path and name of the target file. The path can be relative or absolute. If DestinationFile is not specified, the SourceFile is copied to the current directory, queried with the method RsSmw.MassMemory.currentDirectory command. Note: Existing files with the same name in the destination directory are overwritten without an error message.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('source_file', source_file, DataType.String), ArgSingle('destination_file', destination_file, DataType.String))
		self._core.io.write(f'MMEMory:COPY {param}'.rstrip())

	def delete(self, filename: str) -> None:
		"""SCPI: MMEMory:DELete \n
		Snippet: driver.massMemory.delete(filename = '1') \n
		Removes a file from the specified directory. \n
			:param filename: string String parameter to specify the name and directory of the file to be removed.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'MMEMory:DELete {param}')

	def get_drives(self) -> str:
		"""SCPI: MMEMory:DRIVes \n
		Snippet: value: str = driver.massMemory.get_drives() \n
		No command help available \n
			:return: drive_list: No help available
		"""
		response = self._core.io.query_str('MMEMory:DRIVes?')
		return trim_str_response(response)

	def make_directory(self, directory: str) -> None:
		"""SCPI: MMEMory:MDIRectory \n
		Snippet: driver.massMemory.make_directory(directory = '1') \n
		Creates a subdirectory for mass memory storage in the specified directory. If no directory is specified, a subdirectory
		is created in the default directory. This command can also be used to create a directory tree. \n
			:param directory: string String parameter to specify the new directory.
		"""
		param = Conversions.value_to_quoted_str(directory)
		self._core.io.write(f'MMEMory:MDIRectory {param}')

	def move(self, source_file: str, destination_file: str) -> None:
		"""SCPI: MMEMory:MOVE \n
		Snippet: driver.massMemory.move(source_file = '1', destination_file = '1') \n
		Moves an existing file to a new location or, if no path is specified, renames an existing file. \n
			:param source_file: string String parameter to specify the name of the file to be moved.
			:param destination_file: string String parameters to specify the name of the new file.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('source_file', source_file, DataType.String), ArgSingle('destination_file', destination_file, DataType.String))
		self._core.io.write(f'MMEMory:MOVE {param}'.rstrip())

	def get_msis(self) -> str:
		"""SCPI: MMEMory:MSIS \n
		Snippet: value: str = driver.massMemory.get_msis() \n
		Defines the drive or network resource (in the case of networks) for instruments with windows operating system, using msis
		(MSIS = Mass Storage Identification String) . Note: Instruments with Linux operating system ignore this command, since
		Linux does not use drive letter assignment. \n
			:return: path: No help available
		"""
		response = self._core.io.query_str('MMEMory:MSIS?')
		return trim_str_response(response)

	def set_msis(self, path: str) -> None:
		"""SCPI: MMEMory:MSIS \n
		Snippet: driver.massMemory.set_msis(path = '1') \n
		Defines the drive or network resource (in the case of networks) for instruments with windows operating system, using msis
		(MSIS = Mass Storage Identification String) . Note: Instruments with Linux operating system ignore this command, since
		Linux does not use drive letter assignment. \n
			:param path: No help available
		"""
		param = Conversions.value_to_quoted_str(path)
		self._core.io.write(f'MMEMory:MSIS {param}')

	def delete_directory(self, directory: str) -> None:
		"""SCPI: MMEMory:RDIRectory \n
		Snippet: driver.massMemory.delete_directory(directory = '1') \n
		Removes an existing directory from the mass memory storage system. If no directory is specified, the subdirectory with
		the specified name is deleted in the default directory. \n
			:param directory: string String parameter to specify the directory to be deleted.
		"""
		param = Conversions.value_to_quoted_str(directory)
		self._core.io.write(f'MMEMory:RDIRectory {param}')

	def clone(self) -> 'MassMemory':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MassMemory(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
