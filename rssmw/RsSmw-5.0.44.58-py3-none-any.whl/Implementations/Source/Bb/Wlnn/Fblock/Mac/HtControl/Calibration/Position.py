from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Position:
	"""Position commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("position", core, parent)

	def set(self, position: List[str], frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:MAC:HTControl:CALibration:POSition \n
		Snippet: driver.source.bb.wlnn.fblock.mac.htControl.calibration.position.set(position = ['raw1', 'raw2', 'raw3'], frameBlock = repcap.FrameBlock.Default) \n
		Sets the value for the calibration position. 00 = Not a calibration frame (Default setting) 01 = Calibration Start 10 =
		Sounding Response 11 = Sounding Complete \n
			:param position: integer Range: #H0,2 to #H3,2
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.list_to_csv_str(position)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:MAC:HTControl:CALibration:POSition {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:MAC:HTControl:CALibration:POSition \n
		Snippet: value: List[str] = driver.source.bb.wlnn.fblock.mac.htControl.calibration.position.get(frameBlock = repcap.FrameBlock.Default) \n
		Sets the value for the calibration position. 00 = Not a calibration frame (Default setting) 01 = Calibration Start 10 =
		Sounding Response 11 = Sounding Complete \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: position: integer Range: #H0,2 to #H3,2"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:MAC:HTControl:CALibration:POSition?')
		return Conversions.str_to_str_list(response)
