from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fcount:
	"""Fcount commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fcount", core, parent)

	def set(self, fcount: int, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:FCOunt \n
		Snippet: driver.source.bb.wlnn.fblock.fcount.set(fcount = 1, frameBlock = repcap.FrameBlock.Default) \n
		Sets the number of frames to be transmitted in the current frame block. \n
			:param fcount: integer Range: 1 to 20 000
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.decimal_value_to_str(fcount)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:FCOunt {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:FCOunt \n
		Snippet: value: int = driver.source.bb.wlnn.fblock.fcount.get(frameBlock = repcap.FrameBlock.Default) \n
		Sets the number of frames to be transmitted in the current frame block. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: fcount: integer Range: 1 to 20 000"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:FCOunt?')
		return Conversions.str_to_int(response)
