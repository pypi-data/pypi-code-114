from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Throughput:
	"""Throughput commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("throughput", core, parent)

	def get_delay(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DM:SMODulation:THRoughput:DELay \n
		Snippet: value: int = driver.source.bb.dm.smodulation.throughput.get_delay() \n
		Queries the throughput delay from the data input to the RF output in the case of external modulation. \n
			:return: delay: integer Range: -100 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:SMODulation:THRoughput:DELay?')
		return Conversions.str_to_int(response)
