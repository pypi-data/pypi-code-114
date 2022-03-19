from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EsStream:
	"""EsStream commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("esStream", core, parent)

	def set(self, es_stream: int, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:ESSTream \n
		Snippet: driver.source.bb.wlnn.fblock.esStream.set(es_stream = 1, frameBlock = repcap.FrameBlock.Default) \n
		Sets the value of the extended spatial streams. This field is active for frame block type sounding only to probe
		additional dimensions to the channel. \n
			:param es_stream: integer Range: 1 to dynamic
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.decimal_value_to_str(es_stream)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:ESSTream {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:ESSTream \n
		Snippet: value: int = driver.source.bb.wlnn.fblock.esStream.get(frameBlock = repcap.FrameBlock.Default) \n
		Sets the value of the extended spatial streams. This field is active for frame block type sounding only to probe
		additional dimensions to the channel. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: es_stream: integer Range: 1 to dynamic"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:ESSTream?')
		return Conversions.str_to_int(response)
