from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dual:
	"""Dual commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dual", core, parent)

	def get_pilot(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DTMB:DUAL:PILot \n
		Snippet: value: bool = driver.source.bb.dtmb.dual.get_pilot() \n
		Enables/disables insertion of the dual pilot tone. \n
			:return: dtmb_dual_pilot: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DTMB:DUAL:PILot?')
		return Conversions.str_to_bool(response)

	def set_pilot(self, dtmb_dual_pilot: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DTMB:DUAL:PILot \n
		Snippet: driver.source.bb.dtmb.dual.set_pilot(dtmb_dual_pilot = False) \n
		Enables/disables insertion of the dual pilot tone. \n
			:param dtmb_dual_pilot: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(dtmb_dual_pilot)
		self._core.io.write(f'SOURce<HwInstance>:BB:DTMB:DUAL:PILot {param}')
