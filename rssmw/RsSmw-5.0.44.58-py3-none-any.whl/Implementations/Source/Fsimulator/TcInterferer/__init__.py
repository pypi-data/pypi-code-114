from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TcInterferer:
	"""TcInterferer commands group definition. 21 total commands, 2 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tcInterferer", core, parent)

	@property
	def moving(self):
		"""moving commands group. 2 Sub-classes, 5 commands."""
		if not hasattr(self, '_moving'):
			from .Moving import Moving
			self._moving = Moving(self._core, self._cmd_group)
		return self._moving

	@property
	def reference(self):
		"""reference commands group. 2 Sub-classes, 5 commands."""
		if not hasattr(self, '_reference'):
			from .Reference import Reference
			self._reference = Reference(self._core, self._cmd_group)
		return self._reference

	def get_period(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:TCINterferer:PERiod \n
		Snippet: value: float = driver.source.fsimulator.tcInterferer.get_period() \n
		Sets either the dwell time or the period for a complete cycle of the moving path. \n
			:return: period: float Range: 0.1 to 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:TCINterferer:PERiod?')
		return Conversions.str_to_float(response)

	def set_period(self, period: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:TCINterferer:PERiod \n
		Snippet: driver.source.fsimulator.tcInterferer.set_period(period = 1.0) \n
		Sets either the dwell time or the period for a complete cycle of the moving path. \n
			:param period: float Range: 0.1 to 10
		"""
		param = Conversions.decimal_value_to_str(period)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:TCINterferer:PERiod {param}')

	def get_speed(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:TCINterferer:SPEed \n
		Snippet: value: float = driver.source.fsimulator.tcInterferer.get_speed() \n
		Sets the speed v of the moving receiver for 2 channel interferer fading. \n
			:return: speed: float Range: 0 to 27778 (dynamic)
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:TCINterferer:SPEed?')
		return Conversions.str_to_float(response)

	def set_speed(self, speed: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:TCINterferer:SPEed \n
		Snippet: driver.source.fsimulator.tcInterferer.set_speed(speed = 1.0) \n
		Sets the speed v of the moving receiver for 2 channel interferer fading. \n
			:param speed: float Range: 0 to 27778 (dynamic)
		"""
		param = Conversions.decimal_value_to_str(speed)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:TCINterferer:SPEed {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:TCINterferer:[STATe] \n
		Snippet: value: bool = driver.source.fsimulator.tcInterferer.get_state() \n
		Activates the 2 channel interferer fading configuration. The paths and the fading simulator must be switched on
		separately, see [:SOURce<hw>]:FSIMulator:TCINterferer:REFerence|MOVing:STATe and [:SOURce<hw>]:FSIMulator[:STATe]. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:TCINterferer:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:TCINterferer:[STATe] \n
		Snippet: driver.source.fsimulator.tcInterferer.set_state(state = False) \n
		Activates the 2 channel interferer fading configuration. The paths and the fading simulator must be switched on
		separately, see [:SOURce<hw>]:FSIMulator:TCINterferer:REFerence|MOVing:STATe and [:SOURce<hw>]:FSIMulator[:STATe]. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:TCINterferer:STATe {param}')

	def clone(self) -> 'TcInterferer':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TcInterferer(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
