from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RuType:
	"""RuType commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ruType", core, parent)

	def set(self, ru_type: enums.WlannFbPpduUserRuType, frameBlock=repcap.FrameBlock.Default, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:USER<DI>:RUTYpe \n
		Snippet: driver.source.bb.wlnn.fblock.user.ruType.set(ru_type = enums.WlannFbPpduUserRuType.RU106, frameBlock = repcap.FrameBlock.Default, userIx = repcap.UserIx.Default) \n
		Queries the resource unit type for the current user. \n
			:param ru_type: RU26| RU52| RU106| RU242| RU484| RU996| RU2996| RUC26| RU4996| RU484_242| RU996_484| RU996_484_242| RU2996_484| RU3996| RU3996_484 RU26|RU52|RU106|RU242|RU484|RU996|RU2996|RUC26 Require WLAN standard IEEE 802.11ax or IEEE 802.11be: SOURce1:BB:WLNN:FBLock1:STANdard WAX RU26|RU52|RU106|RU242|RU484|RU996|RU2996|RUC26| RU4996|RU484_242|RU996_484|RU996_484_242| RU2996_484|RU3996|RU3996_484 Require WLAN standard IEEE 802.11be: SOURce1:BB:WLNN:FBLock1:STANdard WBE
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(ru_type, enums.WlannFbPpduUserRuType)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:USER{userIx_cmd_val}:RUTYpe {param}')

	# noinspection PyTypeChecker
	def get(self, frameBlock=repcap.FrameBlock.Default, userIx=repcap.UserIx.Default) -> enums.WlannFbPpduUserRuType:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:USER<DI>:RUTYpe \n
		Snippet: value: enums.WlannFbPpduUserRuType = driver.source.bb.wlnn.fblock.user.ruType.get(frameBlock = repcap.FrameBlock.Default, userIx = repcap.UserIx.Default) \n
		Queries the resource unit type for the current user. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: ru_type: RU26| RU52| RU106| RU242| RU484| RU996| RU2996| RUC26| RU4996| RU484_242| RU996_484| RU996_484_242| RU2996_484| RU3996| RU3996_484 RU26|RU52|RU106|RU242|RU484|RU996|RU2996|RUC26 Require WLAN standard IEEE 802.11ax or IEEE 802.11be: SOURce1:BB:WLNN:FBLock1:STANdard WAX RU26|RU52|RU106|RU242|RU484|RU996|RU2996|RUC26| RU4996|RU484_242|RU996_484|RU996_484_242| RU2996_484|RU3996|RU3996_484 Require WLAN standard IEEE 802.11be: SOURce1:BB:WLNN:FBLock1:STANdard WBE"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:USER{userIx_cmd_val}:RUTYpe?')
		return Conversions.str_to_scalar_enum(response, enums.WlannFbPpduUserRuType)
