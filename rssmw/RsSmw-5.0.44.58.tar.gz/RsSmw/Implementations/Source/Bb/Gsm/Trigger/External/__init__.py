from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class External:
	"""External commands group definition. 5 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("external", core, parent)

	@property
	def clock(self):
		"""clock commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_clock'):
			from .Clock import Clock
			self._clock = Clock(self._core, self._cmd_group)
		return self._clock

	@property
	def synchronize(self):
		"""synchronize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_synchronize'):
			from .Synchronize import Synchronize
			self._synchronize = Synchronize(self._core, self._cmd_group)
		return self._synchronize

	def get_delay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GSM:TRIGger:[EXTernal]:DELay \n
		Snippet: value: float = driver.source.bb.gsm.trigger.external.get_delay() \n
		Sets the trigger delay. \n
			:return: delay: float Range: 0 to 2147483647, Unit: samples
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:TRIGger:EXTernal:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:TRIGger:[EXTernal]:DELay \n
		Snippet: driver.source.bb.gsm.trigger.external.set_delay(delay = 1.0) \n
		Sets the trigger delay. \n
			:param delay: float Range: 0 to 2147483647, Unit: samples
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:TRIGger:EXTernal:DELay {param}')

	def get_inhibit(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GSM:TRIGger:[EXTernal]:INHibit \n
		Snippet: value: int = driver.source.bb.gsm.trigger.external.get_inhibit() \n
		Specifies the duration by which a restart is inhibited. \n
			:return: inhibit: integer Range: 0 to 21.47*symbRate
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:TRIGger:EXTernal:INHibit?')
		return Conversions.str_to_int(response)

	def set_inhibit(self, inhibit: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:TRIGger:[EXTernal]:INHibit \n
		Snippet: driver.source.bb.gsm.trigger.external.set_inhibit(inhibit = 1) \n
		Specifies the duration by which a restart is inhibited. \n
			:param inhibit: integer Range: 0 to 21.47*symbRate
		"""
		param = Conversions.decimal_value_to_str(inhibit)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:TRIGger:EXTernal:INHibit {param}')

	def clone(self) -> 'External':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = External(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
