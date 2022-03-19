from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaxPe:
	"""MaxPe commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maxPe", core, parent)

	def set(self, max_pe_duration: enums.WlannFbPpduPeDuraion, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:MAXPe \n
		Snippet: driver.source.bb.wlnn.fblock.maxPe.set(max_pe_duration = enums.WlannFbPpduPeDuraion.PE0, frameBlock = repcap.FrameBlock.Default) \n
		Sets the maximum packet extension (PE) duration. \n
			:param max_pe_duration: PE0| PE8| PE16 PE0: 0 us PE8: 8 us PE16: 16 us
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.enum_scalar_to_str(max_pe_duration, enums.WlannFbPpduPeDuraion)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:MAXPe {param}')

	# noinspection PyTypeChecker
	def get(self, frameBlock=repcap.FrameBlock.Default) -> enums.WlannFbPpduPeDuraion:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:MAXPe \n
		Snippet: value: enums.WlannFbPpduPeDuraion = driver.source.bb.wlnn.fblock.maxPe.get(frameBlock = repcap.FrameBlock.Default) \n
		Sets the maximum packet extension (PE) duration. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: max_pe_duration: PE0| PE8| PE16 PE0: 0 us PE8: 8 us PE16: 16 us"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:MAXPe?')
		return Conversions.str_to_scalar_enum(response, enums.WlannFbPpduPeDuraion)
