from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Overrange:
	"""Overrange commands group definition. 4 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("overrange", core, parent)

	@property
	def allowed(self):
		"""allowed commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_allowed'):
			from .Allowed import Allowed
			self._allowed = Allowed(self._core, self._cmd_group)
		return self._allowed

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:FREQuency:CONVerter:EXTernal:OVERrange:[STATe] \n
		Snippet: value: bool = driver.source.frequency.converter.external.overrange.get_state() \n
		Enables the extended frequency range of a connected R&S SZU. \n
			:return: overrang_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:CONVerter:EXTernal:OVERrange:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, overrang_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:FREQuency:CONVerter:EXTernal:OVERrange:[STATe] \n
		Snippet: driver.source.frequency.converter.external.overrange.set_state(overrang_state = False) \n
		Enables the extended frequency range of a connected R&S SZU. \n
			:param overrang_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(overrang_state)
		self._core.io.write(f'SOURce<HwInstance>:FREQuency:CONVerter:EXTernal:OVERrange:STATe {param}')

	def clone(self) -> 'Overrange':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Overrange(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
