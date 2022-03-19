from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uplane:
	"""Uplane commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplane", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UPLane:STATe \n
		Snippet: value: bool = driver.source.bb.eutra.uplane.get_state() \n
		Turns user plane data generation according to the O-RAN standard on and off. \n
			:return: up_lane_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UPLane:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, up_lane_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UPLane:STATe \n
		Snippet: driver.source.bb.eutra.uplane.set_state(up_lane_state = False) \n
		Turns user plane data generation according to the O-RAN standard on and off. \n
			:param up_lane_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(up_lane_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UPLane:STATe {param}')
