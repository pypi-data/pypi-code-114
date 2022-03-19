from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Blank:
	"""Blank commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("blank", core, parent)

	def get_time(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:BLANk:TIME \n
		Snippet: value: float = driver.source.bb.pramp.ramp.blank.get_time() \n
		Sets the RF blanking time. To activate RF blanking, use command[:SOURce<hw>]:BB:PRAMp:RAMP:BLANk[:STATe]. \n
			:return: rf_blanking: float Range: 5E-9 to 1E-3, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:PRAMp:RAMP:BLANk:TIME?')
		return Conversions.str_to_float(response)

	def set_time(self, rf_blanking: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:BLANk:TIME \n
		Snippet: driver.source.bb.pramp.ramp.blank.set_time(rf_blanking = 1.0) \n
		Sets the RF blanking time. To activate RF blanking, use command[:SOURce<hw>]:BB:PRAMp:RAMP:BLANk[:STATe]. \n
			:param rf_blanking: float Range: 5E-9 to 1E-3, Unit: s
		"""
		param = Conversions.decimal_value_to_str(rf_blanking)
		self._core.io.write(f'SOURce<HwInstance>:BB:PRAMp:RAMP:BLANk:TIME {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:BLANk:[STATe] \n
		Snippet: value: bool = driver.source.bb.pramp.ramp.blank.get_state() \n
		Activates the RF blanking. To determine the blanking interval, use command [:SOURce<hw>]:BB:PRAMp:RAMP:BLANk[:STATe]. \n
			:return: enable_rf_blank: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:PRAMp:RAMP:BLANk:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, enable_rf_blank: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:BLANk:[STATe] \n
		Snippet: driver.source.bb.pramp.ramp.blank.set_state(enable_rf_blank = False) \n
		Activates the RF blanking. To determine the blanking interval, use command [:SOURce<hw>]:BB:PRAMp:RAMP:BLANk[:STATe]. \n
			:param enable_rf_blank: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(enable_rf_blank)
		self._core.io.write(f'SOURce<HwInstance>:BB:PRAMp:RAMP:BLANk:STATe {param}')
