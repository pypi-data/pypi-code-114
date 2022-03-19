from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Boost:
	"""Boost commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("boost", core, parent)

	def set(self, boost: float, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:BOOSt \n
		Snippet: driver.source.bb.wlnn.fblock.boost.set(boost = 1.0, frameBlock = repcap.FrameBlock.Default) \n
		Assigns a specific RMS power boost/attenuation to the corresponding frame block modulation. The power level of a frame
		block modulation is calculated as sum of the power boost and the power level set in the header of the instrument. Note:
		At least one frame block should have a power boost set to 0 dB value for this gated power mode functionality to work
		properly. \n
			:param boost: float Range: -80 to 0, Unit: dB
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.decimal_value_to_str(boost)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:BOOSt {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:BOOSt \n
		Snippet: value: float = driver.source.bb.wlnn.fblock.boost.get(frameBlock = repcap.FrameBlock.Default) \n
		Assigns a specific RMS power boost/attenuation to the corresponding frame block modulation. The power level of a frame
		block modulation is calculated as sum of the power boost and the power level set in the header of the instrument. Note:
		At least one frame block should have a power boost set to 0 dB value for this gated power mode functionality to work
		properly. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: boost: float Range: -80 to 0, Unit: dB"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:BOOSt?')
		return Conversions.str_to_float(response)
