from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rate:
	"""Rate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rate", core, parent)

	def set(self, rate: enums.WlannFbCodRate, frameBlock=repcap.FrameBlock.Default, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:[USER<DI>]:CODing:RATE \n
		Snippet: driver.source.bb.wlnn.fblock.user.coding.rate.set(rate = enums.WlannFbCodRate.CR1D2, frameBlock = repcap.FrameBlock.Default, userIx = repcap.UserIx.Default) \n
		This command selects the coding rate. \n
			:param rate: CR1D2| CR2D3| CR3D4| CR5D6
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(rate, enums.WlannFbCodRate)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:USER{userIx_cmd_val}:CODing:RATE {param}')

	# noinspection PyTypeChecker
	def get(self, frameBlock=repcap.FrameBlock.Default, userIx=repcap.UserIx.Default) -> enums.WlannFbCodRate:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:[USER<DI>]:CODing:RATE \n
		Snippet: value: enums.WlannFbCodRate = driver.source.bb.wlnn.fblock.user.coding.rate.get(frameBlock = repcap.FrameBlock.Default, userIx = repcap.UserIx.Default) \n
		This command selects the coding rate. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: rate: CR1D2| CR2D3| CR3D4| CR5D6"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:USER{userIx_cmd_val}:CODing:RATE?')
		return Conversions.str_to_scalar_enum(response, enums.WlannFbCodRate)
