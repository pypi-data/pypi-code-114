from .............Internal.Core import Core
from .............Internal.CommandsGroup import CommandsGroup
from .............Internal import Conversions
from ............. import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Valid:
	"""Valid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("valid", core, parent)

	def get(self, subframeNull=repcap.SubframeNull.Default, itemNull=repcap.ItemNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:[SUBF<ST0>]:ENCC:PDCCh:EXTC:ITEM<CH0>:SESPace:CHK:VALid \n
		Snippet: value: bool = driver.source.bb.oneweb.downlink.subf.encc.pdcch.extc.item.sespace.chk.valid.get(subframeNull = repcap.SubframeNull.Default, itemNull = repcap.ItemNull.Default) \n
		No command help available \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param itemNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Item')
			:return: valid: No help available"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		itemNull_cmd_val = self._cmd_group.get_repcap_cmd_value(itemNull, repcap.ItemNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:DL:SUBF{subframeNull_cmd_val}:ENCC:PDCCh:EXTC:ITEM{itemNull_cmd_val}:SESPace:CHK:VALid?')
		return Conversions.str_to_bool(response)
