from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NoGroups:
	"""NoGroups commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("noGroups", core, parent)

	def set(self, group_count: int, subframeNull=repcap.SubframeNull.Default, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PHICh:[CELL<CCIDX>]:NOGRoups \n
		Snippet: driver.source.bb.eutra.downlink.subf.encc.phich.cell.noGroups.set(group_count = 1, subframeNull = repcap.SubframeNull.Default, cellNull = repcap.CellNull.Default) \n
		Queries the number of available PHICH groups. \n
			:param group_count: integer Range: 0 to dynamic
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(group_count)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PHICh:CELL{cellNull_cmd_val}:NOGRoups {param}')

	def get(self, subframeNull=repcap.SubframeNull.Default, cellNull=repcap.CellNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PHICh:[CELL<CCIDX>]:NOGRoups \n
		Snippet: value: int = driver.source.bb.eutra.downlink.subf.encc.phich.cell.noGroups.get(subframeNull = repcap.SubframeNull.Default, cellNull = repcap.CellNull.Default) \n
		Queries the number of available PHICH groups. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: group_count: integer Range: 0 to dynamic"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PHICh:CELL{cellNull_cmd_val}:NOGRoups?')
		return Conversions.str_to_int(response)
