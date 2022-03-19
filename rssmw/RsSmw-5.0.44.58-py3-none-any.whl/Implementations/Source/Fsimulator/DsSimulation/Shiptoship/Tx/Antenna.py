from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Antenna:
	"""Antenna commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("antenna", core, parent)

	def get_height(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:SHIPtoship:TX:ANTenna:HEIGht \n
		Snippet: value: float = driver.source.fsimulator.dsSimulation.shiptoship.tx.antenna.get_height() \n
		No command help available \n
			:return: ant_height: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:SHIPtoship:TX:ANTenna:HEIGht?')
		return Conversions.str_to_float(response)

	def set_height(self, ant_height: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:SHIPtoship:TX:ANTenna:HEIGht \n
		Snippet: driver.source.fsimulator.dsSimulation.shiptoship.tx.antenna.set_height(ant_height = 1.0) \n
		No command help available \n
			:param ant_height: No help available
		"""
		param = Conversions.decimal_value_to_str(ant_height)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:SHIPtoship:TX:ANTenna:HEIGht {param}')
