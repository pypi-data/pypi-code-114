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
	def get_mode(self) -> enums.AntModCalcGeoMode:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:ANTenna:TX:CALC:MODE \n
		Snippet: value: enums.AntModCalcGeoMode = driver.source.fsimulator.scm.antenna.tx.calc.get_mode() \n
		Set how the phase information is calculated \n
			:return: mode: SPACing| RELativphase| BFORming SPACing The phase information is calculated from the spacing between the antenna elements. To set the distance, use the corresponding command, for example [:SOURcehw]:FSIMulator:SCM:ANTenna:TX:ESPacing:HORizontal. RELativphase Load an antenna pattern file that contains the relative phase description. See 'Antenna pattern file format' BFORming Composite antenna pattern of an antenna array comprising gain and phase is used to simulate analog beamforming. To set the distance, use the corresponding command, for example [:SOURcehw]:FSIMulator:SCM:ANTenna:TX:ESPacing:HORizontal.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SCM:ANTenna:TX:CALC:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AntModCalcGeoMode)

	def set_mode(self, mode: enums.AntModCalcGeoMode) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:ANTenna:TX:CALC:MODE \n
		Snippet: driver.source.fsimulator.scm.antenna.tx.calc.set_mode(mode = enums.AntModCalcGeoMode.BFORming) \n
		Set how the phase information is calculated \n
			:param mode: SPACing| RELativphase| BFORming SPACing The phase information is calculated from the spacing between the antenna elements. To set the distance, use the corresponding command, for example [:SOURcehw]:FSIMulator:SCM:ANTenna:TX:ESPacing:HORizontal. RELativphase Load an antenna pattern file that contains the relative phase description. See 'Antenna pattern file format' BFORming Composite antenna pattern of an antenna array comprising gain and phase is used to simulate analog beamforming. To set the distance, use the corresponding command, for example [:SOURcehw]:FSIMulator:SCM:ANTenna:TX:ESPacing:HORizontal.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AntModCalcGeoMode)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:ANTenna:TX:CALC:MODE {param}')
