from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Segment:
	"""Segment commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("segment", core, parent)

	def set(self, segment: enums.WlannFbSegment, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:SEGMent \n
		Snippet: driver.source.bb.wlnn.fblock.segment.set(segment = enums.WlannFbSegment.BOTH, frameBlock = repcap.FrameBlock.Default) \n
		Selects one of the two segments in VHT-80+80 MHz mode with transmission bandwidth 80 MHz or 160 MHz. Both segments can
		only be generated with bandwidth 160 MHz. This parameter applies to VHT-80+80 MHz Tx mode only. \n
			:param segment: SEG0| SEG1| BOTH
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.enum_scalar_to_str(segment, enums.WlannFbSegment)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:SEGMent {param}')

	# noinspection PyTypeChecker
	def get(self, frameBlock=repcap.FrameBlock.Default) -> enums.WlannFbSegment:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:SEGMent \n
		Snippet: value: enums.WlannFbSegment = driver.source.bb.wlnn.fblock.segment.get(frameBlock = repcap.FrameBlock.Default) \n
		Selects one of the two segments in VHT-80+80 MHz mode with transmission bandwidth 80 MHz or 160 MHz. Both segments can
		only be generated with bandwidth 160 MHz. This parameter applies to VHT-80+80 MHz Tx mode only. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: segment: SEG0| SEG1| BOTH"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:SEGMent?')
		return Conversions.str_to_scalar_enum(response, enums.WlannFbSegment)
