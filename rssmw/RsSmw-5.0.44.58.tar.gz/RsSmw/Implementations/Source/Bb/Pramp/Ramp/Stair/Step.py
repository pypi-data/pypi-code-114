from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Step:
	"""Step commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("step", core, parent)

	def get_level(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:STAir:STEP:LEVel \n
		Snippet: value: float = driver.source.bb.pramp.ramp.stair.step.get_level() \n
		Sets the power step size. \n
			:return: step: float Range: 0.01 to 10, Unit: dB
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:PRAMp:RAMP:STAir:STEP:LEVel?')
		return Conversions.str_to_float(response)

	def set_level(self, step: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:STAir:STEP:LEVel \n
		Snippet: driver.source.bb.pramp.ramp.stair.step.set_level(step = 1.0) \n
		Sets the power step size. \n
			:param step: float Range: 0.01 to 10, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(step)
		self._core.io.write(f'SOURce<HwInstance>:BB:PRAMp:RAMP:STAir:STEP:LEVel {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:STAir:STEP:[STATe] \n
		Snippet: value: bool = driver.source.bb.pramp.ramp.stair.step.get_state() \n
		Activates the edit mode to set the power step.
		To determine the power step size, use command [:SOURce<hw>]:BB:PRAMp:RAMP:STAir:STEP:LEVel. \n
			:return: enable_power_step: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:PRAMp:RAMP:STAir:STEP:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, enable_power_step: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:STAir:STEP:[STATe] \n
		Snippet: driver.source.bb.pramp.ramp.stair.step.set_state(enable_power_step = False) \n
		Activates the edit mode to set the power step.
		To determine the power step size, use command [:SOURce<hw>]:BB:PRAMp:RAMP:STAir:STEP:LEVel. \n
			:param enable_power_step: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(enable_power_step)
		self._core.io.write(f'SOURce<HwInstance>:BB:PRAMp:RAMP:STAir:STEP:STATe {param}')
