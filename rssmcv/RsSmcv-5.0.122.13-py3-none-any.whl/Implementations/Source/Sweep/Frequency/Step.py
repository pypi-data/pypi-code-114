from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Step:
	"""Step commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("step", core, parent)

	def get_logarithmic(self) -> float:
		"""SCPI: [SOURce<HW>]:SWEep:[FREQuency]:STEP:LOGarithmic \n
		Snippet: value: float = driver.source.sweep.frequency.step.get_logarithmic() \n
		Sets a logarithmically determined step width for the RF frequency sweep. The value is added at each sweep step to the
		current frequency. See 'Correlating parameters in sweep mode'. \n
			:return: logarithmic: float The unit is mandatory. Range: 0.01 to 100, Unit: PCT
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:SWEep:FREQuency:STEP:LOGarithmic?')
		return Conversions.str_to_float(response)

	def set_logarithmic(self, logarithmic: float) -> None:
		"""SCPI: [SOURce<HW>]:SWEep:[FREQuency]:STEP:LOGarithmic \n
		Snippet: driver.source.sweep.frequency.step.set_logarithmic(logarithmic = 1.0) \n
		Sets a logarithmically determined step width for the RF frequency sweep. The value is added at each sweep step to the
		current frequency. See 'Correlating parameters in sweep mode'. \n
			:param logarithmic: float The unit is mandatory. Range: 0.01 to 100, Unit: PCT
		"""
		param = Conversions.decimal_value_to_str(logarithmic)
		self._core.io.write(f'SOURce<HwInstance>:SWEep:FREQuency:STEP:LOGarithmic {param}')

	def get_linear(self) -> float:
		"""SCPI: [SOURce<HW>]:SWEep:[FREQuency]:STEP:[LINear] \n
		Snippet: value: float = driver.source.sweep.frequency.step.get_linear() \n
		Sets the step width for linear sweeps. See 'Correlating parameters in sweep mode'. Omit the optional keywords so that the
		command is SCPI-compliant. \n
			:return: linear: float Range: 0.001 Hz to (STOP - STARt)
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:SWEep:FREQuency:STEP:LINear?')
		return Conversions.str_to_float(response)

	def set_linear(self, linear: float) -> None:
		"""SCPI: [SOURce<HW>]:SWEep:[FREQuency]:STEP:[LINear] \n
		Snippet: driver.source.sweep.frequency.step.set_linear(linear = 1.0) \n
		Sets the step width for linear sweeps. See 'Correlating parameters in sweep mode'. Omit the optional keywords so that the
		command is SCPI-compliant. \n
			:param linear: float Range: 0.001 Hz to (STOP - STARt)
		"""
		param = Conversions.decimal_value_to_str(linear)
		self._core.io.write(f'SOURce<HwInstance>:SWEep:FREQuency:STEP:LINear {param}')
