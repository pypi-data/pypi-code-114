from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ccode:
	"""Ccode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ccode", core, parent)

	def get(self, mobileStation=repcap.MobileStation.Default, channel=repcap.Channel.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:CHANnel<CH>:DPDCh:E:CCODe \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.hsupa.channel.dpdch.e.ccode.get(mobileStation = repcap.MobileStation.Default, channel = repcap.Channel.Default) \n
		Queries the channelization code and the modulation branch (I or Q) of the E-DPDCH channel. The channelization code is
		dependent on the overall symbol rate set and cannot be modified. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Channel')
			:return: channel_code: integer"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:CHANnel{channel_cmd_val}:DPDCh:E:CCODe?')
		return Conversions.str_to_int(response)
