from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Obaseband:
	"""Obaseband commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("obaseband", core, parent)

	def get_delay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OBASeband:DELay \n
		Snippet: value: float = driver.source.bb.nr5G.trigger.obaseband.get_delay() \n
		Sets the trigger delay for triggering by the trigger signal from the other path. \n
			:return: trig_int_oth_delay: float Range: 0 to 2147483647
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TRIGger:OBASeband:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, trig_int_oth_delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OBASeband:DELay \n
		Snippet: driver.source.bb.nr5G.trigger.obaseband.set_delay(trig_int_oth_delay = 1.0) \n
		Sets the trigger delay for triggering by the trigger signal from the other path. \n
			:param trig_int_oth_delay: float Range: 0 to 2147483647
		"""
		param = Conversions.decimal_value_to_str(trig_int_oth_delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OBASeband:DELay {param}')

	def get_inhibit(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OBASeband:INHibit \n
		Snippet: value: int = driver.source.bb.nr5G.trigger.obaseband.get_inhibit() \n
		For triggering via the other path, specifies the duration by which a restart is inhibited. \n
			:return: int_oth_inhibit: integer Range: 0 to 67108863
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TRIGger:OBASeband:INHibit?')
		return Conversions.str_to_int(response)

	def set_inhibit(self, int_oth_inhibit: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OBASeband:INHibit \n
		Snippet: driver.source.bb.nr5G.trigger.obaseband.set_inhibit(int_oth_inhibit = 1) \n
		For triggering via the other path, specifies the duration by which a restart is inhibited. \n
			:param int_oth_inhibit: integer Range: 0 to 67108863
		"""
		param = Conversions.decimal_value_to_str(int_oth_inhibit)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OBASeband:INHibit {param}')

	def get_rdelay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OBASeband:RDELay \n
		Snippet: value: float = driver.source.bb.nr5G.trigger.obaseband.get_rdelay() \n
		Queries the time a trigger event form the other path is delayed. \n
			:return: int_oth_rdelay_sec: float Range: 0 to 688
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TRIGger:OBASeband:RDELay?')
		return Conversions.str_to_float(response)

	def get_tdelay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OBASeband:TDELay \n
		Snippet: value: float = driver.source.bb.nr5G.trigger.obaseband.get_tdelay() \n
		Specifies the trigger delay for triggering by the signal from the other path. \n
			:return: int_oth_delay_sec: float Range: 0 to 688, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TRIGger:OBASeband:TDELay?')
		return Conversions.str_to_float(response)

	def set_tdelay(self, int_oth_delay_sec: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OBASeband:TDELay \n
		Snippet: driver.source.bb.nr5G.trigger.obaseband.set_tdelay(int_oth_delay_sec = 1.0) \n
		Specifies the trigger delay for triggering by the signal from the other path. \n
			:param int_oth_delay_sec: float Range: 0 to 688, Unit: s
		"""
		param = Conversions.decimal_value_to_str(int_oth_delay_sec)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OBASeband:TDELay {param}')
