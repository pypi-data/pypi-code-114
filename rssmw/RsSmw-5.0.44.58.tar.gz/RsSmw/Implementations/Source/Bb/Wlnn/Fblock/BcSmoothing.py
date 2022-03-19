from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BcSmoothing:
	"""BcSmoothing commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bcSmoothing", core, parent)

	def set(self, bc_smoothing: bool, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:BCSMoothing \n
		Snippet: driver.source.bb.wlnn.fblock.bcSmoothing.set(bc_smoothing = False, frameBlock = repcap.FrameBlock.Default) \n
		Activates beam change and smoothing. \n
			:param bc_smoothing: 1| ON| 0| OFF
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.bool_to_str(bc_smoothing)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:BCSMoothing {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:BCSMoothing \n
		Snippet: value: bool = driver.source.bb.wlnn.fblock.bcSmoothing.get(frameBlock = repcap.FrameBlock.Default) \n
		Activates beam change and smoothing. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: bc_smoothing: 1| ON| 0| OFF"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:BCSMoothing?')
		return Conversions.str_to_bool(response)
