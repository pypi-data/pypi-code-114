from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Link:
	"""Link commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("link", core, parent)

	def set(self, link_direction: enums.UpDownDirection, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:LINK \n
		Snippet: driver.source.bb.wlnn.fblock.link.set(link_direction = enums.UpDownDirection.DOWN, frameBlock = repcap.FrameBlock.Default) \n
		Sets the link direction. \n
			:param link_direction: DOWN| UP
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.enum_scalar_to_str(link_direction, enums.UpDownDirection)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:LINK {param}')

	# noinspection PyTypeChecker
	def get(self, frameBlock=repcap.FrameBlock.Default) -> enums.UpDownDirection:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:LINK \n
		Snippet: value: enums.UpDownDirection = driver.source.bb.wlnn.fblock.link.get(frameBlock = repcap.FrameBlock.Default) \n
		Sets the link direction. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: link_direction: DOWN| UP"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:LINK?')
		return Conversions.str_to_scalar_enum(response, enums.UpDownDirection)
