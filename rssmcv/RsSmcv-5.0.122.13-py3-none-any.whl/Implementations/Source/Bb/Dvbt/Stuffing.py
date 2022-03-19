from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stuffing:
	"""Stuffing commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stuffing", core, parent)

	def get_low(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVBT:STUFfing:LOW \n
		Snippet: value: bool = driver.source.bb.dvbt.stuffing.get_low() \n
		Queries the stuffing state that is active for HP path and LP path. \n
			:return: stuffing_lp: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:STUFfing:LOW?')
		return Conversions.str_to_bool(response)

	def get_high(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVBT:STUFfing:[HIGH] \n
		Snippet: value: bool = driver.source.bb.dvbt.stuffing.get_high() \n
		Queries the stuffing state that is active for HP path and LP path. \n
			:return: stuffing_hp: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:STUFfing:HIGH?')
		return Conversions.str_to_bool(response)
