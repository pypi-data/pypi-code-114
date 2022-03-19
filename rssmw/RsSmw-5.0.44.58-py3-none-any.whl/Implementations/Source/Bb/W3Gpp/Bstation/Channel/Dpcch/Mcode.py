from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mcode:
	"""Mcode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcode", core, parent)

	def set(self, mcode: bool, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:DPCCh:MCODe \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.dpcch.mcode.set(mcode = False, baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		The command activates multicode transmission for the selected channel (ON) or deactivates it (OFF) . The multicode
		channels are destined for the same receiver, that is to say, are part of a radio link. The first channel of this group is
		used as the master channel. The common components (Pilot, TPC and TCFI) for all the channels are then spread using the
		spreading code of the master channel. \n
			:param mcode: 1| ON| 0| OFF
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.bool_to_str(mcode)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:DPCCh:MCODe {param}')

	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:DPCCh:MCODe \n
		Snippet: value: bool = driver.source.bb.w3Gpp.bstation.channel.dpcch.mcode.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		The command activates multicode transmission for the selected channel (ON) or deactivates it (OFF) . The multicode
		channels are destined for the same receiver, that is to say, are part of a radio link. The first channel of this group is
		used as the master channel. The common components (Pilot, TPC and TCFI) for all the channels are then spread using the
		spreading code of the master channel. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: mcode: 1| ON| 0| OFF"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:DPCCh:MCODe?')
		return Conversions.str_to_bool(response)
