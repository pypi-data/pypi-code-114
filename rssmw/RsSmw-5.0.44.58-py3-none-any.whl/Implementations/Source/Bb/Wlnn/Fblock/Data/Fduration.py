from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fduration:
	"""Fduration commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fduration", core, parent)

	def get(self, frameBlock=repcap.FrameBlock.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:DATA:FDURation \n
		Snippet: value: float = driver.source.bb.wlnn.fblock.data.fduration.get(frameBlock = repcap.FrameBlock.Default) \n
		Queries the duration of the frame in milliseconds, i.e. the WLAN burst length. Frame duration and duty cycle are related
		to data length and number of data symbols. Whenever one of them changes, the frame duration and duty cycle are updated. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: frame_duration: float Range: 0 to 1000"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:DATA:FDURation?')
		return Conversions.str_to_float(response)
