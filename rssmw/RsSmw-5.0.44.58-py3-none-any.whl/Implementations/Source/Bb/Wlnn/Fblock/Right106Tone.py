from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Right106Tone:
	"""Right106Tone commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("right106Tone", core, parent)

	def set(self, right_106_tone_ru: bool, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:RIGHt106tone \n
		Snippet: driver.source.bb.wlnn.fblock.right106Tone.set(right_106_tone_ru = False, frameBlock = repcap.FrameBlock.Default) \n
		If enabled, indicates that the right 106-tone RU is within the primary 20 MHz. \n
			:param right_106_tone_ru: 1| ON| 0| OFF
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.bool_to_str(right_106_tone_ru)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:RIGHt106tone {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:RIGHt106tone \n
		Snippet: value: bool = driver.source.bb.wlnn.fblock.right106Tone.get(frameBlock = repcap.FrameBlock.Default) \n
		If enabled, indicates that the right 106-tone RU is within the primary 20 MHz. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: right_106_tone_ru: 1| ON| 0| OFF"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:RIGHt106tone?')
		return Conversions.str_to_bool(response)
