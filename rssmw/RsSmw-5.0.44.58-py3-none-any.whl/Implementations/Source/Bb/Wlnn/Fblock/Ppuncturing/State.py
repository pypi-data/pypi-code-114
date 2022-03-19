from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, preamble_punc: bool, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:PPUNcturing:STATe \n
		Snippet: driver.source.bb.wlnn.fblock.ppuncturing.state.set(preamble_punc = False, frameBlock = repcap.FrameBlock.Default) \n
		Enables preamble puncturing of the HE MU PPDU in 80 MHz or (80+80) /160 MHz channels. \n
			:param preamble_punc: 1| ON| 0| OFF
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.bool_to_str(preamble_punc)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:PPUNcturing:STATe {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:PPUNcturing:STATe \n
		Snippet: value: bool = driver.source.bb.wlnn.fblock.ppuncturing.state.get(frameBlock = repcap.FrameBlock.Default) \n
		Enables preamble puncturing of the HE MU PPDU in 80 MHz or (80+80) /160 MHz channels. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: preamble_punc: 1| ON| 0| OFF"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:PPUNcturing:STATe?')
		return Conversions.str_to_bool(response)
