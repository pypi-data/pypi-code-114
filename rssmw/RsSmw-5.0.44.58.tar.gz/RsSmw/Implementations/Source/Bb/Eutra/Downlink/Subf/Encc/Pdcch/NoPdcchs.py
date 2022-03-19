from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NoPdcchs:
	"""NoPdcchs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("noPdcchs", core, parent)

	def set(self, pdcch_count: int, subframeNull=repcap.SubframeNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PDCCh:NOPDcchs \n
		Snippet: driver.source.bb.eutra.downlink.subf.encc.pdcch.noPdcchs.set(pdcch_count = 1, subframeNull = repcap.SubframeNull.Default) \n
		Sets the number of PDCCHs to be transmitted. \n
			:param pdcch_count: integer Range: 0 to dynamic
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
		"""
		param = Conversions.decimal_value_to_str(pdcch_count)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PDCCh:NOPDcchs {param}')

	def get(self, subframeNull=repcap.SubframeNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PDCCh:NOPDcchs \n
		Snippet: value: int = driver.source.bb.eutra.downlink.subf.encc.pdcch.noPdcchs.get(subframeNull = repcap.SubframeNull.Default) \n
		Sets the number of PDCCHs to be transmitted. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:return: pdcch_count: integer Range: 0 to dynamic"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PDCCh:NOPDcchs?')
		return Conversions.str_to_int(response)
