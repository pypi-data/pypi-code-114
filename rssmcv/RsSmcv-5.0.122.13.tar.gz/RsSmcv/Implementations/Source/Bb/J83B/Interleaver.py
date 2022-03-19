from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Interleaver:
	"""Interleaver commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("interleaver", core, parent)

	def get_mode(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:J83B:INTerleaver:MODE \n
		Snippet: value: int = driver.source.bb.j83B.interleaver.get_mode() \n
		Sets the interleaver mode. \n
			:return: interleaver_mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:J83B:INTerleaver:MODE?')
		return Conversions.str_to_int(response)

	def set_mode(self, interleaver_mode: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:J83B:INTerleaver:MODE \n
		Snippet: driver.source.bb.j83B.interleaver.set_mode(interleaver_mode = 1) \n
		Sets the interleaver mode. \n
			:param interleaver_mode: No help available
		"""
		param = Conversions.decimal_value_to_str(interleaver_mode)
		self._core.io.write(f'SOURce<HwInstance>:BB:J83B:INTerleaver:MODE {param}')
