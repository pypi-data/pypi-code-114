from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dcycle:
	"""Dcycle commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dcycle", core, parent)

	def get(self, frameBlock=repcap.FrameBlock.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:DATA:DCYCle \n
		Snippet: value: float = driver.source.bb.wlnn.fblock.data.dcycle.get(frameBlock = repcap.FrameBlock.Default) \n
		Queries the duty cycle, i.e. the ratio of frame duration and total signal length. Frame duration and duty cycle are
		related to data length and number of data symbols. Whenever one of them changes, the frame duration and duty cycle are
		updated. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: duty_cycle: float Range: 0.1 to 1"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:DATA:DCYCle?')
		return Conversions.str_to_float(response)
