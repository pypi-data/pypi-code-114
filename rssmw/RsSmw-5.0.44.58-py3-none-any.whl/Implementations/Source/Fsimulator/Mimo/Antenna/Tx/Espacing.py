from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Espacing:
	"""Espacing commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("espacing", core, parent)

	def get_cross(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:ANTenna:TX:ESPacing:CROSs \n
		Snippet: value: float = driver.source.fsimulator.mimo.antenna.tx.espacing.get_cross() \n
		Sets the polarized distance between the antennas in the antenna array. \n
			:return: cross: float Range: 0 to 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:MIMO:ANTenna:TX:ESPacing:CROSs?')
		return Conversions.str_to_float(response)

	def set_cross(self, cross: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:ANTenna:TX:ESPacing:CROSs \n
		Snippet: driver.source.fsimulator.mimo.antenna.tx.espacing.set_cross(cross = 1.0) \n
		Sets the polarized distance between the antennas in the antenna array. \n
			:param cross: float Range: 0 to 10
		"""
		param = Conversions.decimal_value_to_str(cross)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:ANTenna:TX:ESPacing:CROSs {param}')

	def get_horizontal(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:ANTenna:TX:ESPacing:HORizontal \n
		Snippet: value: float = driver.source.fsimulator.mimo.antenna.tx.espacing.get_horizontal() \n
		Sets the polarized distance between the antennas in the antenna array. \n
			:return: ant_tx_espac_horizontal: float Range: 0 to 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:MIMO:ANTenna:TX:ESPacing:HORizontal?')
		return Conversions.str_to_float(response)

	def set_horizontal(self, ant_tx_espac_horizontal: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:ANTenna:TX:ESPacing:HORizontal \n
		Snippet: driver.source.fsimulator.mimo.antenna.tx.espacing.set_horizontal(ant_tx_espac_horizontal = 1.0) \n
		Sets the polarized distance between the antennas in the antenna array. \n
			:param ant_tx_espac_horizontal: float Range: 0 to 10
		"""
		param = Conversions.decimal_value_to_str(ant_tx_espac_horizontal)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:ANTenna:TX:ESPacing:HORizontal {param}')

	def get_vertical(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:ANTenna:TX:ESPacing:VERTical \n
		Snippet: value: float = driver.source.fsimulator.mimo.antenna.tx.espacing.get_vertical() \n
		No command help available \n
			:return: ant_tx_espac_vertical: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:MIMO:ANTenna:TX:ESPacing:VERTical?')
		return Conversions.str_to_float(response)

	def set_vertical(self, ant_tx_espac_vertical: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:ANTenna:TX:ESPacing:VERTical \n
		Snippet: driver.source.fsimulator.mimo.antenna.tx.espacing.set_vertical(ant_tx_espac_vertical = 1.0) \n
		No command help available \n
			:param ant_tx_espac_vertical: No help available
		"""
		param = Conversions.decimal_value_to_str(ant_tx_espac_vertical)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:ANTenna:TX:ESPacing:VERTical {param}')
