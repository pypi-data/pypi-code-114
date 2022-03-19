from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def set(self, level: enums.GsmBursPowMode, frameIx=repcap.FrameIx.Default, slotNull=repcap.SlotNull.Default, subchannel=repcap.Subchannel.Default, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:[FRAMe<DI>]:SLOT<ST0>:[SUBChannel<US>]:[USER<CH>]:LEVel \n
		Snippet: driver.source.bb.gsm.frame.slot.subChannel.user.level.set(level = enums.GsmBursPowMode.ATT, frameIx = repcap.FrameIx.Default, slotNull = repcap.SlotNull.Default, subchannel = repcap.Subchannel.Default, userIx = repcap.UserIx.Default) \n
		The command defines the power control level of the selected slot. \n
			:param level: OFF| ATT| FULL OFF The slot is inactive. ATT The power is reduced by the amount defined using :BB:GSM:SLOT:ATT. FULL Full power as specified by the level setting.
			:param frameIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param subchannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'SubChannel')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(level, enums.GsmBursPowMode)
		frameIx_cmd_val = self._cmd_group.get_repcap_cmd_value(frameIx, repcap.FrameIx)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		subchannel_cmd_val = self._cmd_group.get_repcap_cmd_value(subchannel, repcap.Subchannel)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:FRAMe{frameIx_cmd_val}:SLOT{slotNull_cmd_val}:SUBChannel{subchannel_cmd_val}:USER{userIx_cmd_val}:LEVel {param}')

	# noinspection PyTypeChecker
	def get(self, frameIx=repcap.FrameIx.Default, slotNull=repcap.SlotNull.Default, subchannel=repcap.Subchannel.Default, userIx=repcap.UserIx.Default) -> enums.GsmBursPowMode:
		"""SCPI: [SOURce<HW>]:BB:GSM:[FRAMe<DI>]:SLOT<ST0>:[SUBChannel<US>]:[USER<CH>]:LEVel \n
		Snippet: value: enums.GsmBursPowMode = driver.source.bb.gsm.frame.slot.subChannel.user.level.get(frameIx = repcap.FrameIx.Default, slotNull = repcap.SlotNull.Default, subchannel = repcap.Subchannel.Default, userIx = repcap.UserIx.Default) \n
		The command defines the power control level of the selected slot. \n
			:param frameIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param slotNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param subchannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'SubChannel')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: level: OFF| ATT| FULL OFF The slot is inactive. ATT The power is reduced by the amount defined using :BB:GSM:SLOT:ATT. FULL Full power as specified by the level setting."""
		frameIx_cmd_val = self._cmd_group.get_repcap_cmd_value(frameIx, repcap.FrameIx)
		slotNull_cmd_val = self._cmd_group.get_repcap_cmd_value(slotNull, repcap.SlotNull)
		subchannel_cmd_val = self._cmd_group.get_repcap_cmd_value(subchannel, repcap.Subchannel)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GSM:FRAMe{frameIx_cmd_val}:SLOT{slotNull_cmd_val}:SUBChannel{subchannel_cmd_val}:USER{userIx_cmd_val}:LEVel?')
		return Conversions.str_to_scalar_enum(response, enums.GsmBursPowMode)
