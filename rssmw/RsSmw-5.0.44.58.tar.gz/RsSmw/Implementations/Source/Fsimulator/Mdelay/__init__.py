from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mdelay:
	"""Mdelay commands group definition. 23 total commands, 5 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mdelay", core, parent)

	@property
	def all(self):
		"""all commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	@property
	def channel(self):
		"""channel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_channel'):
			from .Channel import Channel
			self._channel = Channel(self._core, self._cmd_group)
		return self._channel

	@property
	def del30(self):
		"""del30 commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_del30'):
			from .Del30 import Del30
			self._del30 = Del30(self._core, self._cmd_group)
		return self._del30

	@property
	def moving(self):
		"""moving commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_moving'):
			from .Moving import Moving
			self._moving = Moving(self._core, self._cmd_group)
		return self._moving

	@property
	def reference(self):
		"""reference commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_reference'):
			from .Reference import Reference
			self._reference = Reference(self._core, self._cmd_group)
		return self._reference

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:MDELay:STATe \n
		Snippet: value: bool = driver.source.fsimulator.mdelay.get_state() \n
		This command activates the moving propagation fading configuration. The paths and the fading simulator must be switched
		on separately (SOURce:FSIMulator:MDELay:MOVing|REFerence:STATe ON and SOURce:FSIMulator ON) . \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:MDELay:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MDELay:STATe \n
		Snippet: driver.source.fsimulator.mdelay.set_state(state = False) \n
		This command activates the moving propagation fading configuration. The paths and the fading simulator must be switched
		on separately (SOURce:FSIMulator:MDELay:MOVing|REFerence:STATe ON and SOURce:FSIMulator ON) . \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MDELay:STATe {param}')

	def clone(self) -> 'Mdelay':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mdelay(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
