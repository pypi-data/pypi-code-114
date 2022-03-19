from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def get(self, channelNull=repcap.ChannelNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:DPControl:[POWer] \n
		Snippet: value: float = driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.dpControl.power.get(channelNull = repcap.ChannelNull.Default) \n
		The command queries the deviation of the channel power (delta POW) from the set power start value of the corresponding
		enhanced channels. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: power: float Range: -60 to 60"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:DPControl:POWer?')
		return Conversions.str_to_float(response)
