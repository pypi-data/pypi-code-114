from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class External:
	"""External commands group definition. 5 total commands, 1 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("external", core, parent)

	@property
	def synchronize(self):
		"""synchronize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_synchronize'):
			from .Synchronize import Synchronize
			self._synchronize = Synchronize(self._core, self._cmd_group)
		return self._synchronize

	def get_rdelay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:TRIGger:EXTernal:RDELay \n
		Snippet: value: float = driver.source.bb.oneweb.trigger.external.get_rdelay() \n
		Queries the time (in seconds) an external trigger event is delayed for. \n
			:return: trig_ext_time_res_d: float Range: 0 to 688
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:TRIGger:EXTernal:RDELay?')
		return Conversions.str_to_float(response)

	def get_tdelay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:TRIGger:EXTernal:TDELay \n
		Snippet: value: float = driver.source.bb.oneweb.trigger.external.get_tdelay() \n
		Specifies the trigger delay for external triggering. The value affects all external trigger signals. \n
			:return: trig_ext_time_del: float Range: 0 to 688
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:TRIGger:EXTernal:TDELay?')
		return Conversions.str_to_float(response)

	def set_tdelay(self, trig_ext_time_del: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:TRIGger:EXTernal:TDELay \n
		Snippet: driver.source.bb.oneweb.trigger.external.set_tdelay(trig_ext_time_del = 1.0) \n
		Specifies the trigger delay for external triggering. The value affects all external trigger signals. \n
			:param trig_ext_time_del: float Range: 0 to 688
		"""
		param = Conversions.decimal_value_to_str(trig_ext_time_del)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:TRIGger:EXTernal:TDELay {param}')

	def get_delay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:TRIGger:[EXTernal]:DELay \n
		Snippet: value: float = driver.source.bb.oneweb.trigger.external.get_delay() \n
		Sets the trigger delay. \n
			:return: trig_ext_delay: float Range: 0 to 68719476735
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:TRIGger:EXTernal:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, trig_ext_delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:TRIGger:[EXTernal]:DELay \n
		Snippet: driver.source.bb.oneweb.trigger.external.set_delay(trig_ext_delay = 1.0) \n
		Sets the trigger delay. \n
			:param trig_ext_delay: float Range: 0 to 68719476735
		"""
		param = Conversions.decimal_value_to_str(trig_ext_delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:TRIGger:EXTernal:DELay {param}')

	def get_inhibit(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:TRIGger:[EXTernal]:INHibit \n
		Snippet: value: int = driver.source.bb.oneweb.trigger.external.get_inhibit() \n
		Specifies the duration by which a restart is inhibited. \n
			:return: trig_ext_inhibit: integer Range: 0 to 67108863
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:TRIGger:EXTernal:INHibit?')
		return Conversions.str_to_int(response)

	def set_inhibit(self, trig_ext_inhibit: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:TRIGger:[EXTernal]:INHibit \n
		Snippet: driver.source.bb.oneweb.trigger.external.set_inhibit(trig_ext_inhibit = 1) \n
		Specifies the duration by which a restart is inhibited. \n
			:param trig_ext_inhibit: integer Range: 0 to 67108863
		"""
		param = Conversions.decimal_value_to_str(trig_ext_inhibit)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:TRIGger:EXTernal:INHibit {param}')

	def clone(self) -> 'External':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = External(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
