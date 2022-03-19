from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import enums
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 4 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	@property
	def dlist(self):
		"""dlist commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_dlist'):
			from .Dlist import Dlist
			self._dlist = Dlist(self._core, self._cmd_group)
		return self._dlist

	@property
	def pattern(self):
		"""pattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pattern'):
			from .Pattern import Pattern
			self._pattern = Pattern(self._core, self._cmd_group)
		return self._pattern

	def set(self, data: enums.GsmBursDataSour, frameIx=repcap.FrameIx.Default, slotNull=repcap.SlotNull.Default, subchannel=repcap.Subchannel.Default, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:[FRAMe<DI>]:SLOT<ST0>:[SUBChannel<US>]:[USER<CH>]:[SOURce]:DATA \n
		Snippet: driver.source.bb.gsm.frame.slot.subChannel.user.source.data.set(data = enums.GsmBursDataSour.ALL0, frameIx = repcap.FrameIx.Default, slotNull = repcap.SlotNull.Default, subchannel = repcap.Subchannel.Default, userIx = repcap.UserIx.Default) \n
		The command defines the data source for the DATA fields in the burst. This command is valid only when burst types that
		contain data fields are selected. If a burst contains multiple DATA fields, these are treated as a continuous field. For
		instance, data such as a pseudo-random sequence is continued without interruption from one DATA field to the next.
		In 'GSM Mode Unframed', this command defines the data source for the unframed signal. The suffix in SLOT has to be set to
		0 (BB:GSM:SLOT0:DATA) . \n
			:param data: ALL0| ALL1| PATTern| PN9| PN11| PN15| PN16| PN20| PN21| PN23| DLISt PNxx The pseudo-random sequence generator is used as the data source. There is a choice of different lengths of random sequence. DLISt A data list is used. The data list is selected with the aid of command SOURce:BB:GSM:SLOT:DATA:DLISt. ALL0 | ALL1 Internal 0 or 1 data is used. PATTern Internal data is used. The bit pattern for the data is defined with the aid of command :SOURce:BB:GSM:SLOT:DATA:PATTern.
			:param frameIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param subchannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'SubChannel')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(data, enums.GsmBursDataSour)
		frameIx_cmd_val = self._cmd_group.get_repcap_cmd_value(frameIx, repcap.FrameIx)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		subchannel_cmd_val = self._cmd_group.get_repcap_cmd_value(subchannel, repcap.Subchannel)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:FRAMe{frameIx_cmd_val}:SLOT{slotNull_cmd_val}:SUBChannel{subchannel_cmd_val}:USER{userIx_cmd_val}:SOURce:DATA {param}')

	# noinspection PyTypeChecker
	def get(self, frameIx=repcap.FrameIx.Default, slotNull=repcap.SlotNull.Default, subchannel=repcap.Subchannel.Default, userIx=repcap.UserIx.Default) -> enums.GsmBursDataSour:
		"""SCPI: [SOURce<HW>]:BB:GSM:[FRAMe<DI>]:SLOT<ST0>:[SUBChannel<US>]:[USER<CH>]:[SOURce]:DATA \n
		Snippet: value: enums.GsmBursDataSour = driver.source.bb.gsm.frame.slot.subChannel.user.source.data.get(frameIx = repcap.FrameIx.Default, slotNull = repcap.SlotNull.Default, subchannel = repcap.Subchannel.Default, userIx = repcap.UserIx.Default) \n
		The command defines the data source for the DATA fields in the burst. This command is valid only when burst types that
		contain data fields are selected. If a burst contains multiple DATA fields, these are treated as a continuous field. For
		instance, data such as a pseudo-random sequence is continued without interruption from one DATA field to the next.
		In 'GSM Mode Unframed', this command defines the data source for the unframed signal. The suffix in SLOT has to be set to
		0 (BB:GSM:SLOT0:DATA) . \n
			:param frameIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param subchannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'SubChannel')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: data: ALL0| ALL1| PATTern| PN9| PN11| PN15| PN16| PN20| PN21| PN23| DLISt PNxx The pseudo-random sequence generator is used as the data source. There is a choice of different lengths of random sequence. DLISt A data list is used. The data list is selected with the aid of command SOURce:BB:GSM:SLOT:DATA:DLISt. ALL0 | ALL1 Internal 0 or 1 data is used. PATTern Internal data is used. The bit pattern for the data is defined with the aid of command :SOURce:BB:GSM:SLOT:DATA:PATTern."""
		frameIx_cmd_val = self._cmd_group.get_repcap_cmd_value(frameIx, repcap.FrameIx)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		subchannel_cmd_val = self._cmd_group.get_repcap_cmd_value(subchannel, repcap.Subchannel)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GSM:FRAMe{frameIx_cmd_val}:SLOT{slotNull_cmd_val}:SUBChannel{subchannel_cmd_val}:USER{userIx_cmd_val}:SOURce:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.GsmBursDataSour)

	def clone(self) -> 'Data':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Data(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
