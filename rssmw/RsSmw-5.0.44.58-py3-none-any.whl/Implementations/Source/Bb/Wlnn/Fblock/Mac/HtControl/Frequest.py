from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequest:
	"""Frequest commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequest", core, parent)

	def set(self, frequest: List[str], frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:MAC:HTControl:FREQuest \n
		Snippet: driver.source.bb.wlnn.fblock.mac.htControl.frequest.set(frequest = ['raw1', 'raw2', 'raw3'], frameBlock = repcap.FrameBlock.Default) \n
		Sets the value for the feedback request. 00 = no request 01 = unsolicited feedback only 10 = immediate feedback 11 =
		aggregated feedback \n
			:param frequest: integer Range: #H0,2 to #H3,2
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.list_to_csv_str(frequest)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:MAC:HTControl:FREQuest {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:MAC:HTControl:FREQuest \n
		Snippet: value: List[str] = driver.source.bb.wlnn.fblock.mac.htControl.frequest.get(frameBlock = repcap.FrameBlock.Default) \n
		Sets the value for the feedback request. 00 = no request 01 = unsolicited feedback only 10 = immediate feedback 11 =
		aggregated feedback \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: frequest: integer Range: #H0,2 to #H3,2"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:MAC:HTControl:FREQuest?')
		return Conversions.str_to_str_list(response)
