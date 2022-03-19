from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Timeslice:
	"""Timeslice commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("timeslice", core, parent)

	def get_low(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVBT:TIMeslice:LOW \n
		Snippet: value: bool = driver.source.bb.dvbt.timeslice.get_low() \n
		Enables/disables time slicing. If enabled, 1 TPS bit (s48) is used to signal that at least one data stream with time
		slicing exists in the multiplex. \n
			:return: time_slicing_lp: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:TIMeslice:LOW?')
		return Conversions.str_to_bool(response)

	def set_low(self, time_slicing_lp: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:TIMeslice:LOW \n
		Snippet: driver.source.bb.dvbt.timeslice.set_low(time_slicing_lp = False) \n
		Enables/disables time slicing. If enabled, 1 TPS bit (s48) is used to signal that at least one data stream with time
		slicing exists in the multiplex. \n
			:param time_slicing_lp: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(time_slicing_lp)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:TIMeslice:LOW {param}')

	def get_high(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVBT:TIMeslice:[HIGH] \n
		Snippet: value: bool = driver.source.bb.dvbt.timeslice.get_high() \n
		Enables/disables time slicing. If enabled, 1 TPS bit (s48) is used to signal that at least one data stream with time
		slicing exists in the multiplex. \n
			:return: time_slicing_hp: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:TIMeslice:HIGH?')
		return Conversions.str_to_bool(response)

	def set_high(self, time_slicing_hp: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:TIMeslice:[HIGH] \n
		Snippet: driver.source.bb.dvbt.timeslice.set_high(time_slicing_hp = False) \n
		Enables/disables time slicing. If enabled, 1 TPS bit (s48) is used to signal that at least one data stream with time
		slicing exists in the multiplex. \n
			:param time_slicing_hp: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(time_slicing_hp)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:TIMeslice:HIGH {param}')
