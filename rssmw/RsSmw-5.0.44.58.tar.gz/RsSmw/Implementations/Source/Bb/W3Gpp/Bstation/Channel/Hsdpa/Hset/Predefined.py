from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Predefined:
	"""Predefined commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("predefined", core, parent)

	def set(self, predefined: enums.HsHsetType, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:HSDPa:HSET:PREDefined \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.hsdpa.hset.predefined.set(predefined = enums.HsHsetType.P10QAM16, baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		The command selects the H-Set and the modulation according to TS 25.101 Annex A.7. \n
			:param predefined: P1QPSK| P1QAM16| P2QPSK| P2QAM16| P3QPSK| P3QAM16| P4QPSK| P5QPSK| P6QPSK| P6QAM16| P7QPSK| P8QAM64| P9QAM16QPSK| P10QPSK| P10QAM16| P11QAM64QAM16| P12QPSK| USER
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.enum_scalar_to_str(predefined, enums.HsHsetType)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSDPa:HSET:PREDefined {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> enums.HsHsetType:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:HSDPa:HSET:PREDefined \n
		Snippet: value: enums.HsHsetType = driver.source.bb.w3Gpp.bstation.channel.hsdpa.hset.predefined.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		The command selects the H-Set and the modulation according to TS 25.101 Annex A.7. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: predefined: P1QPSK| P1QAM16| P2QPSK| P2QAM16| P3QPSK| P3QAM16| P4QPSK| P5QPSK| P6QPSK| P6QAM16| P7QPSK| P8QAM64| P9QAM16QPSK| P10QPSK| P10QAM16| P11QAM64QAM16| P12QPSK| USER"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSDPa:HSET:PREDefined?')
		return Conversions.str_to_scalar_enum(response, enums.HsHsetType)
