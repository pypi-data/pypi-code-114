from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Zpi:
	"""Zpi commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("zpi", core, parent)

	def set(self, zero_pow_conf: List[str], cellNull=repcap.CellNull.Default, indexNull=repcap.IndexNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CSIS:[CELL<CH0>]:[ZPRS<ST0>]:ZPI \n
		Snippet: driver.source.bb.eutra.downlink.csis.cell.zprs.zpi.set(zero_pow_conf = ['raw1', 'raw2', 'raw3'], cellNull = repcap.CellNull.Default, indexNull = repcap.IndexNull.Default) \n
		Sets the parameter ICSI-RS for CSI-RS with zero transmission power. \n
			:param zero_pow_conf: integer Range: 0 to 154
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Zprs')
		"""
		param = Conversions.list_to_csv_str(zero_pow_conf)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:CSIS:CELL{cellNull_cmd_val}:ZPRS{indexNull_cmd_val}:ZPI {param}')

	def get(self, cellNull=repcap.CellNull.Default, indexNull=repcap.IndexNull.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CSIS:[CELL<CH0>]:[ZPRS<ST0>]:ZPI \n
		Snippet: value: List[str] = driver.source.bb.eutra.downlink.csis.cell.zprs.zpi.get(cellNull = repcap.CellNull.Default, indexNull = repcap.IndexNull.Default) \n
		Sets the parameter ICSI-RS for CSI-RS with zero transmission power. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Zprs')
			:return: zero_pow_conf: integer Range: 0 to 154"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:CSIS:CELL{cellNull_cmd_val}:ZPRS{indexNull_cmd_val}:ZPI?')
		return Conversions.str_to_str_list(response)
