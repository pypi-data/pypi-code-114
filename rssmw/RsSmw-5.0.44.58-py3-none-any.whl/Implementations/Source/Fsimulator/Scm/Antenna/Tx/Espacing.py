from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Espacing:
	"""Espacing commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("espacing", core, parent)

	def get_horizontal(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:ANTenna:TX:ESPacing:HORizontal \n
		Snippet: value: float = driver.source.fsimulator.scm.antenna.tx.espacing.get_horizontal() \n
		Sets the distance between the antennas in the antenna array. \n
			:return: horizontal: float Range: 0 to 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SCM:ANTenna:TX:ESPacing:HORizontal?')
		return Conversions.str_to_float(response)

	def set_horizontal(self, horizontal: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:ANTenna:TX:ESPacing:HORizontal \n
		Snippet: driver.source.fsimulator.scm.antenna.tx.espacing.set_horizontal(horizontal = 1.0) \n
		Sets the distance between the antennas in the antenna array. \n
			:param horizontal: float Range: 0 to 10
		"""
		param = Conversions.decimal_value_to_str(horizontal)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:ANTenna:TX:ESPacing:HORizontal {param}')

	def get_vertical(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:ANTenna:TX:ESPacing:VERTical \n
		Snippet: value: float = driver.source.fsimulator.scm.antenna.tx.espacing.get_vertical() \n
		Sets the distance between the antennas in the antenna array. \n
			:return: ant_tx_spac_vertical: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SCM:ANTenna:TX:ESPacing:VERTical?')
		return Conversions.str_to_float(response)

	def set_vertical(self, ant_tx_spac_vertical: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:ANTenna:TX:ESPacing:VERTical \n
		Snippet: driver.source.fsimulator.scm.antenna.tx.espacing.set_vertical(ant_tx_spac_vertical = 1.0) \n
		Sets the distance between the antennas in the antenna array. \n
			:param ant_tx_spac_vertical: float Range: 0 to 10
		"""
		param = Conversions.decimal_value_to_str(ant_tx_spac_vertical)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:ANTenna:TX:ESPacing:VERTical {param}')
