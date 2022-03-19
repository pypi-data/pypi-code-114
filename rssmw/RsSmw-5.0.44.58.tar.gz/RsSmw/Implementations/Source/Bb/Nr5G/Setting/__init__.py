from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Setting:
	"""Setting commands group definition. 16 total commands, 2 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("setting", core, parent)

	@property
	def exchange(self):
		"""exchange commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_exchange'):
			from .Exchange import Exchange
			self._exchange = Exchange(self._core, self._cmd_group)
		return self._exchange

	@property
	def tmodel(self):
		"""tmodel commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_tmodel'):
			from .Tmodel import Tmodel
			self._tmodel = Tmodel(self._core, self._cmd_group)
		return self._tmodel

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SETTing:CATalog \n
		Snippet: value: List[str] = driver.source.bb.nr5G.setting.get_catalog() \n
		Queries the files with settings in the default directory. Listed are files with the file extension *.nr5g.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:return: nr_5_gcat_name: filename1,filename2,... Returns a string of filenames separated by commas.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:SETTing:CATalog?')
		return Conversions.str_to_str_list(response)

	def get_del_py(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SETTing:DEL \n
		Snippet: value: str = driver.source.bb.nr5G.setting.get_del_py() \n
		Deletes the selected file from the default or the specified directory. Deleted are files with extension *.nr5g. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:return: filename: 'filename' Filename or complete file path; file extension can be omitted
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:SETTing:DEL?')
		return trim_str_response(response)

	def set_del_py(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SETTing:DEL \n
		Snippet: driver.source.bb.nr5G.setting.set_del_py(filename = '1') \n
		Deletes the selected file from the default or the specified directory. Deleted are files with extension *.nr5g. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:param filename: 'filename' Filename or complete file path; file extension can be omitted
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:SETTing:DEL {param}')

	def get_load(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SETTing:LOAD \n
		Snippet: value: str = driver.source.bb.nr5G.setting.get_load() \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.nr5g. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:return: filename: 'filename' Filename or complete file path; file extension can be omitted
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:SETTing:LOAD?')
		return trim_str_response(response)

	def set_load(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SETTing:LOAD \n
		Snippet: driver.source.bb.nr5G.setting.set_load(filename = '1') \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.nr5g. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:param filename: 'filename' Filename or complete file path; file extension can be omitted
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:SETTing:LOAD {param}')

	def get_store(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SETTing:STORe \n
		Snippet: value: str = driver.source.bb.nr5G.setting.get_store() \n
		Saves the current settings into the selected file; the file extension (*.nr5g) is assigned automatically.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:return: filename: 'filename' Filename or complete file path
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:SETTing:STORe?')
		return trim_str_response(response)

	def set_store(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SETTing:STORe \n
		Snippet: driver.source.bb.nr5G.setting.set_store(filename = '1') \n
		Saves the current settings into the selected file; the file extension (*.nr5g) is assigned automatically.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:param filename: 'filename' Filename or complete file path
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:SETTing:STORe {param}')

	def clone(self) -> 'Setting':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Setting(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
