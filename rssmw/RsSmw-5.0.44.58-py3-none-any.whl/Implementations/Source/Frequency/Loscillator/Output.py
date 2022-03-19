from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Output:
	"""Output commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("output", core, parent)

	def get_frequency(self) -> float:
		"""SCPI: [SOURce<HW>]:FREQuency:LOSCillator:OUTPut:FREQuency \n
		Snippet: value: float = driver.source.frequency.loscillator.output.get_frequency() \n
		Queries the current frequency of the local oscillator at the [LO OUT] connector. \n
			:return: frequency: float Range: 100E3 to 20E9
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:LOSCillator:OUTPut:FREQuency?')
		return Conversions.str_to_float(response)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:FREQuency:LOSCillator:OUTPut:STATe \n
		Snippet: value: bool = driver.source.frequency.loscillator.output.get_state() \n
		Activates the LO output in the second path. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:LOSCillator:OUTPut:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:FREQuency:LOSCillator:OUTPut:STATe \n
		Snippet: driver.source.frequency.loscillator.output.set_state(state = False) \n
		Activates the LO output in the second path. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:FREQuency:LOSCillator:OUTPut:STATe {param}')
