from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Obaseband:
	"""Obaseband commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("obaseband", core, parent)

	def get_delay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:TERRestrial:TRIGger:OBASeband:DELay \n
		Snippet: value: float = driver.source.bb.xmRadio.terrestrial.trigger.obaseband.get_delay() \n
		No command help available \n
			:return: delay: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:XMRadio:TERRestrial:TRIGger:OBASeband:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:TERRestrial:TRIGger:OBASeband:DELay \n
		Snippet: driver.source.bb.xmRadio.terrestrial.trigger.obaseband.set_delay(delay = 1.0) \n
		No command help available \n
			:param delay: No help available
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:XMRadio:TERRestrial:TRIGger:OBASeband:DELay {param}')

	def get_inhibit(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:TERRestrial:TRIGger:OBASeband:INHibit \n
		Snippet: value: int = driver.source.bb.xmRadio.terrestrial.trigger.obaseband.get_inhibit() \n
		No command help available \n
			:return: inhibit: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:XMRadio:TERRestrial:TRIGger:OBASeband:INHibit?')
		return Conversions.str_to_int(response)

	def set_inhibit(self, inhibit: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:TERRestrial:TRIGger:OBASeband:INHibit \n
		Snippet: driver.source.bb.xmRadio.terrestrial.trigger.obaseband.set_inhibit(inhibit = 1) \n
		No command help available \n
			:param inhibit: No help available
		"""
		param = Conversions.decimal_value_to_str(inhibit)
		self._core.io.write(f'SOURce<HwInstance>:BB:XMRadio:TERRestrial:TRIGger:OBASeband:INHibit {param}')
