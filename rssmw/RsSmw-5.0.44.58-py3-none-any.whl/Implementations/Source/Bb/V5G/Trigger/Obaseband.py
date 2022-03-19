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
		"""SCPI: [SOURce<HW>]:BB:V5G:TRIGger:OBASeband:DELay \n
		Snippet: value: float = driver.source.bb.v5G.trigger.obaseband.get_delay() \n
		Sets the trigger delay for triggering by the trigger signal from the other path. \n
			:return: oth_delay: float Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:TRIGger:OBASeband:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, oth_delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:TRIGger:OBASeband:DELay \n
		Snippet: driver.source.bb.v5G.trigger.obaseband.set_delay(oth_delay = 1.0) \n
		Sets the trigger delay for triggering by the trigger signal from the other path. \n
			:param oth_delay: float Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(oth_delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:TRIGger:OBASeband:DELay {param}')

	def get_inhibit(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:TRIGger:OBASeband:INHibit \n
		Snippet: value: int = driver.source.bb.v5G.trigger.obaseband.get_inhibit() \n
		For triggering via the other path, specifies the duration by which a restart is inhibited. \n
			:return: oth_inhibit: integer Range: 0 to 67108863
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:TRIGger:OBASeband:INHibit?')
		return Conversions.str_to_int(response)

	def set_inhibit(self, oth_inhibit: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:TRIGger:OBASeband:INHibit \n
		Snippet: driver.source.bb.v5G.trigger.obaseband.set_inhibit(oth_inhibit = 1) \n
		For triggering via the other path, specifies the duration by which a restart is inhibited. \n
			:param oth_inhibit: integer Range: 0 to 67108863
		"""
		param = Conversions.decimal_value_to_str(oth_inhibit)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:TRIGger:OBASeband:INHibit {param}')

	def get_rdelay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:TRIGger:OBASeband:RDELay \n
		Snippet: value: float = driver.source.bb.v5G.trigger.obaseband.get_rdelay() \n
		Queries the time a trigger event form the other path is delayed. \n
			:return: oth_time_res_delay: float Range: 0 to 688
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:TRIGger:OBASeband:RDELay?')
		return Conversions.str_to_float(response)

	def get_tdelay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:TRIGger:OBASeband:TDELay \n
		Snippet: value: float = driver.source.bb.v5G.trigger.obaseband.get_tdelay() \n
		Specifies the trigger delay for triggering by the signal from the other path. \n
			:return: oth_time_delay: float Range: 0 to 688
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:TRIGger:OBASeband:TDELay?')
		return Conversions.str_to_float(response)

	def set_tdelay(self, oth_time_delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:TRIGger:OBASeband:TDELay \n
		Snippet: driver.source.bb.v5G.trigger.obaseband.set_tdelay(oth_time_delay = 1.0) \n
		Specifies the trigger delay for triggering by the signal from the other path. \n
			:param oth_time_delay: float Range: 0 to 688
		"""
		param = Conversions.decimal_value_to_str(oth_time_delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:TRIGger:OBASeband:TDELay {param}')
