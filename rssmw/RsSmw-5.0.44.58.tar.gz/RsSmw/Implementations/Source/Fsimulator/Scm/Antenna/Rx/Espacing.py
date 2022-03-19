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
		"""SCPI: [SOURce]:FSIMulator:SCM:ANTenna:RX:ESPacing:HORizontal \n
		Snippet: value: float = driver.source.fsimulator.scm.antenna.rx.espacing.get_horizontal() \n
		Sets the distance between the antennas in the antenna array. \n
			:return: spacing_horizontal: No help available
		"""
		response = self._core.io.query_str('SOURce:FSIMulator:SCM:ANTenna:RX:ESPacing:HORizontal?')
		return Conversions.str_to_float(response)

	def set_horizontal(self, spacing_horizontal: float) -> None:
		"""SCPI: [SOURce]:FSIMulator:SCM:ANTenna:RX:ESPacing:HORizontal \n
		Snippet: driver.source.fsimulator.scm.antenna.rx.espacing.set_horizontal(spacing_horizontal = 1.0) \n
		Sets the distance between the antennas in the antenna array. \n
			:param spacing_horizontal: float Range: 0 to 10
		"""
		param = Conversions.decimal_value_to_str(spacing_horizontal)
		self._core.io.write(f'SOURce:FSIMulator:SCM:ANTenna:RX:ESPacing:HORizontal {param}')

	def get_vertical(self) -> float:
		"""SCPI: [SOURce]:FSIMulator:SCM:ANTenna:RX:ESPacing:VERTical \n
		Snippet: value: float = driver.source.fsimulator.scm.antenna.rx.espacing.get_vertical() \n
		Sets the distance between the antennas in the antenna array. \n
			:return: anten_rx_spac_vert: No help available
		"""
		response = self._core.io.query_str('SOURce:FSIMulator:SCM:ANTenna:RX:ESPacing:VERTical?')
		return Conversions.str_to_float(response)

	def set_vertical(self, anten_rx_spac_vert: float) -> None:
		"""SCPI: [SOURce]:FSIMulator:SCM:ANTenna:RX:ESPacing:VERTical \n
		Snippet: driver.source.fsimulator.scm.antenna.rx.espacing.set_vertical(anten_rx_spac_vert = 1.0) \n
		Sets the distance between the antennas in the antenna array. \n
			:param anten_rx_spac_vert: float Range: 0 to 10
		"""
		param = Conversions.decimal_value_to_str(anten_rx_spac_vert)
		self._core.io.write(f'SOURce:FSIMulator:SCM:ANTenna:RX:ESPacing:VERTical {param}')
