from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AcConstraint:
	"""AcConstraint commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("acConstraint", core, parent)

	def set(self, vht_ac_constraint: List[str], frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:MAC:VHTControl:ACConstraint \n
		Snippet: driver.source.bb.wlnn.fblock.mac.vhtControl.acConstraint.set(vht_ac_constraint = ['raw1', 'raw2', 'raw3'], frameBlock = repcap.FrameBlock.Default) \n
		The command sets the value for the AC signal field. It indicates the access point of the responder (1 bit) . \n
			:param vht_ac_constraint: integer 0 The response may contain data from any TID (Traffic Identifier) 1 The response may contain data only from the same AC as the last data received from the initiator.
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.list_to_csv_str(vht_ac_constraint)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:MAC:VHTControl:ACConstraint {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:MAC:VHTControl:ACConstraint \n
		Snippet: value: List[str] = driver.source.bb.wlnn.fblock.mac.vhtControl.acConstraint.get(frameBlock = repcap.FrameBlock.Default) \n
		The command sets the value for the AC signal field. It indicates the access point of the responder (1 bit) . \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: vht_ac_constraint: integer 0 The response may contain data from any TID (Traffic Identifier) 1 The response may contain data only from the same AC as the last data received from the initiator."""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:MAC:VHTControl:ACConstraint?')
		return Conversions.str_to_str_list(response)
