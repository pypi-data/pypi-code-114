from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Detail:
	"""Detail commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("detail", core, parent)

	def get_bytes(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INFO:L:DETail:BYTes \n
		Snippet: value: int = driver.source.bb.a3Tsc.info.lpy.detail.get_bytes() \n
		Queries the L1 detail signaling length in bytes. \n
			:return: detailed_bytes: integer Range: 25 to 8191
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:INFO:L:DETail:BYTes?')
		return Conversions.str_to_int(response)

	def get_cells(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INFO:L:DETail:CELLs \n
		Snippet: value: int = driver.source.bb.a3Tsc.info.lpy.detail.get_cells() \n
		Queries the L1 detail signaling length in cells. \n
			:return: detail_cells: integer Range: 0 to 5242887
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:INFO:L:DETail:CELLs?')
		return Conversions.str_to_int(response)
