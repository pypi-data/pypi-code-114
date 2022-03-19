from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Flength:
	"""Flength commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("flength", core, parent)

	def get_landing(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:FLENgth:LANDing \n
		Snippet: value: float = driver.source.fsimulator.dsSimulation.towerToAir.flength.get_landing() \n
		No command help available \n
			:return: flen_landing: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:FLENgth:LANDing?')
		return Conversions.str_to_float(response)

	def set_landing(self, flen_landing: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:FLENgth:LANDing \n
		Snippet: driver.source.fsimulator.dsSimulation.towerToAir.flength.set_landing(flen_landing = 1.0) \n
		No command help available \n
			:param flen_landing: No help available
		"""
		param = Conversions.decimal_value_to_str(flen_landing)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:FLENgth:LANDing {param}')

	def get_takeoff(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:FLENgth:TAKeoff \n
		Snippet: value: float = driver.source.fsimulator.dsSimulation.towerToAir.flength.get_takeoff() \n
		No command help available \n
			:return: flen_takeoff: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:FLENgth:TAKeoff?')
		return Conversions.str_to_float(response)

	def set_takeoff(self, flen_takeoff: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:FLENgth:TAKeoff \n
		Snippet: driver.source.fsimulator.dsSimulation.towerToAir.flength.set_takeoff(flen_takeoff = 1.0) \n
		No command help available \n
			:param flen_takeoff: No help available
		"""
		param = Conversions.decimal_value_to_str(flen_takeoff)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:FLENgth:TAKeoff {param}')
