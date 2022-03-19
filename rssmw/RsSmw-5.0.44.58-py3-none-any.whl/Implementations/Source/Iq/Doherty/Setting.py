from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Setting:
	"""Setting commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("setting", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce]:IQ:DOHerty:SETTing:CATalog \n
		Snippet: value: List[str] = driver.source.iq.doherty.setting.get_catalog() \n
		Queries the files with digital Doherty setting in the default directory. Listed are files with the file extension *.
		di_doher. Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in
		the default and in a specific directory. \n
			:return: catalog: string A comma-separated list of filenames; the file extenssion is omitted
		"""
		response = self._core.io.query_str('SOURce:IQ:DOHerty:SETTing:CATalog?')
		return Conversions.str_to_str_list(response)

	def delete(self, filename: str) -> None:
		"""SCPI: [SOURce]:IQ:DOHerty:SETTing:DELete \n
		Snippet: driver.source.iq.doherty.setting.delete(filename = '1') \n
		Deletes the selected file from the default or specified directory. Deleted are files with the file extension *.di_doher.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:param filename: 'filename' Filename or complete file path
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce:IQ:DOHerty:SETTing:DELete {param}')

	def load(self, filename: str) -> None:
		"""SCPI: [SOURce]:IQ:DOHerty:SETTing:LOAD \n
		Snippet: driver.source.iq.doherty.setting.load(filename = '1') \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.di_doher. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:param filename: 'filename' Filename or complete file path
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce:IQ:DOHerty:SETTing:LOAD {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce]:IQ:DOHerty:SETTing:PRESet \n
		Snippet: driver.source.iq.doherty.setting.preset() \n
		Sets the default settings (*RST values specified for the commands) . Not affected is the state set with the command
		[:SOURce]:IQ:DOHerty:STATe. \n
		"""
		self._core.io.write(f'SOURce:IQ:DOHerty:SETTing:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce]:IQ:DOHerty:SETTing:PRESet \n
		Snippet: driver.source.iq.doherty.setting.preset_with_opc() \n
		Sets the default settings (*RST values specified for the commands) . Not affected is the state set with the command
		[:SOURce]:IQ:DOHerty:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce:IQ:DOHerty:SETTing:PRESet', opc_timeout_ms)

	def set_store(self, filename: str) -> None:
		"""SCPI: [SOURce]:IQ:DOHerty:SETTing:STORe \n
		Snippet: driver.source.iq.doherty.setting.set_store(filename = '1') \n
		Stores the current settings into the selected file; the file extension (*.di_doher) is assigned automatically. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:param filename: 'filename' Filename or complete file path
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce:IQ:DOHerty:SETTing:STORe {param}')
