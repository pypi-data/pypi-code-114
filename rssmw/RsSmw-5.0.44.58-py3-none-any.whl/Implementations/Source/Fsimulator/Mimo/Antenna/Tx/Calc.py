from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Calc:
	"""Calc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("calc", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.AntModCalcMode:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:ANTenna:TX:CALC:MODE \n
		Snippet: value: enums.AntModCalcMode = driver.source.fsimulator.mimo.antenna.tx.calc.get_mode() \n
		Set how the distance between the antenna elements is defined: based on the physical distance or on the relative phase. \n
			:return: ant_mod_calc_rx_mod: SPACing| RELativphase SPACing To set the distance, use the corresponding command, for example [:SOURcehw]:FSIMulator:MIMO:ANTenna:TX:ESPacing:HORizontal. RELativphase Load an antenna pattern file that contains the relative phase description. See 'Antenna pattern file format'
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:MIMO:ANTenna:TX:CALC:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AntModCalcMode)

	def set_mode(self, ant_mod_calc_rx_mod: enums.AntModCalcMode) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:ANTenna:TX:CALC:MODE \n
		Snippet: driver.source.fsimulator.mimo.antenna.tx.calc.set_mode(ant_mod_calc_rx_mod = enums.AntModCalcMode.RELativphase) \n
		Set how the distance between the antenna elements is defined: based on the physical distance or on the relative phase. \n
			:param ant_mod_calc_rx_mod: SPACing| RELativphase SPACing To set the distance, use the corresponding command, for example [:SOURcehw]:FSIMulator:MIMO:ANTenna:TX:ESPacing:HORizontal. RELativphase Load an antenna pattern file that contains the relative phase description. See 'Antenna pattern file format'
		"""
		param = Conversions.enum_scalar_to_str(ant_mod_calc_rx_mod, enums.AntModCalcMode)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:ANTenna:TX:CALC:MODE {param}')
