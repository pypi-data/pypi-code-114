from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Zp:
	"""Zp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("zp", core, parent)

	def set(self, zero_power: List[str], cellNull=repcap.CellNull.Default, indexNull=repcap.IndexNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CSIS:[CELL<CH0>]:[ZPRS<ST0>]:ZP \n
		Snippet: driver.source.bb.eutra.downlink.csis.cell.zprs.zp.set(zero_power = ['raw1', 'raw2', 'raw3'], cellNull = repcap.CellNull.Default, indexNull = repcap.IndexNull.Default) \n
		Sets the used CSI-RS configurations in the zero transmission power subframes. \n
			:param zero_power: decimal value In the user interface, the 16 bits are set as a hexadecimal value. In the remote control, as a decimal value. Range: 0 to 65535
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Zprs')
		"""
		param = Conversions.list_to_csv_str(zero_power)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:CSIS:CELL{cellNull_cmd_val}:ZPRS{indexNull_cmd_val}:ZP {param}')

	def get(self, cellNull=repcap.CellNull.Default, indexNull=repcap.IndexNull.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CSIS:[CELL<CH0>]:[ZPRS<ST0>]:ZP \n
		Snippet: value: List[str] = driver.source.bb.eutra.downlink.csis.cell.zprs.zp.get(cellNull = repcap.CellNull.Default, indexNull = repcap.IndexNull.Default) \n
		Sets the used CSI-RS configurations in the zero transmission power subframes. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Zprs')
			:return: zero_power: decimal value In the user interface, the 16 bits are set as a hexadecimal value. In the remote control, as a decimal value. Range: 0 to 65535"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:CSIS:CELL{cellNull_cmd_val}:ZPRS{indexNull_cmd_val}:ZP?')
		return Conversions.str_to_str_list(response)
