from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UlPcrs:
	"""UlPcrs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ulPcrs", core, parent)

	def set(self, dci_ulpcrs: int, subframeNull=repcap.SubframeNull.Default, itemNull=repcap.ItemNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:ENCC:XPDCch:EXTC:ITEM<CH0>:DCIConf:ULPCrs \n
		Snippet: driver.source.bb.v5G.downlink.subf.encc.xpdcch.extc.item.dciConf.ulPcrs.set(dci_ulpcrs = 1, subframeNull = repcap.SubframeNull.Default, itemNull = repcap.ItemNull.Default) \n
		Sets the DCI format field UL dual PCRS for single-layer transmission. \n
			:param dci_ulpcrs: integer 0: scheduled uses a PCRS AP (corresponding to a DM-RS AP) 1: scheduled uses two PCRS APs Range: 0 to 1
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param itemNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Item')
		"""
		param = Conversions.decimal_value_to_str(dci_ulpcrs)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		itemNull_cmd_val = self._cmd_group.get_repcap_cmd_value(itemNull, repcap.ItemNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:ENCC:XPDCch:EXTC:ITEM{itemNull_cmd_val}:DCIConf:ULPCrs {param}')

	def get(self, subframeNull=repcap.SubframeNull.Default, itemNull=repcap.ItemNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:ENCC:XPDCch:EXTC:ITEM<CH0>:DCIConf:ULPCrs \n
		Snippet: value: int = driver.source.bb.v5G.downlink.subf.encc.xpdcch.extc.item.dciConf.ulPcrs.get(subframeNull = repcap.SubframeNull.Default, itemNull = repcap.ItemNull.Default) \n
		Sets the DCI format field UL dual PCRS for single-layer transmission. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param itemNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Item')
			:return: dci_ulpcrs: integer 0: scheduled uses a PCRS AP (corresponding to a DM-RS AP) 1: scheduled uses two PCRS APs Range: 0 to 1"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		itemNull_cmd_val = self._cmd_group.get_repcap_cmd_value(itemNull, repcap.ItemNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:ENCC:XPDCch:EXTC:ITEM{itemNull_cmd_val}:DCIConf:ULPCrs?')
		return Conversions.str_to_int(response)
