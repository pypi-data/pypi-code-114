from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Radius:
	"""Radius commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("radius", core, parent)

	def get_lturn(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:RADius:LTURn \n
		Snippet: value: float = driver.source.fsimulator.dsSimulation.towerToAir.radius.get_lturn() \n
		No command help available \n
			:return: radius_left_turn: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:RADius:LTURn?')
		return Conversions.str_to_float(response)

	def set_lturn(self, radius_left_turn: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:RADius:LTURn \n
		Snippet: driver.source.fsimulator.dsSimulation.towerToAir.radius.set_lturn(radius_left_turn = 1.0) \n
		No command help available \n
			:param radius_left_turn: No help available
		"""
		param = Conversions.decimal_value_to_str(radius_left_turn)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:RADius:LTURn {param}')

	def get_rturn(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:RADius:RTURn \n
		Snippet: value: float = driver.source.fsimulator.dsSimulation.towerToAir.radius.get_rturn() \n
		No command help available \n
			:return: radius_right_turn: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:RADius:RTURn?')
		return Conversions.str_to_float(response)

	def set_rturn(self, radius_right_turn: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:RADius:RTURn \n
		Snippet: driver.source.fsimulator.dsSimulation.towerToAir.radius.set_rturn(radius_right_turn = 1.0) \n
		No command help available \n
			:param radius_right_turn: No help available
		"""
		param = Conversions.decimal_value_to_str(radius_right_turn)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:RADius:RTURn {param}')
