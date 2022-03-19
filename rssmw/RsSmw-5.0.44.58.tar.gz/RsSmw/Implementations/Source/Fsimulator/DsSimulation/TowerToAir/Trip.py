from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trip:
	"""Trip commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trip", core, parent)

	def get_duration(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:TRIP:DURation \n
		Snippet: value: float = driver.source.fsimulator.dsSimulation.towerToAir.trip.get_duration() \n
		No command help available \n
			:return: trip_duration: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:TRIP:DURation?')
		return Conversions.str_to_float(response)

	def get_length(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:TRIP:LENGth \n
		Snippet: value: float = driver.source.fsimulator.dsSimulation.towerToAir.trip.get_length() \n
		No command help available \n
			:return: trip_length: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:TRIP:LENGth?')
		return Conversions.str_to_float(response)
