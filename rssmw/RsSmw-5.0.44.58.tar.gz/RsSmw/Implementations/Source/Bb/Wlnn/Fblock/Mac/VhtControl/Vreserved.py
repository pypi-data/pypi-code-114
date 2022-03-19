from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Vreserved:
	"""Vreserved commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vreserved", core, parent)

	def set(self, vht_reserved: List[str], frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:MAC:VHTControl:VREServed \n
		Snippet: driver.source.bb.wlnn.fblock.mac.vhtControl.vreserved.set(vht_reserved = ['raw1', 'raw2', 'raw3'], frameBlock = repcap.FrameBlock.Default) \n
		This signal field is currently defined, but not used. It is set to zero by the transmitter and ignored by the receiver. \n
			:param vht_reserved: integer
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.list_to_csv_str(vht_reserved)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:MAC:VHTControl:VREServed {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:MAC:VHTControl:VREServed \n
		Snippet: value: List[str] = driver.source.bb.wlnn.fblock.mac.vhtControl.vreserved.get(frameBlock = repcap.FrameBlock.Default) \n
		This signal field is currently defined, but not used. It is set to zero by the transmitter and ignored by the receiver. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: vht_reserved: integer"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:MAC:VHTControl:VREServed?')
		return Conversions.str_to_str_list(response)
