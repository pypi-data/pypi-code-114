from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def get_breakpoint(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:POWer:BREakpoint \n
		Snippet: value: float = driver.source.iq.doherty.shaping.power.get_breakpoint() \n
		Sets the power value required for the calculation of the correction function if classic Doherty shaping is used. \n
			:return: split: float Range: -50 to 0
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DOHerty:SHAPing:POWer:BREakpoint?')
		return Conversions.str_to_float(response)

	def set_breakpoint(self, split: float) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:POWer:BREakpoint \n
		Snippet: driver.source.iq.doherty.shaping.power.set_breakpoint(split = 1.0) \n
		Sets the power value required for the calculation of the correction function if classic Doherty shaping is used. \n
			:param split: float Range: -50 to 0
		"""
		param = Conversions.decimal_value_to_str(split)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DOHerty:SHAPing:POWer:BREakpoint {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:POWer:STATe \n
		Snippet: value: bool = driver.source.iq.doherty.shaping.power.get_state() \n
		Enables/disables the power and phase corrections. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DOHerty:SHAPing:POWer:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:POWer:STATe \n
		Snippet: driver.source.iq.doherty.shaping.power.set_state(state = False) \n
		Enables/disables the power and phase corrections. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DOHerty:SHAPing:POWer:STATe {param}')
