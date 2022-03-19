from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Obaseband:
	"""Obaseband commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("obaseband", core, parent)

	def get_delay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:NFC:TRIGger:OBASeband:DELay \n
		Snippet: value: float = driver.source.bb.nfc.trigger.obaseband.get_delay() \n
		Specifies the trigger delay (expressed as a number of samples) for triggering by the trigger signal from the second path. \n
			:return: delay: float Range: 0 to 2147483647
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:TRIGger:OBASeband:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:TRIGger:OBASeband:DELay \n
		Snippet: driver.source.bb.nfc.trigger.obaseband.set_delay(delay = 1.0) \n
		Specifies the trigger delay (expressed as a number of samples) for triggering by the trigger signal from the second path. \n
			:param delay: float Range: 0 to 2147483647
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:TRIGger:OBASeband:DELay {param}')

	def get_inhibit(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NFC:TRIGger:OBASeband:INHibit \n
		Snippet: value: int = driver.source.bb.nfc.trigger.obaseband.get_inhibit() \n
		Available for two-path instruments only. Internal other baseband trigger inhibit. Sets the trigger signal inhibit in
		samples on internal triggering via the second path. \n
			:return: inhibit: integer Range: 0 to 67108863
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:TRIGger:OBASeband:INHibit?')
		return Conversions.str_to_int(response)

	def set_inhibit(self, inhibit: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:TRIGger:OBASeband:INHibit \n
		Snippet: driver.source.bb.nfc.trigger.obaseband.set_inhibit(inhibit = 1) \n
		Available for two-path instruments only. Internal other baseband trigger inhibit. Sets the trigger signal inhibit in
		samples on internal triggering via the second path. \n
			:param inhibit: integer Range: 0 to 67108863
		"""
		param = Conversions.decimal_value_to_str(inhibit)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:TRIGger:OBASeband:INHibit {param}')
