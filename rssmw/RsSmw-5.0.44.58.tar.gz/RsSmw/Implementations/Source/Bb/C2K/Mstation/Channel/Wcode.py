from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Wcode:
	"""Wcode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wcode", core, parent)

	def get(self, mobileStation=repcap.MobileStation.Default, channel=repcap.Channel.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:C2K:MSTation<ST>:CHANnel<CH>:WCODe \n
		Snippet: value: int = driver.source.bb.c2K.mstation.channel.wcode.get(mobileStation = repcap.MobileStation.Default, channel = repcap.Channel.Default) \n
		Queries the Walsh code. The standard assigns a fixed walsh code to some channels. For the traffic channels, this value is
		specific for the selected radio configuration. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Channel')
			:return: wcode: integer Range: 0 to 255"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:MSTation{mobileStation_cmd_val}:CHANnel{channel_cmd_val}:WCODe?')
		return Conversions.str_to_int(response)
