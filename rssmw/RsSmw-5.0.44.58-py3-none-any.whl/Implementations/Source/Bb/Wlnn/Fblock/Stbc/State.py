from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	def get(self, frameBlock=repcap.FrameBlock.Default) -> enums.WlannFbStbcState:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:STBC:STATe \n
		Snippet: value: enums.WlannFbStbcState = driver.source.bb.wlnn.fblock.stbc.state.get(frameBlock = repcap.FrameBlock.Default) \n
		Queries the status of the space time block coding. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: state: INACtive| ACTive"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:STBC:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.WlannFbStbcState)
