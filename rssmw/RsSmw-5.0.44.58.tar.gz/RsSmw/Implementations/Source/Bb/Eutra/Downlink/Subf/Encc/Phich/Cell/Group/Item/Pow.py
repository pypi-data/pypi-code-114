from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pow:
	"""Pow commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pow", core, parent)

	def set(self, power: float, subframeNull=repcap.SubframeNull.Default, cellNull=repcap.CellNull.Default, groupNull=repcap.GroupNull.Default, itemNull=repcap.ItemNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PHICh:[CELL<CCIDX>]:GROup<GR0>:ITEM<USER0>:POW \n
		Snippet: driver.source.bb.eutra.downlink.subf.encc.phich.cell.group.item.pow.set(power = 1.0, subframeNull = repcap.SubframeNull.Default, cellNull = repcap.CellNull.Default, groupNull = repcap.GroupNull.Default, itemNull = repcap.ItemNull.Default) \n
		Sets the power of the individual PHICHs. \n
			:param power: float Range: -80 to 10
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Group')
			:param itemNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Item')
		"""
		param = Conversions.decimal_value_to_str(power)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		itemNull_cmd_val = self._cmd_group.get_repcap_cmd_value(itemNull, repcap.ItemNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PHICh:CELL{cellNull_cmd_val}:GROup{groupNull_cmd_val}:ITEM{itemNull_cmd_val}:POW {param}')

	def get(self, subframeNull=repcap.SubframeNull.Default, cellNull=repcap.CellNull.Default, groupNull=repcap.GroupNull.Default, itemNull=repcap.ItemNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PHICh:[CELL<CCIDX>]:GROup<GR0>:ITEM<USER0>:POW \n
		Snippet: value: float = driver.source.bb.eutra.downlink.subf.encc.phich.cell.group.item.pow.get(subframeNull = repcap.SubframeNull.Default, cellNull = repcap.CellNull.Default, groupNull = repcap.GroupNull.Default, itemNull = repcap.ItemNull.Default) \n
		Sets the power of the individual PHICHs. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Group')
			:param itemNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Item')
			:return: power: float Range: -80 to 10"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		itemNull_cmd_val = self._cmd_group.get_repcap_cmd_value(itemNull, repcap.ItemNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PHICh:CELL{cellNull_cmd_val}:GROup{groupNull_cmd_val}:ITEM{itemNull_cmd_val}:POW?')
		return Conversions.str_to_float(response)
