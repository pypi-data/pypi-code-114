from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Step:
	"""Step commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("step", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.FreqStepMode:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:DIGital:POWer:STEP:MODE \n
		Snippet: value: enums.FreqStepMode = driver.source.iq.output.digital.power.step.get_mode() \n
		Defines the type of step size to vary the digital output power step by step. \n
			:return: mode: DECimal| USER DECimal Increases or decreases the level in steps of 10 dB. USER Increases or decreases the level in increments, determined with the command [:SOURcehw]:IQ:OUTPut:DIGital:POWer:STEP[:INCRement].
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:DIGital:POWer:STEP:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FreqStepMode)

	def set_mode(self, mode: enums.FreqStepMode) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:DIGital:POWer:STEP:MODE \n
		Snippet: driver.source.iq.output.digital.power.step.set_mode(mode = enums.FreqStepMode.DECimal) \n
		Defines the type of step size to vary the digital output power step by step. \n
			:param mode: DECimal| USER DECimal Increases or decreases the level in steps of 10 dB. USER Increases or decreases the level in increments, determined with the command [:SOURcehw]:IQ:OUTPut:DIGital:POWer:STEP[:INCRement].
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.FreqStepMode)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:DIGital:POWer:STEP:MODE {param}')

	def get_increment(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:DIGital:POWer:STEP:[INCRement] \n
		Snippet: value: float = driver.source.iq.output.digital.power.step.get_increment() \n
		Sets the step width. Use this value to vary the digital I/Q output level step-by-step. \n
			:return: ipart_increment: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:DIGital:POWer:STEP:INCRement?')
		return Conversions.str_to_float(response)

	def set_increment(self, ipart_increment: float) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:DIGital:POWer:STEP:[INCRement] \n
		Snippet: driver.source.iq.output.digital.power.step.set_increment(ipart_increment = 1.0) \n
		Sets the step width. Use this value to vary the digital I/Q output level step-by-step. \n
			:param ipart_increment: float Range: 0 to 100
		"""
		param = Conversions.decimal_value_to_str(ipart_increment)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:DIGital:POWer:STEP:INCRement {param}')
