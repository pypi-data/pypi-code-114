from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HeIndicator:
	"""HeIndicator commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("heIndicator", core, parent)

	def get(self, frameBlock=repcap.FrameBlock.Default, userIx=repcap.UserIx.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:[USER<DI>]:MAC:HEControl:HEINdicator \n
		Snippet: value: List[str] = driver.source.bb.wlnn.fblock.user.mac.heControl.heIndicator.get(frameBlock = repcap.FrameBlock.Default, userIx = repcap.UserIx.Default) \n
		Indicates the use of the HE format, if [:SOURce<hw>]:BB:WLNN:FBLock<ch>[:USER<di>]:MAC:VHTControl:HVINdicator? is set to
		1. The command returns 1 if the HE format is used and 0 if not. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: he_indicator: integer"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:USER{userIx_cmd_val}:MAC:HEControl:HEINdicator?')
		return Conversions.str_to_str_list(response)
