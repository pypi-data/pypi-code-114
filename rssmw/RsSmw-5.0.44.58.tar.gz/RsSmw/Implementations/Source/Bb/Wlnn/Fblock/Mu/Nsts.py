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

	def set(self, no_of_sts: int, frameBlock=repcap.FrameBlock.Default, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:MU<ST0>:NSTS \n
		Snippet: driver.source.bb.wlnn.fblock.mu.nsts.set(no_of_sts = 1, frameBlock = repcap.FrameBlock.Default, userIx = repcap.UserIx.Default) \n
		Sets the number of space time streams for each user. \n
			:param no_of_sts: integer Range: 0 to Max
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mu')
		"""
		param = Conversions.decimal_value_to_str(no_of_sts)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:MU{userIx_cmd_val}:NSTS {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default, userIx=repcap.UserIx.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:MU<ST0>:NSTS \n
		Snippet: value: int = driver.source.bb.wlnn.fblock.mu.nsts.get(frameBlock = repcap.FrameBlock.Default, userIx = repcap.UserIx.Default) \n
		Sets the number of space time streams for each user. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mu')
			:return: no_of_sts: integer Range: 0 to Max"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:MU{userIx_cmd_val}:NSTS?')
		return Conversions.str_to_int(response)
