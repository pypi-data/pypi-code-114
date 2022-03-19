from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ccode:
	"""Ccode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ccode", core, parent)

	def get(self, mobileStation=repcap.MobileStation.Default, channel=repcap.Channel.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:CHANnel<CH>:DPDCh:CCODe \n
		Snippet: value: float = driver.source.bb.w3Gpp.mstation.channel.dpdch.ccode.get(mobileStation = repcap.MobileStation.Default, channel = repcap.Channel.Default) \n
		The command queries the channelization code of the specified channel. The value is fixed and depends on the overall
		symbol rate of the user equipment. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Channel')
			:return: ccode: float"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:CHANnel{channel_cmd_val}:DPDCh:CCODe?')
		return Conversions.str_to_float(response)
