from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scpir:
	"""Scpir commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: ChannelNull, default value after init: ChannelNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scpir", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_channelNull_get', 'repcap_channelNull_set', repcap.ChannelNull.Nr0)

	def repcap_channelNull_set(self, channelNull: repcap.ChannelNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to ChannelNull.Default
		Default value after init: ChannelNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(channelNull)

	def repcap_channelNull_get(self) -> repcap.ChannelNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, scpir: float, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:AQPSk:SCPIR<CH0> \n
		Snippet: driver.source.bb.gsm.aqPsk.scpir.set(scpir = 1.0, channelNull = repcap.ChannelNull.Default) \n
		Sets the Subchannel Power Imbalance Ratio (SCPIR) . It is related to the angle α as follows: SCPIR = 20 * log10(tan α) dB,
		where the value of α is chosen such that |SCPIR|≤10dB. \n
			:param scpir: float Range: -115.1625 to 115.1625
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Scpir')
		"""
		param = Conversions.decimal_value_to_str(scpir)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:AQPSk:SCPIR{channelNull_cmd_val} {param}')

	def get(self, channelNull=repcap.ChannelNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GSM:AQPSk:SCPIR<CH0> \n
		Snippet: value: float = driver.source.bb.gsm.aqPsk.scpir.get(channelNull = repcap.ChannelNull.Default) \n
		Sets the Subchannel Power Imbalance Ratio (SCPIR) . It is related to the angle α as follows: SCPIR = 20 * log10(tan α) dB,
		where the value of α is chosen such that |SCPIR|≤10dB. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Scpir')
			:return: scpir: float Range: -115.1625 to 115.1625"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GSM:AQPSk:SCPIR{channelNull_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Scpir':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scpir(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
