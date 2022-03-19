from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	# noinspection PyTypeChecker
	def get_detect(self) -> enums.TmastConn:
		"""SCPI: [SOURce<HW>]:FSIMulator:FREQuency:DETect \n
		Snippet: value: enums.TmastConn = driver.source.fsimulator.frequency.get_detect() \n
		Queries the output interface the steam used to estimate the dedicated frequency is mapped to. \n
			:return: detect_primary: RFA| BBMM1| RFB| BBMM2| IQOUT1| IQOUT2| FAD1| FAD2| FAD4| FAD3| DEF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:FREQuency:DETect?')
		return Conversions.str_to_scalar_enum(response, enums.TmastConn)

	def get_value(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:FREQuency \n
		Snippet: value: float = driver.source.fsimulator.frequency.get_value() \n
			INTRO_CMD_HELP: The effect depends on the selected mode: \n
			- If [:SOURce<hw>]:FSIMulator:SDEStinationRF is selected, queries the estimated RF frequency.
			- If [:SOURce<hw>]:FSIMulator:SDEStinationBB is selected, sets the frequency used for the calculation of the Doppler shift. \n
			:return: frequency: float Range: 1E5 to 100E9, Unit: Hz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:FREQuency?')
		return Conversions.str_to_float(response)

	def set_value(self, frequency: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:FREQuency \n
		Snippet: driver.source.fsimulator.frequency.set_value(frequency = 1.0) \n
			INTRO_CMD_HELP: The effect depends on the selected mode: \n
			- If [:SOURce<hw>]:FSIMulator:SDEStinationRF is selected, queries the estimated RF frequency.
			- If [:SOURce<hw>]:FSIMulator:SDEStinationBB is selected, sets the frequency used for the calculation of the Doppler shift. \n
			:param frequency: float Range: 1E5 to 100E9, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:FREQuency {param}')
