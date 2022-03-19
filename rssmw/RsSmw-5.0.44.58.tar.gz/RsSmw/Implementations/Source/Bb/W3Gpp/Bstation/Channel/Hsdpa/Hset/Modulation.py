from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modulation:
	"""Modulation commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: TwoStreams, default value after init: TwoStreams.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)
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

	def set(self, modulation: enums.ModulationC, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default, twoStreams=repcap.TwoStreams.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:HSDPa:HSET:MODulation<DI> \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.hsdpa.hset.modulation.set(modulation = enums.ModulationC.QAM16, baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default, twoStreams = repcap.TwoStreams.Default) \n
		Sets the modulation for stream 1 and stream 2 to QPSK, 16QAM or 64QAM. For HS-SCCH Type 2, the available modulation
		scheme is QPSK only. \n
			:param modulation: QPSK| QAM16| QAM64
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:param twoStreams: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Modulation')
		"""
		param = Conversions.enum_scalar_to_str(modulation, enums.ModulationC)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		twoStreams_cmd_val = self._cmd_group.get_repcap_cmd_value(twoStreams, repcap.TwoStreams)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSDPa:HSET:MODulation{twoStreams_cmd_val} {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default, twoStreams=repcap.TwoStreams.Default) -> enums.ModulationC:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:HSDPa:HSET:MODulation<DI> \n
		Snippet: value: enums.ModulationC = driver.source.bb.w3Gpp.bstation.channel.hsdpa.hset.modulation.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default, twoStreams = repcap.TwoStreams.Default) \n
		Sets the modulation for stream 1 and stream 2 to QPSK, 16QAM or 64QAM. For HS-SCCH Type 2, the available modulation
		scheme is QPSK only. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:param twoStreams: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Modulation')
			:return: modulation: QPSK| QAM16| QAM64"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		twoStreams_cmd_val = self._cmd_group.get_repcap_cmd_value(twoStreams, repcap.TwoStreams)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSDPa:HSET:MODulation{twoStreams_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.ModulationC)

	def clone(self) -> 'Modulation':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Modulation(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
