from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PreSweep:
	"""PreSweep commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("preSweep", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:PRESweep:STATe \n
		Snippet: value: bool = driver.source.bb.pramp.ramp.preSweep.get_state() \n
		Activates the pre-sweep. To determine the pre-sweep power, use command [:SOURce<hw>]:BB:PRAMp:RAMP:PRESweep[:LEVel]. \n
			:return: enable_pre_sweep: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:PRAMp:RAMP:PRESweep:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, enable_pre_sweep: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:PRESweep:STATe \n
		Snippet: driver.source.bb.pramp.ramp.preSweep.set_state(enable_pre_sweep = False) \n
		Activates the pre-sweep. To determine the pre-sweep power, use command [:SOURce<hw>]:BB:PRAMp:RAMP:PRESweep[:LEVel]. \n
			:param enable_pre_sweep: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(enable_pre_sweep)
		self._core.io.write(f'SOURce<HwInstance>:BB:PRAMp:RAMP:PRESweep:STATe {param}')

	def get_time(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:PRESweep:TIME \n
		Snippet: value: float = driver.source.bb.pramp.ramp.preSweep.get_time() \n
		Queries the calculated pre-sweep time. \n
			:return: pre_sweep_time: float Range: 0 to 20
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:PRAMp:RAMP:PRESweep:TIME?')
		return Conversions.str_to_float(response)

	def set_time(self, pre_sweep_time: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:PRESweep:TIME \n
		Snippet: driver.source.bb.pramp.ramp.preSweep.set_time(pre_sweep_time = 1.0) \n
		Queries the calculated pre-sweep time. \n
			:param pre_sweep_time: float Range: 0 to 20
		"""
		param = Conversions.decimal_value_to_str(pre_sweep_time)
		self._core.io.write(f'SOURce<HwInstance>:BB:PRAMp:RAMP:PRESweep:TIME {param}')

	def get_level(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:PRESweep:[LEVel] \n
		Snippet: value: float = driver.source.bb.pramp.ramp.preSweep.get_level() \n
		Sets the pre-sweep power. To activate pre-sweep, use command [:SOURce<hw>]:BB:PRAMp:RAMP:PRESweep:STATe. \n
			:return: pre_sweep_level: float Range: 0 to 20, Unit: dB
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:PRAMp:RAMP:PRESweep:LEVel?')
		return Conversions.str_to_float(response)

	def set_level(self, pre_sweep_level: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:PRESweep:[LEVel] \n
		Snippet: driver.source.bb.pramp.ramp.preSweep.set_level(pre_sweep_level = 1.0) \n
		Sets the pre-sweep power. To activate pre-sweep, use command [:SOURce<hw>]:BB:PRAMp:RAMP:PRESweep:STATe. \n
			:param pre_sweep_level: float Range: 0 to 20, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(pre_sweep_level)
		self._core.io.write(f'SOURce<HwInstance>:BB:PRAMp:RAMP:PRESweep:LEVel {param}')
