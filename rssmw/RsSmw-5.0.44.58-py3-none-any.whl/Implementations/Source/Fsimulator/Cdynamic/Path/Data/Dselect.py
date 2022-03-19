from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dselect:
	"""Dselect commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dselect", core, parent)

	def set(self, filename: str, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:CDYNamic:PATH<CH>:DATA:DSELect \n
		Snippet: driver.source.fsimulator.cdynamic.path.data.dselect.set(filename = '1', path = repcap.Path.Default) \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.fad_udyn. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:param filename: 'filename' Filename or absolute file path; file extension can be omitted.
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
		"""
		param = Conversions.value_to_quoted_str(filename)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:CDYNamic:PATH{path_cmd_val}:DATA:DSELect {param}')

	def get(self, path=repcap.Path.Default) -> str:
		"""SCPI: [SOURce<HW>]:FSIMulator:CDYNamic:PATH<CH>:DATA:DSELect \n
		Snippet: value: str = driver.source.fsimulator.cdynamic.path.data.dselect.get(path = repcap.Path.Default) \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.fad_udyn. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
			:return: filename: 'filename' Filename or absolute file path; file extension can be omitted."""
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:CDYNamic:PATH{path_cmd_val}:DATA:DSELect?')
		return trim_str_response(response)
