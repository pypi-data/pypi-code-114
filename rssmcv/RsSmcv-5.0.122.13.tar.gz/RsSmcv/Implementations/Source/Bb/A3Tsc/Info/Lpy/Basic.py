from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Basic:
	"""Basic commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("basic", core, parent)

	def get_bytes(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INFO:L:BASic:BYTes \n
		Snippet: value: int = driver.source.bb.a3Tsc.info.lpy.basic.get_bytes() \n
		Queries the L1 basic signaling length in bytes. \n
			:return: basic_bytes: integer Range: 25 to 25
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:INFO:L:BASic:BYTes?')
		return Conversions.str_to_int(response)

	def get_cells(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INFO:L:BASic:CELLs \n
		Snippet: value: int = driver.source.bb.a3Tsc.info.lpy.basic.get_cells() \n
		Queries the L1 basic signaling length in cells. \n
			:return: basic_cells: integer Range: 69 to 3820
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:INFO:L:BASic:CELLs?')
		return Conversions.str_to_int(response)
