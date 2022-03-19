from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pratio:
	"""Pratio commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pratio", core, parent)

	def get_horizontal(self) -> float:
		"""SCPI: [SOURce]:FSIMulator:MIMO:ANTenna:POLarization:PRATio:HORizontal \n
		Snippet: value: float = driver.source.fsimulator.mimo.antenna.polarization.pratio.get_horizontal() \n
		Sets the cross polarization power ratio (XPR) in dB. \n
			:return: ant_pol_pow_rat_hor: No help available
		"""
		response = self._core.io.query_str('SOURce:FSIMulator:MIMO:ANTenna:POLarization:PRATio:HORizontal?')
		return Conversions.str_to_float(response)

	def set_horizontal(self, ant_pol_pow_rat_hor: float) -> None:
		"""SCPI: [SOURce]:FSIMulator:MIMO:ANTenna:POLarization:PRATio:HORizontal \n
		Snippet: driver.source.fsimulator.mimo.antenna.polarization.pratio.set_horizontal(ant_pol_pow_rat_hor = 1.0) \n
		Sets the cross polarization power ratio (XPR) in dB. \n
			:param ant_pol_pow_rat_hor: float Range: 0 to 20
		"""
		param = Conversions.decimal_value_to_str(ant_pol_pow_rat_hor)
		self._core.io.write(f'SOURce:FSIMulator:MIMO:ANTenna:POLarization:PRATio:HORizontal {param}')

	def get_vertical(self) -> float:
		"""SCPI: [SOURce]:FSIMulator:MIMO:ANTenna:POLarization:PRATio:VERTical \n
		Snippet: value: float = driver.source.fsimulator.mimo.antenna.polarization.pratio.get_vertical() \n
		Sets the cross polarization power ratio (XPR) in dB. \n
			:return: ant_pol_pow_rat_ver: float Range: 0 to 20
		"""
		response = self._core.io.query_str('SOURce:FSIMulator:MIMO:ANTenna:POLarization:PRATio:VERTical?')
		return Conversions.str_to_float(response)

	def set_vertical(self, ant_pol_pow_rat_ver: float) -> None:
		"""SCPI: [SOURce]:FSIMulator:MIMO:ANTenna:POLarization:PRATio:VERTical \n
		Snippet: driver.source.fsimulator.mimo.antenna.polarization.pratio.set_vertical(ant_pol_pow_rat_ver = 1.0) \n
		Sets the cross polarization power ratio (XPR) in dB. \n
			:param ant_pol_pow_rat_ver: float Range: 0 to 20
		"""
		param = Conversions.decimal_value_to_str(ant_pol_pow_rat_ver)
		self._core.io.write(f'SOURce:FSIMulator:MIMO:ANTenna:POLarization:PRATio:VERTical {param}')
