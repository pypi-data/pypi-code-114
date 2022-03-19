from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gap:
	"""Gap commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gap", core, parent)

	def set(self, gap: bool, subframeNull=repcap.SubframeNull.Default, itemNull=repcap.ItemNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PDCCh:EXTC:ITEM<CH0>:DCIConf:GAP \n
		Snippet: driver.source.bb.eutra.downlink.subf.encc.pdcch.extc.item.dciConf.gap.set(gap = False, subframeNull = repcap.SubframeNull.Default, itemNull = repcap.ItemNull.Default) \n
		Sets the DCI Format 1A/1B/1C/1D field GAP value. \n
			:param gap: ON| OFF
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param itemNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Item')
		"""
		param = Conversions.bool_to_str(gap)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		itemNull_cmd_val = self._cmd_group.get_repcap_cmd_value(itemNull, repcap.ItemNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PDCCh:EXTC:ITEM{itemNull_cmd_val}:DCIConf:GAP {param}')

	def get(self, subframeNull=repcap.SubframeNull.Default, itemNull=repcap.ItemNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PDCCh:EXTC:ITEM<CH0>:DCIConf:GAP \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.subf.encc.pdcch.extc.item.dciConf.gap.get(subframeNull = repcap.SubframeNull.Default, itemNull = repcap.ItemNull.Default) \n
		Sets the DCI Format 1A/1B/1C/1D field GAP value. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param itemNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Item')
			:return: gap: ON| OFF"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		itemNull_cmd_val = self._cmd_group.get_repcap_cmd_value(itemNull, repcap.ItemNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PDCCh:EXTC:ITEM{itemNull_cmd_val}:DCIConf:GAP?')
		return Conversions.str_to_bool(response)
