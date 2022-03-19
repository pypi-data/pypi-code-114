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
		"""SCPI: [SOURce<HW>]:FREQuency:STEP:MODE \n
		Snippet: value: enums.FreqStepMode = driver.source.frequency.step.get_mode() \n
		Defines the type of step size to vary the RF frequency at discrete steps with the commands FREQ UP or FREQ DOWN. You can
		define the step mode for each path separately. \n
			:return: mode: DECimal| USER DECimal Increases or decreases the level in steps of ten. USER Increases or decreases the level in increments, set with the command FREQ:STEP[:INCR].
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:STEP:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FreqStepMode)

	def set_mode(self, mode: enums.FreqStepMode) -> None:
		"""SCPI: [SOURce<HW>]:FREQuency:STEP:MODE \n
		Snippet: driver.source.frequency.step.set_mode(mode = enums.FreqStepMode.DECimal) \n
		Defines the type of step size to vary the RF frequency at discrete steps with the commands FREQ UP or FREQ DOWN. You can
		define the step mode for each path separately. \n
			:param mode: DECimal| USER DECimal Increases or decreases the level in steps of ten. USER Increases or decreases the level in increments, set with the command FREQ:STEP[:INCR].
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.FreqStepMode)
		self._core.io.write(f'SOURce<HwInstance>:FREQuency:STEP:MODE {param}')

	def get_increment(self) -> float:
		"""SCPI: [SOURce<HW>]:FREQuency:STEP:[INCRement] \n
		Snippet: value: float = driver.source.frequency.step.get_increment() \n
		Sets the step width. You can use this value to vary the RF frequency with command FREQ UP or FREQ DOWN, if you have
		activated FREQ:STEP:MODE USER. Note: This value also applies to the step width of the rotary knob on the instrument and,
		in user-defined step mode, increases or decreases the frequency. \n
			:return: increment: float Range: 0 Hz to RFmax - 100 kHz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:STEP:INCRement?')
		return Conversions.str_to_float(response)

	def set_increment(self, increment: float) -> None:
		"""SCPI: [SOURce<HW>]:FREQuency:STEP:[INCRement] \n
		Snippet: driver.source.frequency.step.set_increment(increment = 1.0) \n
		Sets the step width. You can use this value to vary the RF frequency with command FREQ UP or FREQ DOWN, if you have
		activated FREQ:STEP:MODE USER. Note: This value also applies to the step width of the rotary knob on the instrument and,
		in user-defined step mode, increases or decreases the frequency. \n
			:param increment: float Range: 0 Hz to RFmax - 100 kHz
		"""
		param = Conversions.decimal_value_to_str(increment)
		self._core.io.write(f'SOURce<HwInstance>:FREQuency:STEP:INCRement {param}')
