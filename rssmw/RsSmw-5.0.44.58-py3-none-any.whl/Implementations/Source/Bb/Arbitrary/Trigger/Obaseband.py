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
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TRIGger:OBASeband:DELay \n
		Snippet: value: float = driver.source.bb.arbitrary.trigger.obaseband.get_delay() \n
		Delays the trigger event compared to the trigger event in the other basebands. \n
			:return: delay: float Range: 0 to 2147483647
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:TRIGger:OBASeband:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TRIGger:OBASeband:DELay \n
		Snippet: driver.source.bb.arbitrary.trigger.obaseband.set_delay(delay = 1.0) \n
		Delays the trigger event compared to the trigger event in the other basebands. \n
			:param delay: float Range: 0 to 2147483647
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:TRIGger:OBASeband:DELay {param}')

	def get_inhibit(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TRIGger:OBASeband:INHibit \n
		Snippet: value: int = driver.source.bb.arbitrary.trigger.obaseband.get_inhibit() \n
		For triggering via the other path, specifies the number of samples by which a restart is inhibited. \n
			:return: inhibit: integer Range: 0 to 67108863, Unit: sample
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:TRIGger:OBASeband:INHibit?')
		return Conversions.str_to_int(response)

	def set_inhibit(self, inhibit: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TRIGger:OBASeband:INHibit \n
		Snippet: driver.source.bb.arbitrary.trigger.obaseband.set_inhibit(inhibit = 1) \n
		For triggering via the other path, specifies the number of samples by which a restart is inhibited. \n
			:param inhibit: integer Range: 0 to 67108863, Unit: sample
		"""
		param = Conversions.decimal_value_to_str(inhibit)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:TRIGger:OBASeband:INHibit {param}')

	def get_rdelay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TRIGger:OBASeband:RDELay \n
		Snippet: value: float = driver.source.bb.arbitrary.trigger.obaseband.get_rdelay() \n
		Queries the time a trigger event form the other path is delayed. \n
			:return: res_time_delay_sec: float Range: 0 to 688, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:TRIGger:OBASeband:RDELay?')
		return Conversions.str_to_float(response)

	def get_tdelay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TRIGger:OBASeband:TDELay \n
		Snippet: value: float = driver.source.bb.arbitrary.trigger.obaseband.get_tdelay() \n
		Specifies the trigger delay for triggering by the signal from the other path. Maximum trigger delay and trigger inhibit
		values depend on the installed options. See 'Specifying delay and inhibit values'. \n
			:return: obas_time_delay: float Range: 0 to depends on the symbol rate, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:TRIGger:OBASeband:TDELay?')
		return Conversions.str_to_float(response)

	def set_tdelay(self, obas_time_delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TRIGger:OBASeband:TDELay \n
		Snippet: driver.source.bb.arbitrary.trigger.obaseband.set_tdelay(obas_time_delay = 1.0) \n
		Specifies the trigger delay for triggering by the signal from the other path. Maximum trigger delay and trigger inhibit
		values depend on the installed options. See 'Specifying delay and inhibit values'. \n
			:param obas_time_delay: float Range: 0 to depends on the symbol rate, Unit: s
		"""
		param = Conversions.decimal_value_to_str(obas_time_delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:TRIGger:OBASeband:TDELay {param}')
