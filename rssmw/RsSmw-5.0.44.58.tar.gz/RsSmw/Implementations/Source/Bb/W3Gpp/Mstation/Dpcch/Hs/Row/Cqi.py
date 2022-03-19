from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cqi:
	"""Cqi commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: ChannelQualId, default value after init: ChannelQualId.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cqi", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_channelQualId_get', 'repcap_channelQualId_set', repcap.ChannelQualId.Nr1)

	def repcap_channelQualId_set(self, channelQualId: repcap.ChannelQualId) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to ChannelQualId.Default
		Default value after init: ChannelQualId.Nr1"""
		self._cmd_group.set_repcap_enum_value(channelQualId)

	def repcap_channelQualId_get(self) -> repcap.ChannelQualId:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, cqi: int, mobileStation=repcap.MobileStation.Default, rowNull=repcap.RowNull.Default, channelQualId=repcap.ChannelQualId.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:ROW<CH0>:CQI<DI> \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.hs.row.cqi.set(cqi = 1, mobileStation = repcap.MobileStation.Default, rowNull = repcap.RowNull.Default, channelQualId = repcap.ChannelQualId.Default) \n
		No command help available \n
			:param cqi: No help available
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
			:param channelQualId: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cqi')
		"""
		param = Conversions.decimal_value_to_str(cqi)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		channelQualId_cmd_val = self._cmd_group.get_repcap_cmd_value(channelQualId, repcap.ChannelQualId)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:ROW{rowNull_cmd_val}:CQI{channelQualId_cmd_val} {param}')

	def get(self, mobileStation=repcap.MobileStation.Default, rowNull=repcap.RowNull.Default, channelQualId=repcap.ChannelQualId.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:ROW<CH0>:CQI<DI> \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.dpcch.hs.row.cqi.get(mobileStation = repcap.MobileStation.Default, rowNull = repcap.RowNull.Default, channelQualId = repcap.ChannelQualId.Default) \n
		No command help available \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
			:param channelQualId: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cqi')
			:return: cqi: No help available"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		channelQualId_cmd_val = self._cmd_group.get_repcap_cmd_value(channelQualId, repcap.ChannelQualId)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:ROW{rowNull_cmd_val}:CQI{channelQualId_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Cqi':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cqi(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
