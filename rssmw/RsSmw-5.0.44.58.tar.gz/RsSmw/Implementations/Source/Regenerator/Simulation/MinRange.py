from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MinRange:
	"""MinRange commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minRange", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:MINRange:[STATe] \n
		Snippet: value: bool = driver.source.regenerator.simulation.minRange.get_state() \n
		Enables the simulation of delays that are shorter than the system latency (τ < tBZ) . \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:SIMulation:MINRange:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:MINRange:[STATe] \n
		Snippet: driver.source.regenerator.simulation.minRange.set_state(state = False) \n
		Enables the simulation of delays that are shorter than the system latency (τ < tBZ) . \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:SIMulation:MINRange:STATe {param}')
