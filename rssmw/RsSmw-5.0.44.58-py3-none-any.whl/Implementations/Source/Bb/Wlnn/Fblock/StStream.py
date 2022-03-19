from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StStream:
	"""StStream commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stStream", core, parent)

	def set(self, st_stream: int, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:STSTream \n
		Snippet: driver.source.bb.wlnn.fblock.stStream.set(st_stream = 1, frameBlock = repcap.FrameBlock.Default) \n
		Sets the number of the space time streams. This value depends on the number of spatial streams defined with command
		SOURce:BB:WLNN:FBLock:SSTReam. Changing the number of the Spatial Streams immediately changes the value of the Space Time
		Streams to the same value. \n
			:param st_stream: integer Range: 1 to dynamic
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.decimal_value_to_str(st_stream)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:STSTream {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:STSTream \n
		Snippet: value: int = driver.source.bb.wlnn.fblock.stStream.get(frameBlock = repcap.FrameBlock.Default) \n
		Sets the number of the space time streams. This value depends on the number of spatial streams defined with command
		SOURce:BB:WLNN:FBLock:SSTReam. Changing the number of the Spatial Streams immediately changes the value of the Space Time
		Streams to the same value. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: st_stream: integer Range: 1 to dynamic"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:STSTream?')
		return Conversions.str_to_int(response)
