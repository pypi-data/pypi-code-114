from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	@property
	def dselect(self):
		"""dselect commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dselect'):
			from .Dselect import Dselect
			self._dselect = Dselect(self._core, self._cmd_group)
		return self._dselect

	@property
	def pattern(self):
		"""pattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pattern'):
			from .Pattern import Pattern
			self._pattern = Pattern(self._core, self._cmd_group)
		return self._pattern

	def set(self, data: enums.TpcDataSour, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:DPCCh:TPC:DATA \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.dpcch.tpc.data.set(data = enums.TpcDataSour.DLISt, baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		Determines the data source for the TPC field of the channel. \n
			:param data: ZERO| ONE| PATTern| DLISt DLISt A data list is used. Use the command [:SOURcehw]:BB:W3GPp:BSTationst:CHANnelch0:DPCCh:TPC:DATA:DSELect to define the data list file. ZERO | ONE Internal 0 and 1 data is used. PATTern Internal data is used. Use the command [:SOURcehw]:BB:W3GPp:BSTationst:CHANnelch0:DPCCh:TPC:DATA:PATTern to define the bit pattern.
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.enum_scalar_to_str(data, enums.TpcDataSour)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:DPCCh:TPC:DATA {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> enums.TpcDataSour:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:DPCCh:TPC:DATA \n
		Snippet: value: enums.TpcDataSour = driver.source.bb.w3Gpp.bstation.channel.dpcch.tpc.data.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		Determines the data source for the TPC field of the channel. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: data: ZERO| ONE| PATTern| DLISt DLISt A data list is used. Use the command [:SOURcehw]:BB:W3GPp:BSTationst:CHANnelch0:DPCCh:TPC:DATA:DSELect to define the data list file. ZERO | ONE Internal 0 and 1 data is used. PATTern Internal data is used. Use the command [:SOURcehw]:BB:W3GPp:BSTationst:CHANnelch0:DPCCh:TPC:DATA:PATTern to define the bit pattern."""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:DPCCh:TPC:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.TpcDataSour)

	def clone(self) -> 'Data':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Data(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
