from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import enums
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PdcchType:
	"""PdcchType commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdcchType", core, parent)

	def set(self, pdcch_type: enums.EutraPdcchType, subframeNull=repcap.SubframeNull.Default, itemNull=repcap.ItemNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PDCCh:EXTC:ITEM<CH0>:PDCChtype \n
		Snippet: driver.source.bb.eutra.downlink.subf.encc.pdcch.extc.item.pdcchType.set(pdcch_type = enums.EutraPdcchType.EPD1, subframeNull = repcap.SubframeNull.Default, itemNull = repcap.ItemNull.Default) \n
		Sets if the DCI is carried by a PDCCH or by an EPDCCH set. \n
			:param pdcch_type: PDCCh| EPD1| EPD2 EPD1|EPD2 EPDCCH sets cannot be allocated TDD special subframes, if the combinations listed in Table 'Combinations of cyclic prefix and TDD special subframe configurations' apply.
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param itemNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Item')
		"""
		param = Conversions.enum_scalar_to_str(pdcch_type, enums.EutraPdcchType)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		itemNull_cmd_val = self._cmd_group.get_repcap_cmd_value(itemNull, repcap.ItemNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PDCCh:EXTC:ITEM{itemNull_cmd_val}:PDCChtype {param}')

	# noinspection PyTypeChecker
	def get(self, subframeNull=repcap.SubframeNull.Default, itemNull=repcap.ItemNull.Default) -> enums.EutraPdcchType:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PDCCh:EXTC:ITEM<CH0>:PDCChtype \n
		Snippet: value: enums.EutraPdcchType = driver.source.bb.eutra.downlink.subf.encc.pdcch.extc.item.pdcchType.get(subframeNull = repcap.SubframeNull.Default, itemNull = repcap.ItemNull.Default) \n
		Sets if the DCI is carried by a PDCCH or by an EPDCCH set. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param itemNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Item')
			:return: pdcch_type: PDCCh| EPD1| EPD2 EPD1|EPD2 EPDCCH sets cannot be allocated TDD special subframes, if the combinations listed in Table 'Combinations of cyclic prefix and TDD special subframe configurations' apply."""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		itemNull_cmd_val = self._cmd_group.get_repcap_cmd_value(itemNull, repcap.ItemNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PDCCh:EXTC:ITEM{itemNull_cmd_val}:PDCChtype?')
		return Conversions.str_to_scalar_enum(response, enums.EutraPdcchType)
