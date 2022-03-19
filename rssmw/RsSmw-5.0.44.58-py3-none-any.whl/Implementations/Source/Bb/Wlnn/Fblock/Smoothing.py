from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Smoothing:
	"""Smoothing commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("smoothing", core, parent)

	def set(self, smoothing: bool, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:SMOothing \n
		Snippet: driver.source.bb.wlnn.fblock.smoothing.set(smoothing = False, frameBlock = repcap.FrameBlock.Default) \n
		(available for all Tx modes, except VHT) This command indicates to the receiver whether frequency-domain smoothing is
		recommended as part of channel estimation. \n
			:param smoothing: OFF| ON ON Indicates that channel estimate smoothing is recommended. OFF Indicates that only per-carrier independent channel (unsmoothed) estimate is recommended.
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.bool_to_str(smoothing)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:SMOothing {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:SMOothing \n
		Snippet: value: bool = driver.source.bb.wlnn.fblock.smoothing.get(frameBlock = repcap.FrameBlock.Default) \n
		(available for all Tx modes, except VHT) This command indicates to the receiver whether frequency-domain smoothing is
		recommended as part of channel estimation. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: smoothing: OFF| ON ON Indicates that channel estimate smoothing is recommended. OFF Indicates that only per-carrier independent channel (unsmoothed) estimate is recommended."""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:SMOothing?')
		return Conversions.str_to_bool(response)
