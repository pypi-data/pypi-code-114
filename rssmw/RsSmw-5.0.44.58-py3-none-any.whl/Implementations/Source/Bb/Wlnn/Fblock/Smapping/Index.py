from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Index:
	"""Index commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("index", core, parent)

	def set(self, index: int, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:SMAPping:INDex \n
		Snippet: driver.source.bb.wlnn.fblock.smapping.index.set(index = 1, frameBlock = repcap.FrameBlock.Default) \n
		Sets the index of the subcarrier. A matrix is mapped to each subcarrier. Except for k=0, the index can be set in the
		value range of -64 to 63 \n
			:param index: integer Range: depends on TxMode to depends on TxMode
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.decimal_value_to_str(index)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:SMAPping:INDex {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:SMAPping:INDex \n
		Snippet: value: int = driver.source.bb.wlnn.fblock.smapping.index.get(frameBlock = repcap.FrameBlock.Default) \n
		Sets the index of the subcarrier. A matrix is mapped to each subcarrier. Except for k=0, the index can be set in the
		value range of -64 to 63 \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: index: integer Range: depends on TxMode to depends on TxMode"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:SMAPping:INDex?')
		return Conversions.str_to_int(response)
