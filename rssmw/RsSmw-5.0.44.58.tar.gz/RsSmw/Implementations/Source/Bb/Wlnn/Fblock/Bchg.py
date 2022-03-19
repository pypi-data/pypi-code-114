from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bchg:
	"""Bchg commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bchg", core, parent)

	def set(self, beam_change: bool, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:BCHG \n
		Snippet: driver.source.bb.wlnn.fblock.bchg.set(beam_change = False, frameBlock = repcap.FrameBlock.Default) \n
		If enabled, the beam is changed between pre-HE and HE modulated fields. \n
			:param beam_change: OFF| ON| 1| 0
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.bool_to_str(beam_change)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:BCHG {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:BCHG \n
		Snippet: value: bool = driver.source.bb.wlnn.fblock.bchg.get(frameBlock = repcap.FrameBlock.Default) \n
		If enabled, the beam is changed between pre-HE and HE modulated fields. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: beam_change: OFF| ON| 1| 0"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:BCHG?')
		return Conversions.str_to_bool(response)
