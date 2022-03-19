from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RdgMore:
	"""RdgMore commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rdgMore", core, parent)

	def set(self, vht_rdg_more: List[str], frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:MAC:VHTControl:RDGMore \n
		Snippet: driver.source.bb.wlnn.fblock.mac.vhtControl.rdgMore.set(vht_rdg_more = ['raw1', 'raw2', 'raw3'], frameBlock = repcap.FrameBlock.Default) \n
		The command issues the reverse direction grant. When transmitted by an initiator or a responder, this field is
		interpreted differently. Transmitted by Initiator 0 = No reverse grant. 1 = A reverse grant is present, as defined by the
		Duration/ID field. Transmitted by Responder 0 = The PPDU carrying the MPDU is the last transmission by the responder. 1 =
		The PPDU carrying the frame is followed by another PPDU. \n
			:param vht_rdg_more: integer
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.list_to_csv_str(vht_rdg_more)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:MAC:VHTControl:RDGMore {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:MAC:VHTControl:RDGMore \n
		Snippet: value: List[str] = driver.source.bb.wlnn.fblock.mac.vhtControl.rdgMore.get(frameBlock = repcap.FrameBlock.Default) \n
		The command issues the reverse direction grant. When transmitted by an initiator or a responder, this field is
		interpreted differently. Transmitted by Initiator 0 = No reverse grant. 1 = A reverse grant is present, as defined by the
		Duration/ID field. Transmitted by Responder 0 = The PPDU carrying the MPDU is the last transmission by the responder. 1 =
		The PPDU carrying the frame is followed by another PPDU. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: vht_rdg_more: integer"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:MAC:VHTControl:RDGMore?')
		return Conversions.str_to_str_list(response)
