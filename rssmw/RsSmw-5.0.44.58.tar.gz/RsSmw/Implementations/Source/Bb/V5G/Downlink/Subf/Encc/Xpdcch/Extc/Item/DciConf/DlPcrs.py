from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import enums
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DlPcrs:
	"""DlPcrs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dlPcrs", core, parent)

	def set(self, dci_dl_pcrs: enums.V5GdCiDlPcrs, subframeNull=repcap.SubframeNull.Default, itemNull=repcap.ItemNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:ENCC:XPDCch:EXTC:ITEM<CH0>:DCIConf:DLPCrs \n
		Snippet: driver.source.bb.v5G.downlink.subf.encc.xpdcch.extc.item.dciConf.dlPcrs.set(dci_dl_pcrs = enums.V5GdCiDlPcrs.AP60, subframeNull = repcap.SubframeNull.Default, itemNull = repcap.ItemNull.Default) \n
		Sets the DCI format field DL PCRS to specify antenna ports used by PCRS signal. \n
			:param dci_dl_pcrs: NONE| AP60| AP61| AP6061 No PCRS, PCRS on AP 60, 61, or APs 60-61
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param itemNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Item')
		"""
		param = Conversions.enum_scalar_to_str(dci_dl_pcrs, enums.V5GdCiDlPcrs)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		itemNull_cmd_val = self._cmd_group.get_repcap_cmd_value(itemNull, repcap.ItemNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:ENCC:XPDCch:EXTC:ITEM{itemNull_cmd_val}:DCIConf:DLPCrs {param}')

	# noinspection PyTypeChecker
	def get(self, subframeNull=repcap.SubframeNull.Default, itemNull=repcap.ItemNull.Default) -> enums.V5GdCiDlPcrs:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:ENCC:XPDCch:EXTC:ITEM<CH0>:DCIConf:DLPCrs \n
		Snippet: value: enums.V5GdCiDlPcrs = driver.source.bb.v5G.downlink.subf.encc.xpdcch.extc.item.dciConf.dlPcrs.get(subframeNull = repcap.SubframeNull.Default, itemNull = repcap.ItemNull.Default) \n
		Sets the DCI format field DL PCRS to specify antenna ports used by PCRS signal. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param itemNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Item')
			:return: dci_dl_pcrs: NONE| AP60| AP61| AP6061 No PCRS, PCRS on AP 60, 61, or APs 60-61"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		itemNull_cmd_val = self._cmd_group.get_repcap_cmd_value(itemNull, repcap.ItemNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:ENCC:XPDCch:EXTC:ITEM{itemNull_cmd_val}:DCIConf:DLPCrs?')
		return Conversions.str_to_scalar_enum(response, enums.V5GdCiDlPcrs)
