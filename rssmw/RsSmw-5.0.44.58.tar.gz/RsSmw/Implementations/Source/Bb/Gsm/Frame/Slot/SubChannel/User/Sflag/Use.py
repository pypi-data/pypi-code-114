from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Use:
	"""Use commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("use", core, parent)

	def set(self, use: bool, frameIx=repcap.FrameIx.Default, slotNull=repcap.SlotNull.Default, subchannel=repcap.Subchannel.Default, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:[FRAMe<DI>]:SLOT<ST0>:[SUBChannel<US>]:[USER<CH>]:SFLag:USE \n
		Snippet: driver.source.bb.gsm.frame.slot.subChannel.user.sflag.use.set(use = False, frameIx = repcap.FrameIx.Default, slotNull = repcap.SlotNull.Default, subchannel = repcap.Subchannel.Default, userIx = repcap.UserIx.Default) \n
		The command enables or disables the use of Stealing Flags. If not used, the Stealing Flags bits are allocated to the DATA
		fields (only for Normal burst BB:GSM:SLOT:TYPE NORM) . \n
			:param use: 1| ON| 0| OFF
			:param frameIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param subchannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'SubChannel')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.bool_to_str(use)
		frameIx_cmd_val = self._cmd_group.get_repcap_cmd_value(frameIx, repcap.FrameIx)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		subchannel_cmd_val = self._cmd_group.get_repcap_cmd_value(subchannel, repcap.Subchannel)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:FRAMe{frameIx_cmd_val}:SLOT{slotNull_cmd_val}:SUBChannel{subchannel_cmd_val}:USER{userIx_cmd_val}:SFLag:USE {param}')

	def get(self, frameIx=repcap.FrameIx.Default, slotNull=repcap.SlotNull.Default, subchannel=repcap.Subchannel.Default, userIx=repcap.UserIx.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GSM:[FRAMe<DI>]:SLOT<ST0>:[SUBChannel<US>]:[USER<CH>]:SFLag:USE \n
		Snippet: value: bool = driver.source.bb.gsm.frame.slot.subChannel.user.sflag.use.get(frameIx = repcap.FrameIx.Default, slotNull = repcap.SlotNull.Default, subchannel = repcap.Subchannel.Default, userIx = repcap.UserIx.Default) \n
		The command enables or disables the use of Stealing Flags. If not used, the Stealing Flags bits are allocated to the DATA
		fields (only for Normal burst BB:GSM:SLOT:TYPE NORM) . \n
			:param frameIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param subchannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'SubChannel')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: use: 1| ON| 0| OFF"""
		frameIx_cmd_val = self._cmd_group.get_repcap_cmd_value(frameIx, repcap.FrameIx)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		subchannel_cmd_val = self._cmd_group.get_repcap_cmd_value(subchannel, repcap.Subchannel)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GSM:FRAMe{frameIx_cmd_val}:SLOT{slotNull_cmd_val}:SUBChannel{subchannel_cmd_val}:USER{userIx_cmd_val}:SFLag:USE?')
		return Conversions.str_to_bool(response)
