from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Binterval:
	"""Binterval commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("binterval", core, parent)

	def set(self, binterval: float, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:BFConfiguration:BINTerval \n
		Snippet: driver.source.bb.wlnn.fblock.bfConfiguration.binterval.set(binterval = 1.0, frameBlock = repcap.FrameBlock.Default) \n
		Defines the time interval between two beacon transmissions. \n
			:param binterval: float Range: 0 to 65, Unit: s
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.decimal_value_to_str(binterval)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:BFConfiguration:BINTerval {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:BFConfiguration:BINTerval \n
		Snippet: value: float = driver.source.bb.wlnn.fblock.bfConfiguration.binterval.get(frameBlock = repcap.FrameBlock.Default) \n
		Defines the time interval between two beacon transmissions. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: binterval: float Range: 0 to 65, Unit: s"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:BFConfiguration:BINTerval?')
		return Conversions.str_to_float(response)
