from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dwell:
	"""Dwell commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dwell", core, parent)

	def get_time(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:STAir:DWELl:TIME \n
		Snippet: value: float = driver.source.bb.pramp.ramp.stair.dwell.get_time() \n
		Sets the dwell time for a power step. To activate the dwell time, use command .
		[:SOURce<hw>]:BB:PRAMp:RAMP:STAir:DWELl[:STATe]. \n
			:return: dwell_time: float Range: 5E-9 to 20, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:PRAMp:RAMP:STAir:DWELl:TIME?')
		return Conversions.str_to_float(response)

	def set_time(self, dwell_time: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:STAir:DWELl:TIME \n
		Snippet: driver.source.bb.pramp.ramp.stair.dwell.set_time(dwell_time = 1.0) \n
		Sets the dwell time for a power step. To activate the dwell time, use command .
		[:SOURce<hw>]:BB:PRAMp:RAMP:STAir:DWELl[:STATe]. \n
			:param dwell_time: float Range: 5E-9 to 20, Unit: s
		"""
		param = Conversions.decimal_value_to_str(dwell_time)
		self._core.io.write(f'SOURce<HwInstance>:BB:PRAMp:RAMP:STAir:DWELl:TIME {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:STAir:DWELl:[STATe] \n
		Snippet: value: bool = driver.source.bb.pramp.ramp.stair.dwell.get_state() \n
		Activates the edit mode to set the dwell time.
		To determine the dwell time, use command [:SOURce<hw>]:BB:PRAMp:RAMP:STAir:DWELl:TIME. \n
			:return: enable_dwell: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:PRAMp:RAMP:STAir:DWELl:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, enable_dwell: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:STAir:DWELl:[STATe] \n
		Snippet: driver.source.bb.pramp.ramp.stair.dwell.set_state(enable_dwell = False) \n
		Activates the edit mode to set the dwell time.
		To determine the dwell time, use command [:SOURce<hw>]:BB:PRAMp:RAMP:STAir:DWELl:TIME. \n
			:param enable_dwell: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(enable_dwell)
		self._core.io.write(f'SOURce<HwInstance>:BB:PRAMp:RAMP:STAir:DWELl:STATe {param}')
