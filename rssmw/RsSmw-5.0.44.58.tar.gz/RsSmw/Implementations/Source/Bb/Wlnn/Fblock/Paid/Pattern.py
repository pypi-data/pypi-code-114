from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pattern:
	"""Pattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)

	def set(self, pattern: List[str], frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:PAID:PATTern \n
		Snippet: driver.source.bb.wlnn.fblock.paid.pattern.set(pattern = ['raw1', 'raw2', 'raw3'], frameBlock = repcap.FrameBlock.Default) \n
		(avaliable only for VHT Tx mode) The command provides an abbreviated indication of the intended recipient(s) of the frame. \n
			:param pattern: 9 bits Range: #H000,9 to #H1FF,9
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.list_to_csv_str(pattern)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:PAID:PATTern {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:PAID:PATTern \n
		Snippet: value: List[str] = driver.source.bb.wlnn.fblock.paid.pattern.get(frameBlock = repcap.FrameBlock.Default) \n
		(avaliable only for VHT Tx mode) The command provides an abbreviated indication of the intended recipient(s) of the frame. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: pattern: 9 bits Range: #H000,9 to #H1FF,9"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:PAID:PATTern?')
		return Conversions.str_to_str_list(response)
