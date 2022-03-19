from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class File:
	"""File commands group definition. 4 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("file", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:EFRontend:ALIGnment:FILE:CATalog \n
		Snippet: value: List[str] = driver.source.efrontend.alignment.file.get_catalog() \n
		Queries the cable correction files with settings in the default directory. Listed are cable correction files with
		extension *.s2p. Refer to 'Accessing Files in the Default or Specified Directory' for general information on file
		handling in the default and in a specific directory. \n
			:return: freq_conv_fe_cable_corr_cat: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:EFRontend:ALIGnment:FILE:CATalog?')
		return Conversions.str_to_str_list(response)

	def get_select(self) -> str:
		"""SCPI: [SOURce<HW>]:EFRontend:ALIGnment:FILE:[SELect] \n
		Snippet: value: str = driver.source.efrontend.alignment.file.get_select() \n
		Selects an existing correction file to compensate for cable losses. Selectable file have file extension *.s2p. \n
			:return: cable_corr_file_na: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:EFRontend:ALIGnment:FILE:SELect?')
		return trim_str_response(response)

	def set_select(self, cable_corr_file_na: str) -> None:
		"""SCPI: [SOURce<HW>]:EFRontend:ALIGnment:FILE:[SELect] \n
		Snippet: driver.source.efrontend.alignment.file.set_select(cable_corr_file_na = '1') \n
		Selects an existing correction file to compensate for cable losses. Selectable file have file extension *.s2p. \n
			:param cable_corr_file_na: string
		"""
		param = Conversions.value_to_quoted_str(cable_corr_file_na)
		self._core.io.write(f'SOURce<HwInstance>:EFRontend:ALIGnment:FILE:SELect {param}')

	def clone(self) -> 'File':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = File(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
