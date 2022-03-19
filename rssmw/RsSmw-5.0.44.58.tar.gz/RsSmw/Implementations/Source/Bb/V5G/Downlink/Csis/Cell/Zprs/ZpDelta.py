from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ZpDelta:
	"""ZpDelta commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("zpDelta", core, parent)

	def get(self, cellNull=repcap.CellNull.Default, indexNull=repcap.IndexNull.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:CSIS:[CELL<CH0>]:[ZPRS<ST0>]:ZPDelta \n
		Snippet: value: List[str] = driver.source.bb.v5G.downlink.csis.cell.zprs.zpDelta.get(cellNull = repcap.CellNull.Default, indexNull = repcap.IndexNull.Default) \n
		No command help available \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Zprs')
			:return: zero_power_offset: No help available"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:CSIS:CELL{cellNull_cmd_val}:ZPRS{indexNull_cmd_val}:ZPDelta?')
		return Conversions.str_to_str_list(response)
