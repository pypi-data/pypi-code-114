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
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:TRIGger:OBASeband:DELay \n
		Snippet: value: float = driver.source.bb.esequencer.trigger.obaseband.get_delay() \n
		Determines the delay of the trigger event to the trigger signal of another trigger source, e.g. the internal baseband
		trigger signal of the other path (BB:ESEQ:TRIG:SOUR INTA or INTB) , or an external . \n
			:return: delay: float Range: 0 to 2147483647
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ESEQuencer:TRIGger:OBASeband:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:TRIGger:OBASeband:DELay \n
		Snippet: driver.source.bb.esequencer.trigger.obaseband.set_delay(delay = 1.0) \n
		Determines the delay of the trigger event to the trigger signal of another trigger source, e.g. the internal baseband
		trigger signal of the other path (BB:ESEQ:TRIG:SOUR INTA or INTB) , or an external . \n
			:param delay: float Range: 0 to 2147483647
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:TRIGger:OBASeband:DELay {param}')

	def get_inhibit(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:TRIGger:OBASeband:INHibit \n
		Snippet: value: int = driver.source.bb.esequencer.trigger.obaseband.get_inhibit() \n
		For triggering via the other path, specifies the number of samples by which a restart is to be inhibited following a
		trigger event. \n
			:return: inhibit: integer Range: 0 to 67108863
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ESEQuencer:TRIGger:OBASeband:INHibit?')
		return Conversions.str_to_int(response)

	def set_inhibit(self, inhibit: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:TRIGger:OBASeband:INHibit \n
		Snippet: driver.source.bb.esequencer.trigger.obaseband.set_inhibit(inhibit = 1) \n
		For triggering via the other path, specifies the number of samples by which a restart is to be inhibited following a
		trigger event. \n
			:param inhibit: integer Range: 0 to 67108863
		"""
		param = Conversions.decimal_value_to_str(inhibit)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:TRIGger:OBASeband:INHibit {param}')

	def get_rdelay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:TRIGger:OBASeband:RDELay \n
		Snippet: value: float = driver.source.bb.esequencer.trigger.obaseband.get_rdelay() \n
		Queries the time a trigger event from the other path is delayed. \n
			:return: other_res_time_delay: float Range: 0 to 688
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ESEQuencer:TRIGger:OBASeband:RDELay?')
		return Conversions.str_to_float(response)

	def get_tdelay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:TRIGger:OBASeband:TDELay \n
		Snippet: value: float = driver.source.bb.esequencer.trigger.obaseband.get_tdelay() \n
		Specifies the trigger delay for triggering by the signal from the other path. \n
			:return: other_time_delay: float Range: 0 to 688, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ESEQuencer:TRIGger:OBASeband:TDELay?')
		return Conversions.str_to_float(response)

	def set_tdelay(self, other_time_delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:TRIGger:OBASeband:TDELay \n
		Snippet: driver.source.bb.esequencer.trigger.obaseband.set_tdelay(other_time_delay = 1.0) \n
		Specifies the trigger delay for triggering by the signal from the other path. \n
			:param other_time_delay: float Range: 0 to 688, Unit: s
		"""
		param = Conversions.decimal_value_to_str(other_time_delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:TRIGger:OBASeband:TDELay {param}')
