from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Glonass:
	"""Glonass commands group definition. 6 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("glonass", core, parent)

	@property
	def signal(self):
		"""signal commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_signal'):
			from .Signal import Signal
			self._signal = Signal(self._core, self._cmd_group)
		return self._signal

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SYSTem:GLONass:[STATe] \n
		Snippet: value: bool = driver.source.bb.gnss.system.glonass.get_state() \n
		Defines if satellites from the selected GNSS system are included in the simulated satellites constellation. \n
			:return: state: 1| ON| 0| OFF Disabling a GNSS system deactivates all SVID and signals from this system.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:SYSTem:GLONass:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SYSTem:GLONass:[STATe] \n
		Snippet: driver.source.bb.gnss.system.glonass.set_state(state = False) \n
		Defines if satellites from the selected GNSS system are included in the simulated satellites constellation. \n
			:param state: 1| ON| 0| OFF Disabling a GNSS system deactivates all SVID and signals from this system.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SYSTem:GLONass:STATe {param}')

	def clone(self) -> 'Glonass':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Glonass(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
