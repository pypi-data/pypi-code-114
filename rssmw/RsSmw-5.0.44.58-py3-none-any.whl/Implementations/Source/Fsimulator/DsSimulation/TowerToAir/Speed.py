from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Speed:
	"""Speed commands group definition. 6 total commands, 0 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("speed", core, parent)

	def get_cruise(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:SPEed:CRUise \n
		Snippet: value: float = driver.source.fsimulator.dsSimulation.towerToAir.speed.get_cruise() \n
		No command help available \n
			:return: speed_cruise: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:SPEed:CRUise?')
		return Conversions.str_to_float(response)

	def set_cruise(self, speed_cruise: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:SPEed:CRUise \n
		Snippet: driver.source.fsimulator.dsSimulation.towerToAir.speed.set_cruise(speed_cruise = 1.0) \n
		No command help available \n
			:param speed_cruise: No help available
		"""
		param = Conversions.decimal_value_to_str(speed_cruise)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:SPEed:CRUise {param}')

	def get_departure(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:SPEed:DEParture \n
		Snippet: value: float = driver.source.fsimulator.dsSimulation.towerToAir.speed.get_departure() \n
		No command help available \n
			:return: speed_departure: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:SPEed:DEParture?')
		return Conversions.str_to_float(response)

	def set_departure(self, speed_departure: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:SPEed:DEParture \n
		Snippet: driver.source.fsimulator.dsSimulation.towerToAir.speed.set_departure(speed_departure = 1.0) \n
		No command help available \n
			:param speed_departure: No help available
		"""
		param = Conversions.decimal_value_to_str(speed_departure)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:SPEed:DEParture {param}')

	def get_descent(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:SPEed:DESCent \n
		Snippet: value: float = driver.source.fsimulator.dsSimulation.towerToAir.speed.get_descent() \n
		No command help available \n
			:return: speed_descent: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:SPEed:DESCent?')
		return Conversions.str_to_float(response)

	def set_descent(self, speed_descent: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:SPEed:DESCent \n
		Snippet: driver.source.fsimulator.dsSimulation.towerToAir.speed.set_descent(speed_descent = 1.0) \n
		No command help available \n
			:param speed_descent: No help available
		"""
		param = Conversions.decimal_value_to_str(speed_descent)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:SPEed:DESCent {param}')

	def get_start(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:SPEed:STARt \n
		Snippet: value: float = driver.source.fsimulator.dsSimulation.towerToAir.speed.get_start() \n
		No command help available \n
			:return: speed_start: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:SPEed:STARt?')
		return Conversions.str_to_float(response)

	def set_start(self, speed_start: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:SPEed:STARt \n
		Snippet: driver.source.fsimulator.dsSimulation.towerToAir.speed.set_start(speed_start = 1.0) \n
		No command help available \n
			:param speed_start: No help available
		"""
		param = Conversions.decimal_value_to_str(speed_start)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:SPEed:STARt {param}')

	def get_takeoff(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:SPEed:TAKeoff \n
		Snippet: value: float = driver.source.fsimulator.dsSimulation.towerToAir.speed.get_takeoff() \n
		No command help available \n
			:return: speed_takeoff: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:SPEed:TAKeoff?')
		return Conversions.str_to_float(response)

	def set_takeoff(self, speed_takeoff: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:SPEed:TAKeoff \n
		Snippet: driver.source.fsimulator.dsSimulation.towerToAir.speed.set_takeoff(speed_takeoff = 1.0) \n
		No command help available \n
			:param speed_takeoff: No help available
		"""
		param = Conversions.decimal_value_to_str(speed_takeoff)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:SPEed:TAKeoff {param}')

	def get_touchdown(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:SPEed:TOUChdown \n
		Snippet: value: float = driver.source.fsimulator.dsSimulation.towerToAir.speed.get_touchdown() \n
		No command help available \n
			:return: speed_touchdown: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:SPEed:TOUChdown?')
		return Conversions.str_to_float(response)

	def set_touchdown(self, speed_touchdown: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:SPEed:TOUChdown \n
		Snippet: driver.source.fsimulator.dsSimulation.towerToAir.speed.set_touchdown(speed_touchdown = 1.0) \n
		No command help available \n
			:param speed_touchdown: No help available
		"""
		param = Conversions.decimal_value_to_str(speed_touchdown)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:SPEed:TOUChdown {param}')
