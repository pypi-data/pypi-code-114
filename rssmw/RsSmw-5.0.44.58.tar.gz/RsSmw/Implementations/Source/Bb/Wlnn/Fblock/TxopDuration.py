from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TxopDuration:
	"""TxopDuration commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("txopDuration", core, parent)

	def set(self, tx_op_duraion: int, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:TXOPduration \n
		Snippet: driver.source.bb.wlnn.fblock.txopDuration.set(tx_op_duraion = 1, frameBlock = repcap.FrameBlock.Default) \n
		If transmission opportunity (TXOP) is set to 127, it indicates no duration information. If it is set to any other value,
		it indicates duration information for network allocation vector (NAV) parameter and that the TXOP is protected. \n
			:param tx_op_duraion: integer Range: 0 to 127
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.decimal_value_to_str(tx_op_duraion)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:TXOPduration {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:TXOPduration \n
		Snippet: value: int = driver.source.bb.wlnn.fblock.txopDuration.get(frameBlock = repcap.FrameBlock.Default) \n
		If transmission opportunity (TXOP) is set to 127, it indicates no duration information. If it is set to any other value,
		it indicates duration information for network allocation vector (NAV) parameter and that the TXOP is protected. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: tx_op_duraion: integer Range: 0 to 127"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:TXOPduration?')
		return Conversions.str_to_int(response)
