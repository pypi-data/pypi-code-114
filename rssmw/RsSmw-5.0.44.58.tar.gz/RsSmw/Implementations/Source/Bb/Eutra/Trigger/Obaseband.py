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
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TRIGger:OBASeband:DELay \n
		Snippet: value: float = driver.source.bb.eutra.trigger.obaseband.get_delay() \n
		When triggering via the other basebands, delays the trigger event compared to the one in the other baseband. \n
			:return: delay: float Range: 0 to 2147483647
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TRIGger:OBASeband:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TRIGger:OBASeband:DELay \n
		Snippet: driver.source.bb.eutra.trigger.obaseband.set_delay(delay = 1.0) \n
		When triggering via the other basebands, delays the trigger event compared to the one in the other baseband. \n
			:param delay: float Range: 0 to 2147483647
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TRIGger:OBASeband:DELay {param}')

	def get_inhibit(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TRIGger:OBASeband:INHibit \n
		Snippet: value: int = driver.source.bb.eutra.trigger.obaseband.get_inhibit() \n
		For triggering via the other path, specifies the number of samples by which a restart is inhibited. \n
			:return: inhibit: integer Range: 0 to 67108863
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TRIGger:OBASeband:INHibit?')
		return Conversions.str_to_int(response)

	def set_inhibit(self, inhibit: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TRIGger:OBASeband:INHibit \n
		Snippet: driver.source.bb.eutra.trigger.obaseband.set_inhibit(inhibit = 1) \n
		For triggering via the other path, specifies the number of samples by which a restart is inhibited. \n
			:param inhibit: integer Range: 0 to 67108863
		"""
		param = Conversions.decimal_value_to_str(inhibit)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TRIGger:OBASeband:INHibit {param}')

	def get_rdelay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TRIGger:OBASeband:RDELay \n
		Snippet: value: float = driver.source.bb.eutra.trigger.obaseband.get_rdelay() \n
		Queries the actual trigger delay (expressed in time units) of the trigger signal from the second path. \n
			:return: int_oth_rdelay: float Range: 0 to 688
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TRIGger:OBASeband:RDELay?')
		return Conversions.str_to_float(response)

	def get_tdelay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TRIGger:OBASeband:TDELay \n
		Snippet: value: float = driver.source.bb.eutra.trigger.obaseband.get_tdelay() \n
		Specifies the trigger delay (expressed in time units) for triggering by the trigger signal from the other path. \n
			:return: int_oth_tdelay: float Range: 0 to depends on other values, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TRIGger:OBASeband:TDELay?')
		return Conversions.str_to_float(response)

	def set_tdelay(self, int_oth_tdelay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TRIGger:OBASeband:TDELay \n
		Snippet: driver.source.bb.eutra.trigger.obaseband.set_tdelay(int_oth_tdelay = 1.0) \n
		Specifies the trigger delay (expressed in time units) for triggering by the trigger signal from the other path. \n
			:param int_oth_tdelay: float Range: 0 to depends on other values, Unit: s
		"""
		param = Conversions.decimal_value_to_str(int_oth_tdelay)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TRIGger:OBASeband:TDELay {param}')
