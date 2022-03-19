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
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:TDW:STATe \n
		Snippet: value: bool = driver.source.bb.oneweb.tdw.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:TDW:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:TDW:STATe \n
		Snippet: driver.source.bb.oneweb.tdw.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:TDW:STATe {param}')

	def get_tr_time(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:TDW:TRTime \n
		Snippet: value: float = driver.source.bb.oneweb.tdw.get_tr_time() \n
		No command help available \n
			:return: transition_time: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:TDW:TRTime?')
		return Conversions.str_to_float(response)

	def set_tr_time(self, transition_time: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:TDW:TRTime \n
		Snippet: driver.source.bb.oneweb.tdw.set_tr_time(transition_time = 1.0) \n
		No command help available \n
			:param transition_time: No help available
		"""
		param = Conversions.decimal_value_to_str(transition_time)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:TDW:TRTime {param}')
