from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tdw:
	"""Tdw commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tdw", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TDW:STATe \n
		Snippet: value: bool = driver.source.bb.eutra.tdw.get_state() \n
		Activates/deactivates the time domain windowing. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TDW:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TDW:STATe \n
		Snippet: driver.source.bb.eutra.tdw.set_state(state = False) \n
		Activates/deactivates the time domain windowing. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TDW:STATe {param}')

	def get_tr_time(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TDW:TRTime \n
		Snippet: value: float = driver.source.bb.eutra.tdw.get_tr_time() \n
		Sets the transition time when time domain windowing is active. \n
			:return: transition_time: float Range: 0 to 1E-5, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TDW:TRTime?')
		return Conversions.str_to_float(response)

	def set_tr_time(self, transition_time: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TDW:TRTime \n
		Snippet: driver.source.bb.eutra.tdw.set_tr_time(transition_time = 1.0) \n
		Sets the transition time when time domain windowing is active. \n
			:param transition_time: float Range: 0 to 1E-5, Unit: s
		"""
		param = Conversions.decimal_value_to_str(transition_time)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TDW:TRTime {param}')
