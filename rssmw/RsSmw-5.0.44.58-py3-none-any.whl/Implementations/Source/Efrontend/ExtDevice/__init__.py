from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExtDevice:
	"""ExtDevice commands group definition. 4 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("extDevice", core, parent)

	@property
	def correction(self):
		"""correction commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_correction'):
			from .Correction import Correction
			self._correction = Correction(self._core, self._cmd_group)
		return self._correction

	@property
	def refresh(self):
		"""refresh commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_refresh'):
			from .Refresh import Refresh
			self._refresh = Refresh(self._core, self._cmd_group)
		return self._refresh

	def get_list_py(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:EFRontend:EXTDevice:LIST \n
		Snippet: value: List[str] = driver.source.efrontend.extDevice.get_list_py() \n
		No command help available \n
			:return: id_pi_db_freq_conv_fes_pi_dev_list: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:EFRontend:EXTDevice:LIST?')
		return Conversions.str_to_str_list(response)

	def clone(self) -> 'ExtDevice':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ExtDevice(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
