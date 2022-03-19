from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Altitude:
	"""Altitude commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("altitude", core, parent)

	def get_cruise(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:ALTitude:CRUise \n
		Snippet: value: float = driver.source.fsimulator.dsSimulation.towerToAir.altitude.get_cruise() \n
		No command help available \n
			:return: altitude_cruise: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:ALTitude:CRUise?')
		return Conversions.str_to_float(response)

	def set_cruise(self, altitude_cruise: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:ALTitude:CRUise \n
		Snippet: driver.source.fsimulator.dsSimulation.towerToAir.altitude.set_cruise(altitude_cruise = 1.0) \n
		No command help available \n
			:param altitude_cruise: No help available
		"""
		param = Conversions.decimal_value_to_str(altitude_cruise)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:ALTitude:CRUise {param}')
