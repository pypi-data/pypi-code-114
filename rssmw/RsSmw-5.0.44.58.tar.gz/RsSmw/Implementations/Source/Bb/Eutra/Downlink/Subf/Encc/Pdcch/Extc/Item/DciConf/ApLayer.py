from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ApLayer:
	"""ApLayer commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("apLayer", core, parent)

	def set(self, ap_layer_id: int, subframeNull=repcap.SubframeNull.Default, itemNull=repcap.ItemNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PDCCh:EXTC:ITEM<CH0>:DCIConf:APLayer \n
		Snippet: driver.source.bb.eutra.downlink.subf.encc.pdcch.extc.item.dciConf.apLayer.set(ap_layer_id = 1, subframeNull = repcap.SubframeNull.Default, itemNull = repcap.ItemNull.Default) \n
		Sets the DCI Format 2C field antenna port(s) , layer, scrambling Id. Option: R&S SMW-K119: Value range <ApLayerId>
			Table Header: [:SOURce<hw>]:BB:EUTRa:DL:USER<ch>:CELL<st0>:DMRS:STATe / [:SOURce<hw>]:BB:EUTRa:DL:USER<ch>:CELL<st0>:SEOL:STATe / 1 codeword / 2 codewords \n
			- 0 / 0 / 0 to 6 / 0 to 7
			- 1 / 0 / 0 to 11 / 0 to 14
			- 1 / 1 / 0 to 1 / 0 to 1 \n
			:param ap_layer_id: integer Range: 0 to 7
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param itemNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Item')
		"""
		param = Conversions.decimal_value_to_str(ap_layer_id)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		itemNull_cmd_val = self._cmd_group.get_repcap_cmd_value(itemNull, repcap.ItemNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PDCCh:EXTC:ITEM{itemNull_cmd_val}:DCIConf:APLayer {param}')

	def get(self, subframeNull=repcap.SubframeNull.Default, itemNull=repcap.ItemNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PDCCh:EXTC:ITEM<CH0>:DCIConf:APLayer \n
		Snippet: value: int = driver.source.bb.eutra.downlink.subf.encc.pdcch.extc.item.dciConf.apLayer.get(subframeNull = repcap.SubframeNull.Default, itemNull = repcap.ItemNull.Default) \n
		Sets the DCI Format 2C field antenna port(s) , layer, scrambling Id. Option: R&S SMW-K119: Value range <ApLayerId>
			Table Header: [:SOURce<hw>]:BB:EUTRa:DL:USER<ch>:CELL<st0>:DMRS:STATe / [:SOURce<hw>]:BB:EUTRa:DL:USER<ch>:CELL<st0>:SEOL:STATe / 1 codeword / 2 codewords \n
			- 0 / 0 / 0 to 6 / 0 to 7
			- 1 / 0 / 0 to 11 / 0 to 14
			- 1 / 1 / 0 to 1 / 0 to 1 \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param itemNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Item')
			:return: ap_layer_id: integer Range: 0 to 7"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		itemNull_cmd_val = self._cmd_group.get_repcap_cmd_value(itemNull, repcap.ItemNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PDCCh:EXTC:ITEM{itemNull_cmd_val}:DCIConf:APLayer?')
		return Conversions.str_to_int(response)
