from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fader:
	"""Fader commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fader", core, parent)

	@property
	def hardware(self):
		"""hardware commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hardware'):
			from .Hardware import Hardware
			self._hardware = Hardware(self._core, self._cmd_group)
		return self._hardware

	def get_value(self) -> bool:
		"""SCPI: TEST:FADer \n
		Snippet: value: bool = driver.test.fader.get_value() \n
		No command help available \n
			:return: fader: No help available
		"""
		response = self._core.io.query_str('TEST:FADer?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Fader':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fader(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
