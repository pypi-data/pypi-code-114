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
		"""SCPI: [SOURce<HW>]:BB:EVDO:TRIGger:OBASeband:DELay \n
		Snippet: value: float = driver.source.bb.evdo.trigger.obaseband.get_delay() \n
		Specifies the trigger delay for triggering by the trigger signal from the other baseband. \n
			:return: delay: float Range: 0 to 2147483647
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EVDO:TRIGger:OBASeband:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TRIGger:OBASeband:DELay \n
		Snippet: driver.source.bb.evdo.trigger.obaseband.set_delay(delay = 1.0) \n
		Specifies the trigger delay for triggering by the trigger signal from the other baseband. \n
			:param delay: float Range: 0 to 2147483647
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:TRIGger:OBASeband:DELay {param}')

	def get_inhibit(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TRIGger:OBASeband:INHibit \n
		Snippet: value: int = driver.source.bb.evdo.trigger.obaseband.get_inhibit() \n
		For triggering via the other path, specifies the duration by which a restart is inhibited. \n
			:return: inhibit: integer Range: 0 to 67108863
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EVDO:TRIGger:OBASeband:INHibit?')
		return Conversions.str_to_int(response)

	def set_inhibit(self, inhibit: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TRIGger:OBASeband:INHibit \n
		Snippet: driver.source.bb.evdo.trigger.obaseband.set_inhibit(inhibit = 1) \n
		For triggering via the other path, specifies the duration by which a restart is inhibited. \n
			:param inhibit: integer Range: 0 to 67108863
		"""
		param = Conversions.decimal_value_to_str(inhibit)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:TRIGger:OBASeband:INHibit {param}')
