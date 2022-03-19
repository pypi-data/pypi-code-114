from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Polarization:
	"""Polarization commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("polarization", core, parent)

	@property
	def pratio(self):
		"""pratio commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_pratio'):
			from .Pratio import Pratio
			self._pratio = Pratio(self._core, self._cmd_group)
		return self._pratio

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:POLarization:STATe \n
		Snippet: value: bool = driver.source.fsimulator.scm.polarization.get_state() \n
		Enables/disables simulation of channel polarization. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SCM:POLarization:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:POLarization:STATe \n
		Snippet: driver.source.fsimulator.scm.polarization.set_state(state = False) \n
		Enables/disables simulation of channel polarization. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:POLarization:STATe {param}')

	def clone(self) -> 'Polarization':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Polarization(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
