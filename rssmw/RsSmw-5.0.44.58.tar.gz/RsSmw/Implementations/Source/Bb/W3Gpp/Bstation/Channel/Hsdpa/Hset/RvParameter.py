from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RvParameter:
	"""RvParameter commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Index, default value after init: Index.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rvParameter", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_index_get', 'repcap_index_set', repcap.Index.Nr1)

	def repcap_index_set(self, index: repcap.Index) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Index.Default
		Default value after init: Index.Nr1"""
		self._cmd_group.set_repcap_enum_value(index)

	def repcap_index_get(self) -> repcap.Index:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, rv_parameter: int, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default, index=repcap.Index.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:HSDPa:HSET:RVParameter<DI> \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.hsdpa.hset.rvParameter.set(rv_parameter = 1, baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default, index = repcap.Index.Default) \n
		The parameter is enabled for 'HARQ Simulation Mode' set to Constant ACK. The command sets the Redundancy Version
		Parameter. This value determines the processing of the Forward Error Correction and Constellation Arrangement (QAM16 and
		64QAM modulation) , see TS 25.212 4.6.2. For HS-SCCH Type 2 (less operation) , the Redundancy Version Parameter is always
		0. \n
			:param rv_parameter: integer Range: 0 to 7
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'RvParameter')
		"""
		param = Conversions.decimal_value_to_str(rv_parameter)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSDPa:HSET:RVParameter{index_cmd_val} {param}')

	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default, index=repcap.Index.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:HSDPa:HSET:RVParameter<DI> \n
		Snippet: value: int = driver.source.bb.w3Gpp.bstation.channel.hsdpa.hset.rvParameter.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default, index = repcap.Index.Default) \n
		The parameter is enabled for 'HARQ Simulation Mode' set to Constant ACK. The command sets the Redundancy Version
		Parameter. This value determines the processing of the Forward Error Correction and Constellation Arrangement (QAM16 and
		64QAM modulation) , see TS 25.212 4.6.2. For HS-SCCH Type 2 (less operation) , the Redundancy Version Parameter is always
		0. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'RvParameter')
			:return: rv_parameter: integer Range: 0 to 7"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSDPa:HSET:RVParameter{index_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'RvParameter':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RvParameter(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
