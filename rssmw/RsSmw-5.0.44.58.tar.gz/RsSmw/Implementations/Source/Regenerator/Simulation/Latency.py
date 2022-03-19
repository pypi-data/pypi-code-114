from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Latency:
	"""Latency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("latency", core, parent)

	def get_bz(self) -> float:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:LATency:[BZ] \n
		Snippet: value: float = driver.source.regenerator.simulation.latency.get_bz() \n
		Sets the system latency value manually. \n
			:return: blind_zone: float Range: 0 to 3000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:SIMulation:LATency:BZ?')
		return Conversions.str_to_float(response)

	def set_bz(self, blind_zone: float) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:LATency:[BZ] \n
		Snippet: driver.source.regenerator.simulation.latency.set_bz(blind_zone = 1.0) \n
		Sets the system latency value manually. \n
			:param blind_zone: float Range: 0 to 3000
		"""
		param = Conversions.decimal_value_to_str(blind_zone)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:SIMulation:LATency:BZ {param}')
