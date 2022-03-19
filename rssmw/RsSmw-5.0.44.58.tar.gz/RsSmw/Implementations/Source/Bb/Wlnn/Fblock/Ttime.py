from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ttime:
	"""Ttime commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ttime", core, parent)

	def set(self, ttime: float, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:TTIMe \n
		Snippet: driver.source.bb.wlnn.fblock.ttime.set(ttime = 1.0, frameBlock = repcap.FrameBlock.Default) \n
		Sets the transition time when time domain windowing is active. The transition time defines the overlap range of two OFDM
		symbols. At a setting of 100 ns and if BW = 20 MHz, one sample overlaps. \n
			:param ttime: float Range: 0 to 1000 ns
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.decimal_value_to_str(ttime)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:TTIMe {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:TTIMe \n
		Snippet: value: float = driver.source.bb.wlnn.fblock.ttime.get(frameBlock = repcap.FrameBlock.Default) \n
		Sets the transition time when time domain windowing is active. The transition time defines the overlap range of two OFDM
		symbols. At a setting of 100 ns and if BW = 20 MHz, one sample overlaps. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: ttime: float Range: 0 to 1000 ns"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:TTIMe?')
		return Conversions.str_to_float(response)
