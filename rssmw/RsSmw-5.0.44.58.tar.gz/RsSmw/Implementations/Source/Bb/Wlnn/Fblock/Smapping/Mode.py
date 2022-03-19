from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.WlannFbSpatMapMode, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:SMAPping:MODE \n
		Snippet: driver.source.bb.wlnn.fblock.smapping.mode.set(mode = enums.WlannFbSpatMapMode.BEAMforming, frameBlock = repcap.FrameBlock.Default) \n
		Selects the spatial mapping mode for the selected frame block. Except of the beamforming mode, the matrix element values
		are loaded by using info class methods. \n
			:param mode: OFF| DIRect| EXPansion| BEAMforming| INDirect OFF (only 'LEGACY' mode) The spatial mapping mode is switched off automatically. DIRect (only active with physical modes MIXED MODE or GREEN FIELD when NTX = NSTS) The transmit matrix is a CSD matrix, that is, diagonal matrix of unit magnitude and complex values that represent cyclic shifts in the time domain. EXPansion (only active with physical modes MIXED MODE or GREEN FIELD) The transmit matrix is the product of a CSD matrix and a square matrix formed of orthogonal columns, as defined in the IEEE 802.11n specification. INDirect (only active with physical modes MIXED MODE or GREEN FIELD) The transmit matrix is the product of a CSD matrix and the Hadamard unitary matrix.
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.WlannFbSpatMapMode)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:SMAPping:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, frameBlock=repcap.FrameBlock.Default) -> enums.WlannFbSpatMapMode:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:SMAPping:MODE \n
		Snippet: value: enums.WlannFbSpatMapMode = driver.source.bb.wlnn.fblock.smapping.mode.get(frameBlock = repcap.FrameBlock.Default) \n
		Selects the spatial mapping mode for the selected frame block. Except of the beamforming mode, the matrix element values
		are loaded by using info class methods. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: mode: OFF| DIRect| EXPansion| BEAMforming| INDirect OFF (only 'LEGACY' mode) The spatial mapping mode is switched off automatically. DIRect (only active with physical modes MIXED MODE or GREEN FIELD when NTX = NSTS) The transmit matrix is a CSD matrix, that is, diagonal matrix of unit magnitude and complex values that represent cyclic shifts in the time domain. EXPansion (only active with physical modes MIXED MODE or GREEN FIELD) The transmit matrix is the product of a CSD matrix and a square matrix formed of orthogonal columns, as defined in the IEEE 802.11n specification. INDirect (only active with physical modes MIXED MODE or GREEN FIELD) The transmit matrix is the product of a CSD matrix and the Hadamard unitary matrix."""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:SMAPping:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.WlannFbSpatMapMode)
