from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mgl:
	"""Mgl commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mgl", core, parent)

	def set(self, mfsi_gid_l: List[str], frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:MAC:VHTControl:MGL \n
		Snippet: driver.source.bb.wlnn.fblock.mac.vhtControl.mgl.set(mfsi_gid_l = ['raw1', 'raw2', 'raw3'], frameBlock = repcap.FrameBlock.Default) \n
		The command determines the information of the MFSI/GID-L subfield. MFB = 0 If the Unsolicited MFB subfield is set to 0,
		the MFSI/GID-L subfield contains the received value of MSI contained in the frame to which the MFB information refers.
		MFB = 1 The MFSI/GID-L subfield contains the lowest 3 bits of Group ID of the PPDU to which the unsolicited MFB refers. \n
			:param mfsi_gid_l: integer
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.list_to_csv_str(mfsi_gid_l)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:MAC:VHTControl:MGL {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:MAC:VHTControl:MGL \n
		Snippet: value: List[str] = driver.source.bb.wlnn.fblock.mac.vhtControl.mgl.get(frameBlock = repcap.FrameBlock.Default) \n
		The command determines the information of the MFSI/GID-L subfield. MFB = 0 If the Unsolicited MFB subfield is set to 0,
		the MFSI/GID-L subfield contains the received value of MSI contained in the frame to which the MFB information refers.
		MFB = 1 The MFSI/GID-L subfield contains the lowest 3 bits of Group ID of the PPDU to which the unsolicited MFB refers. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: mfsi_gid_l: integer"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:MAC:VHTControl:MGL?')
		return Conversions.str_to_str_list(response)
