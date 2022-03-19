from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ntps:
	"""Ntps commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ntps", core, parent)

	def set(self, ntps: bool, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:NTPS \n
		Snippet: driver.source.bb.wlnn.fblock.ntps.set(ntps = False, frameBlock = repcap.FrameBlock.Default) \n
		(Available only for VHT Tx mode) Indicates whether VHT AP allows VHT non-AP STAs in TXOP power save mode to enter during
		TXOP. \n
			:param ntps: OFF| ON ON Indicates that the VHT AP allows VHT non-AP STAs to enter doze mode during a TXOP. OFF Indicates that the VHT AP does not allow VHT non-AP STAs to enter doze mode during a TXOP.
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.bool_to_str(ntps)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:NTPS {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:NTPS \n
		Snippet: value: bool = driver.source.bb.wlnn.fblock.ntps.get(frameBlock = repcap.FrameBlock.Default) \n
		(Available only for VHT Tx mode) Indicates whether VHT AP allows VHT non-AP STAs in TXOP power save mode to enter during
		TXOP. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: ntps: OFF| ON ON Indicates that the VHT AP allows VHT non-AP STAs to enter doze mode during a TXOP. OFF Indicates that the VHT AP does not allow VHT non-AP STAs to enter doze mode during a TXOP."""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:NTPS?')
		return Conversions.str_to_bool(response)
