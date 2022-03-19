from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PnSeed:
	"""PnSeed commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pnSeed", core, parent)

	def set(self, pn_seed: List[str], frameBlock=repcap.FrameBlock.Default, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:[USER<DI>]:PNSeed \n
		Snippet: driver.source.bb.wlnn.fblock.user.pnSeed.set(pn_seed = ['raw1', 'raw2', 'raw3'], frameBlock = repcap.FrameBlock.Default, userIx = repcap.UserIx.Default) \n
		Sets the PN seed. Use this setting, if you don't use the default PN seed. \n
			:param pn_seed: 24 bits | 24 bit Range: #H000001,24 to #H7FFFFF,24
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.list_to_csv_str(pn_seed)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:USER{userIx_cmd_val}:PNSeed {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default, userIx=repcap.UserIx.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:[USER<DI>]:PNSeed \n
		Snippet: value: List[str] = driver.source.bb.wlnn.fblock.user.pnSeed.get(frameBlock = repcap.FrameBlock.Default, userIx = repcap.UserIx.Default) \n
		Sets the PN seed. Use this setting, if you don't use the default PN seed. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: pn_seed: 24 bits | 24 bit Range: #H000001,24 to #H7FFFFF,24"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:USER{userIx_cmd_val}:PNSeed?')
		return Conversions.str_to_str_list(response)
