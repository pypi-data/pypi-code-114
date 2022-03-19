from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import enums
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CbSymbol:
	"""CbSymbol commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cbSymbol", core, parent)

	def set(self, dci_cb_symb_ind: enums.V5GdCiCbSym, subframeNull=repcap.SubframeNull.Default, itemNull=repcap.ItemNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:ENCC:XPDCch:EXTC:ITEM<CH0>:DCIConf:CBSYmbol \n
		Snippet: driver.source.bb.v5G.downlink.subf.encc.xpdcch.extc.item.dciConf.cbSymbol.set(dci_cb_symb_ind = enums.V5GdCiCbSym.S12, subframeNull = repcap.SubframeNull.Default, itemNull = repcap.ItemNull.Default) \n
		Sets the DCI format field OFDM symbol index for CSI-RS / BRRS. \n
			:param dci_cb_symb_ind: S12| S13| S1213 13th symbol, 14th symbol, 13th and 14th symbol
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param itemNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Item')
		"""
		param = Conversions.enum_scalar_to_str(dci_cb_symb_ind, enums.V5GdCiCbSym)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		itemNull_cmd_val = self._cmd_group.get_repcap_cmd_value(itemNull, repcap.ItemNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:ENCC:XPDCch:EXTC:ITEM{itemNull_cmd_val}:DCIConf:CBSYmbol {param}')

	# noinspection PyTypeChecker
	def get(self, subframeNull=repcap.SubframeNull.Default, itemNull=repcap.ItemNull.Default) -> enums.V5GdCiCbSym:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:ENCC:XPDCch:EXTC:ITEM<CH0>:DCIConf:CBSYmbol \n
		Snippet: value: enums.V5GdCiCbSym = driver.source.bb.v5G.downlink.subf.encc.xpdcch.extc.item.dciConf.cbSymbol.get(subframeNull = repcap.SubframeNull.Default, itemNull = repcap.ItemNull.Default) \n
		Sets the DCI format field OFDM symbol index for CSI-RS / BRRS. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param itemNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Item')
			:return: dci_cb_symb_ind: S12| S13| S1213 13th symbol, 14th symbol, 13th and 14th symbol"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		itemNull_cmd_val = self._cmd_group.get_repcap_cmd_value(itemNull, repcap.ItemNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:ENCC:XPDCch:EXTC:ITEM{itemNull_cmd_val}:DCIConf:CBSYmbol?')
		return Conversions.str_to_scalar_enum(response, enums.V5GdCiCbSym)
