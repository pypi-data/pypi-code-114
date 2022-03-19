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
		"""SCPI: [SOURce<HW>]:BB:WLAD:TRIGger:OBASeband:DELay \n
		Snippet: value: float = driver.source.bb.wlad.trigger.obaseband.get_delay() \n
		Stops signal generation for trigger modes Armed_Auto and Armed_Retrigger. A subsequent internal or external trigger event
		restart signal generation. \n
			:return: delay: float Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:TRIGger:OBASeband:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:TRIGger:OBASeband:DELay \n
		Snippet: driver.source.bb.wlad.trigger.obaseband.set_delay(delay = 1.0) \n
		Stops signal generation for trigger modes Armed_Auto and Armed_Retrigger. A subsequent internal or external trigger event
		restart signal generation. \n
			:param delay: float Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:TRIGger:OBASeband:DELay {param}')

	def get_inhibit(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:WLAD:TRIGger:OBASeband:INHibit \n
		Snippet: value: int = driver.source.bb.wlad.trigger.obaseband.get_inhibit() \n
		Specifies the number of samples by which a restart is to be inhibited following a trigger event. This command applies
		only for triggering by the second path. \n
			:return: inhibit: integer Range: 0 to 67108863
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:TRIGger:OBASeband:INHibit?')
		return Conversions.str_to_int(response)

	def set_inhibit(self, inhibit: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:TRIGger:OBASeband:INHibit \n
		Snippet: driver.source.bb.wlad.trigger.obaseband.set_inhibit(inhibit = 1) \n
		Specifies the number of samples by which a restart is to be inhibited following a trigger event. This command applies
		only for triggering by the second path. \n
			:param inhibit: integer Range: 0 to 67108863
		"""
		param = Conversions.decimal_value_to_str(inhibit)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:TRIGger:OBASeband:INHibit {param}')
