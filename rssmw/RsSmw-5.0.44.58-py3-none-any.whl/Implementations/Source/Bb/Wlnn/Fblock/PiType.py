from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PiType:
	"""PiType commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("piType", core, parent)

	def set(self, pi_type: enums.WlannFbPilotType, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:PITYpe \n
		Snippet: driver.source.bb.wlnn.fblock.piType.set(pi_type = enums.WlannFbPilotType.FIXed, frameBlock = repcap.FrameBlock.Default) \n
		No command help available \n
			:param pi_type: No help available
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.enum_scalar_to_str(pi_type, enums.WlannFbPilotType)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:PITYpe {param}')

	# noinspection PyTypeChecker
	def get(self, frameBlock=repcap.FrameBlock.Default) -> enums.WlannFbPilotType:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:PITYpe \n
		Snippet: value: enums.WlannFbPilotType = driver.source.bb.wlnn.fblock.piType.get(frameBlock = repcap.FrameBlock.Default) \n
		No command help available \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: pi_type: No help available"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:PITYpe?')
		return Conversions.str_to_scalar_enum(response, enums.WlannFbPilotType)
