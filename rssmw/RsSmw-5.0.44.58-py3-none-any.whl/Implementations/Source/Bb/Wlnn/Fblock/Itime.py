from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Itime:
	"""Itime commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("itime", core, parent)

	def set(self, itime: float, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:ITIMe \n
		Snippet: driver.source.bb.wlnn.fblock.itime.set(itime = 1.0, frameBlock = repcap.FrameBlock.Default) \n
		Sets the time interval separating two frames in this frame block. The default unit for the time interval are seconds.
		However, the time interval can be set in milliseconds. In this case the unit has to be set. \n
			:param itime: float Range: 0 to 1
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.decimal_value_to_str(itime)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:ITIMe {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:ITIMe \n
		Snippet: value: float = driver.source.bb.wlnn.fblock.itime.get(frameBlock = repcap.FrameBlock.Default) \n
		Sets the time interval separating two frames in this frame block. The default unit for the time interval are seconds.
		However, the time interval can be set in milliseconds. In this case the unit has to be set. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: itime: float Range: 0 to 1"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:ITIMe?')
		return Conversions.str_to_float(response)
