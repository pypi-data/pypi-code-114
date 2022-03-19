from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dbinonht:
	"""Dbinonht commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dbinonht", core, parent)

	def set(self, dbinonht: enums.WlannFbDynBwInNonHt, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:DBINonht \n
		Snippet: driver.source.bb.wlnn.fblock.dbinonht.set(dbinonht = enums.WlannFbDynBwInNonHt.DYN, frameBlock = repcap.FrameBlock.Default) \n
		(available only for VHT Tx mode) Modifys the first 7 bits of the scrambling sequence to indicate if the transmitter is
		capable of 'Static' or 'Dynamic' bandwidth operation. \n
			:param dbinonht: STAT| DYN| OFF STAT The transmitter is capable of static bandwidth operation. DYN The transmitter is capable of dynamic bandwidth operation. OFF Dynamic bandwidth in Non HT is not present.
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.enum_scalar_to_str(dbinonht, enums.WlannFbDynBwInNonHt)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:DBINonht {param}')

	# noinspection PyTypeChecker
	def get(self, frameBlock=repcap.FrameBlock.Default) -> enums.WlannFbDynBwInNonHt:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:DBINonht \n
		Snippet: value: enums.WlannFbDynBwInNonHt = driver.source.bb.wlnn.fblock.dbinonht.get(frameBlock = repcap.FrameBlock.Default) \n
		(available only for VHT Tx mode) Modifys the first 7 bits of the scrambling sequence to indicate if the transmitter is
		capable of 'Static' or 'Dynamic' bandwidth operation. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: dbinonht: STAT| DYN| OFF STAT The transmitter is capable of static bandwidth operation. DYN The transmitter is capable of dynamic bandwidth operation. OFF Dynamic bandwidth in Non HT is not present."""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:DBINonht?')
		return Conversions.str_to_scalar_enum(response, enums.WlannFbDynBwInNonHt)
