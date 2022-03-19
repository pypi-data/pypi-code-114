from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import enums
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Xpend:
	"""Xpend commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("xpend", core, parent)

	def set(self, dci_xpdsch_end: enums.V5GdCiXpdscheNd, subframeNull=repcap.SubframeNull.Default, itemNull=repcap.ItemNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:ENCC:XPDCch:EXTC:ITEM<CH0>:DCIConf:XPENd \n
		Snippet: driver.source.bb.v5G.downlink.subf.encc.xpdcch.extc.item.dciConf.xpend.set(dci_xpdsch_end = enums.V5GdCiXpdscheNd.S11, subframeNull = repcap.SubframeNull.Default, itemNull = repcap.ItemNull.Default) \n
		Sets the DCI format field end. \n
			:param dci_xpdsch_end: S11| S13 12th, 14th symbol
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param itemNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Item')
		"""
		param = Conversions.enum_scalar_to_str(dci_xpdsch_end, enums.V5GdCiXpdscheNd)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		itemNull_cmd_val = self._cmd_group.get_repcap_cmd_value(itemNull, repcap.ItemNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:ENCC:XPDCch:EXTC:ITEM{itemNull_cmd_val}:DCIConf:XPENd {param}')

	# noinspection PyTypeChecker
	def get(self, subframeNull=repcap.SubframeNull.Default, itemNull=repcap.ItemNull.Default) -> enums.V5GdCiXpdscheNd:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:ENCC:XPDCch:EXTC:ITEM<CH0>:DCIConf:XPENd \n
		Snippet: value: enums.V5GdCiXpdscheNd = driver.source.bb.v5G.downlink.subf.encc.xpdcch.extc.item.dciConf.xpend.get(subframeNull = repcap.SubframeNull.Default, itemNull = repcap.ItemNull.Default) \n
		Sets the DCI format field end. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param itemNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Item')
			:return: dci_xpdsch_end: S11| S13 12th, 14th symbol"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		itemNull_cmd_val = self._cmd_group.get_repcap_cmd_value(itemNull, repcap.ItemNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:ENCC:XPDCch:EXTC:ITEM{itemNull_cmd_val}:DCIConf:XPENd?')
		return Conversions.str_to_scalar_enum(response, enums.V5GdCiXpdscheNd)
