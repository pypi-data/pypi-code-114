from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tp:
	"""Tp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tp", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:TP:[STATe] \n
		Snippet: value: bool = driver.source.bb.radio.fm.rds.tp.get_state() \n
		Enable/disables the traffic program flag. \n
			:return: tp: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:TP:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, tp: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:TP:[STATe] \n
		Snippet: driver.source.bb.radio.fm.rds.tp.set_state(tp = False) \n
		Enable/disables the traffic program flag. \n
			:param tp: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(tp)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:TP:STATe {param}')
