from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ccrc:
	"""Ccrc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ccrc", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:CCRC:STATe \n
		Snippet: value: bool = driver.source.bb.btooth.ccrc.get_state() \n
		Enables/disables the corruption of CRC for every second generated packet. If enabled, only 50% of packets are generated
		with correct CRC. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:CCRC:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:CCRC:STATe \n
		Snippet: driver.source.bb.btooth.ccrc.set_state(state = False) \n
		Enables/disables the corruption of CRC for every second generated packet. If enabled, only 50% of packets are generated
		with correct CRC. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:CCRC:STATe {param}')
