from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class QsControl:
	"""QsControl commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qsControl", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:QSControl:STATe \n
		Snippet: value: bool = driver.source.bb.wlad.pconfig.mac.qsControl.get_state() \n
		Enables/disables the QoS control. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:QSControl:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:QSControl:STATe \n
		Snippet: driver.source.bb.wlad.pconfig.mac.qsControl.set_state(state = False) \n
		Enables/disables the QoS control. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:QSControl:STATe {param}')

	def get_value(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:QSControl \n
		Snippet: value: List[str] = driver.source.bb.wlad.pconfig.mac.qsControl.get_value() \n
		Sets the value for the QoS control field. \n
			:return: qs_control: 16 bits
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:QSControl?')
		return Conversions.str_to_str_list(response)

	def set_value(self, qs_control: List[str]) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:QSControl \n
		Snippet: driver.source.bb.wlad.pconfig.mac.qsControl.set_value(qs_control = ['raw1', 'raw2', 'raw3']) \n
		Sets the value for the QoS control field. \n
			:param qs_control: 16 bits
		"""
		param = Conversions.list_to_csv_str(qs_control)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:QSControl {param}')
