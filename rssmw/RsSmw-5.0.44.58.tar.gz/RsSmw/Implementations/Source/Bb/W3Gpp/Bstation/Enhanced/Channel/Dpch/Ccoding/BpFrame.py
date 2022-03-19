from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BpFrame:
	"""BpFrame commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bpFrame", core, parent)

	def get(self, channelNull=repcap.ChannelNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:CCODing:BPFRame \n
		Snippet: value: int = driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.ccoding.bpFrame.get(channelNull = repcap.ChannelNull.Default) \n
		Queries the number of data bits in the DPDCH component of the frame at the physical layer. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: bp_frame: integer Range: 30 to 20000"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:CCODing:BPFRame?')
		return Conversions.str_to_int(response)
