from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cvpb:
	"""Cvpb commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: TwoStreams, default value after init: TwoStreams.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cvpb", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_twoStreams_get', 'repcap_twoStreams_set', repcap.TwoStreams.Nr1)

	def repcap_twoStreams_set(self, twoStreams: repcap.TwoStreams) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to TwoStreams.Default
		Default value after init: TwoStreams.Nr1"""
		self._cmd_group.set_repcap_enum_value(twoStreams)

	def repcap_twoStreams_get(self) -> repcap.TwoStreams:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, cvpb: int, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default, twoStreams=repcap.TwoStreams.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:HSDPa:MIMO:CVPB<DI> \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.hsdpa.mimo.cvpb.set(cvpb = 1, baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default, twoStreams = repcap.TwoStreams.Default) \n
		The command switches the order of the constellation points of the 16QAM and 64QAM mapping. The re-arrengement is done
		according to 3GPP TS25.212. \n
			:param cvpb: 0 | 1 | 2 | 3 Range: 0 to 3
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:param twoStreams: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cvpb')
		"""
		param = Conversions.decimal_value_to_str(cvpb)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		twoStreams_cmd_val = self._cmd_group.get_repcap_cmd_value(twoStreams, repcap.TwoStreams)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSDPa:MIMO:CVPB{twoStreams_cmd_val} {param}')

	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default, twoStreams=repcap.TwoStreams.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:HSDPa:MIMO:CVPB<DI> \n
		Snippet: value: int = driver.source.bb.w3Gpp.bstation.channel.hsdpa.mimo.cvpb.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default, twoStreams = repcap.TwoStreams.Default) \n
		The command switches the order of the constellation points of the 16QAM and 64QAM mapping. The re-arrengement is done
		according to 3GPP TS25.212. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:param twoStreams: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cvpb')
			:return: cvpb: 0 | 1 | 2 | 3 Range: 0 to 3"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		twoStreams_cmd_val = self._cmd_group.get_repcap_cmd_value(twoStreams, repcap.TwoStreams)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSDPa:MIMO:CVPB{twoStreams_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Cvpb':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cvpb(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
