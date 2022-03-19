from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rate:
	"""Rate commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rate", core, parent)

	def get_climb(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:RATE:CLIMb \n
		Snippet: value: float = driver.source.fsimulator.dsSimulation.towerToAir.rate.get_climb() \n
		No command help available \n
			:return: rate_climb: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:RATE:CLIMb?')
		return Conversions.str_to_float(response)

	def set_climb(self, rate_climb: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:RATE:CLIMb \n
		Snippet: driver.source.fsimulator.dsSimulation.towerToAir.rate.set_climb(rate_climb = 1.0) \n
		No command help available \n
			:param rate_climb: No help available
		"""
		param = Conversions.decimal_value_to_str(rate_climb)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:RATE:CLIMb {param}')

	def get_descent(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:RATE:DESCent \n
		Snippet: value: float = driver.source.fsimulator.dsSimulation.towerToAir.rate.get_descent() \n
		No command help available \n
			:return: rate_descent: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:RATE:DESCent?')
		return Conversions.str_to_float(response)

	def set_descent(self, rate_descent: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:RATE:DESCent \n
		Snippet: driver.source.fsimulator.dsSimulation.towerToAir.rate.set_descent(rate_descent = 1.0) \n
		No command help available \n
			:param rate_descent: No help available
		"""
		param = Conversions.decimal_value_to_str(rate_descent)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:RATE:DESCent {param}')
