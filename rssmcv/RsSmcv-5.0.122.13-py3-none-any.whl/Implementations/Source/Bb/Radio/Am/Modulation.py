from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modulation:
	"""Modulation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	def get_depth(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:RADio:AM:MODulation:DEPTh \n
		Snippet: value: int = driver.source.bb.radio.am.modulation.get_depth() \n
		Displays the modulation depth. \n
			:return: mod_depth: integer Range: 0 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:AM:MODulation:DEPTh?')
		return Conversions.str_to_int(response)
