from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nsts:
	"""Nsts commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nsts", core, parent)

	def set(self, user_nsts: int, frameBlock=repcap.FrameBlock.Default, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:USER<DI>:NSTS \n
		Snippet: driver.source.bb.wlnn.fblock.user.nsts.set(user_nsts = 1, frameBlock = repcap.FrameBlock.Default, userIx = repcap.UserIx.Default) \n
		Sets the number of spatial streams, the number of space time streams minus 1. \n
			:param user_nsts: integer Range: 1 to 8
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.decimal_value_to_str(user_nsts)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:USER{userIx_cmd_val}:NSTS {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default, userIx=repcap.UserIx.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:USER<DI>:NSTS \n
		Snippet: value: int = driver.source.bb.wlnn.fblock.user.nsts.get(frameBlock = repcap.FrameBlock.Default, userIx = repcap.UserIx.Default) \n
		Sets the number of spatial streams, the number of space time streams minus 1. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: user_nsts: integer Range: 1 to 8"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:USER{userIx_cmd_val}:NSTS?')
		return Conversions.str_to_int(response)
