from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bw:
	"""Bw commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bw", core, parent)

	def set(self, preamble_punc_bw: enums.WlannFbPpduPreamblePuncturingBw, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:PPUNcturing:BW \n
		Snippet: driver.source.bb.wlnn.fblock.ppuncturing.bw.set(preamble_punc_bw = enums.WlannFbPpduPreamblePuncturingBw._4, frameBlock = repcap.FrameBlock.Default) \n
		Sets the bandwidth mode of preamble puncturing. \n
			:param preamble_punc_bw: 4| 5| 6| 7 4|5 Sets the bandwidth mode for HE80 channels. 6|7 Sets the bandwidth mode for HE8080 channels.
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.enum_scalar_to_str(preamble_punc_bw, enums.WlannFbPpduPreamblePuncturingBw)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:PPUNcturing:BW {param}')

	# noinspection PyTypeChecker
	def get(self, frameBlock=repcap.FrameBlock.Default) -> enums.WlannFbPpduPreamblePuncturingBw:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:PPUNcturing:BW \n
		Snippet: value: enums.WlannFbPpduPreamblePuncturingBw = driver.source.bb.wlnn.fblock.ppuncturing.bw.get(frameBlock = repcap.FrameBlock.Default) \n
		Sets the bandwidth mode of preamble puncturing. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: preamble_punc_bw: 4| 5| 6| 7 4|5 Sets the bandwidth mode for HE80 channels. 6|7 Sets the bandwidth mode for HE8080 channels."""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:PPUNcturing:BW?')
		return Conversions.str_to_scalar_enum(response, enums.WlannFbPpduPreamblePuncturingBw)
