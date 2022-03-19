from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import enums
from ........... import repcap


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

	def set(self, data: enums.DataSourceA, channelNull=repcap.ChannelNull.Default, transportChannelNull=repcap.TransportChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:TCHannel<DI0>:DATA \n
		Snippet: driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.tchannel.data.set(data = enums.DataSourceA.DLISt, channelNull = repcap.ChannelNull.Default, transportChannelNull = repcap.TransportChannelNull.Default) \n
		The command determines the data source for the data fields of enhanced channels with channel coding. If channel coding is
		not active, the DPCH data source is used (SOURce:BB:W3GPp:BST:CHANnel:DATA) . \n
			:param data: PN9| PN11| PN15| PN16| PN20| PN21| PN23| DLISt| ZERO | ONE| PATTern| PNxx The pseudo-random sequence generator is used as the data source. Different random sequence lengths can be selected. DLISt A data list is used. The data list is selected with the command [:SOURcehw]:BB:W3GPp:BSTation:ENHanced:CHANnelch0:DPCH:TCHanneldi0:DATA:DSELect. ZERO | ONE Internal 0 and 1 data is used. PATTern Internal data is used. The bit pattern for the data is defined with the command [:SOURcehw]:BB:W3GPp:BSTation:ENHanced:CHANnelch0:DPCH:TCHanneldi0:DATA:PATTern.
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:param transportChannelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tchannel')
		"""
		param = Conversions.enum_scalar_to_str(data, enums.DataSourceA)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		transportChannelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transportChannelNull, repcap.TransportChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:TCHannel{transportChannelNull_cmd_val}:DATA {param}')

	# noinspection PyTypeChecker
	def get(self, channelNull=repcap.ChannelNull.Default, transportChannelNull=repcap.TransportChannelNull.Default) -> enums.DataSourceA:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation:ENHanced:CHANnel<CH0>:DPCH:TCHannel<DI0>:DATA \n
		Snippet: value: enums.DataSourceA = driver.source.bb.w3Gpp.bstation.enhanced.channel.dpch.tchannel.data.get(channelNull = repcap.ChannelNull.Default, transportChannelNull = repcap.TransportChannelNull.Default) \n
		The command determines the data source for the data fields of enhanced channels with channel coding. If channel coding is
		not active, the DPCH data source is used (SOURce:BB:W3GPp:BST:CHANnel:DATA) . \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:param transportChannelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Tchannel')
			:return: data: PN9| PN11| PN15| PN16| PN20| PN21| PN23| DLISt| ZERO | ONE| PATTern| PNxx The pseudo-random sequence generator is used as the data source. Different random sequence lengths can be selected. DLISt A data list is used. The data list is selected with the command [:SOURcehw]:BB:W3GPp:BSTation:ENHanced:CHANnelch0:DPCH:TCHanneldi0:DATA:DSELect. ZERO | ONE Internal 0 and 1 data is used. PATTern Internal data is used. The bit pattern for the data is defined with the command [:SOURcehw]:BB:W3GPp:BSTation:ENHanced:CHANnelch0:DPCH:TCHanneldi0:DATA:PATTern."""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		transportChannelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(transportChannelNull, repcap.TransportChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation:ENHanced:CHANnel{channelNull_cmd_val}:DPCH:TCHannel{transportChannelNull_cmd_val}:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.DataSourceA)

	def clone(self) -> 'Data':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Data(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
