from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Step:
	"""Step commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("step", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.FreqStepMode:
		"""SCPI: [SOURce<HW>]:POWer:STEP:MODE \n
		Snippet: value: enums.FreqStepMode = driver.source.power.step.get_mode() \n
		Defines the type of step width to vary the RF output power step-by-step with the commands POW UP or POW DOWN. \n
			:return: mode: DECimal| USER DECimal Increases or decreases the level in steps of ten. USER Increases or decreases the level in increments, determined with the command [:SOURcehw]:POWer:STEP[:INCRement].
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:STEP:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FreqStepMode)

	def set_mode(self, mode: enums.FreqStepMode) -> None:
		"""SCPI: [SOURce<HW>]:POWer:STEP:MODE \n
		Snippet: driver.source.power.step.set_mode(mode = enums.FreqStepMode.DECimal) \n
		Defines the type of step width to vary the RF output power step-by-step with the commands POW UP or POW DOWN. \n
			:param mode: DECimal| USER DECimal Increases or decreases the level in steps of ten. USER Increases or decreases the level in increments, determined with the command [:SOURcehw]:POWer:STEP[:INCRement].
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.FreqStepMode)
		self._core.io.write(f'SOURce<HwInstance>:POWer:STEP:MODE {param}')

	def get_increment(self) -> float:
		"""SCPI: [SOURce<HW>]:POWer:STEP:[INCRement] \n
		Snippet: value: float = driver.source.power.step.get_increment() \n
		Specifies the step width in the appropriate path for POW:STEP:MODE USER. To adjust the level step-by-step with this
		increment value, use the command POW UP, or POW DOWN. \n
			:return: increment: float Range: 0 to 200, Unit: dB
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:STEP:INCRement?')
		return Conversions.str_to_float(response)

	def set_increment(self, increment: float) -> None:
		"""SCPI: [SOURce<HW>]:POWer:STEP:[INCRement] \n
		Snippet: driver.source.power.step.set_increment(increment = 1.0) \n
		Specifies the step width in the appropriate path for POW:STEP:MODE USER. To adjust the level step-by-step with this
		increment value, use the command POW UP, or POW DOWN. \n
			:param increment: float Range: 0 to 200, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(increment)
		self._core.io.write(f'SOURce<HwInstance>:POWer:STEP:INCRement {param}')
