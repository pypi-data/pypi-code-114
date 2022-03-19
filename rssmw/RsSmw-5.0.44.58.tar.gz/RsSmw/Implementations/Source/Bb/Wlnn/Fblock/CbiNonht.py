from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CbiNonht:
	"""CbiNonht commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cbiNonht", core, parent)

	def set(self, cbi_nonht: enums.WlannFbChBwInNonHt, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:CBINonht \n
		Snippet: driver.source.bb.wlnn.fblock.cbiNonht.set(cbi_nonht = enums.WlannFbChBwInNonHt.B160, frameBlock = repcap.FrameBlock.Default) \n
		(Available only for VHT Tx mode) The command is used to modify the first 7 bits of the scrambling sequence to indicate
		the duplicated bandwidth of the PPDU. \n
			:param cbi_nonht: B20| B40| B80| B160| OFF B20|B40|B80|B160 Indicates 20 MHz, 40MHz, 80MHz or 160 (80+80) MHz channel bandwidth of the transmitted packet. OFF Channel bandwidth in Non HT is not present. Unit: MHz
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.enum_scalar_to_str(cbi_nonht, enums.WlannFbChBwInNonHt)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:CBINonht {param}')

	# noinspection PyTypeChecker
	def get(self, frameBlock=repcap.FrameBlock.Default) -> enums.WlannFbChBwInNonHt:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:CBINonht \n
		Snippet: value: enums.WlannFbChBwInNonHt = driver.source.bb.wlnn.fblock.cbiNonht.get(frameBlock = repcap.FrameBlock.Default) \n
		(Available only for VHT Tx mode) The command is used to modify the first 7 bits of the scrambling sequence to indicate
		the duplicated bandwidth of the PPDU. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: cbi_nonht: B20| B40| B80| B160| OFF B20|B40|B80|B160 Indicates 20 MHz, 40MHz, 80MHz or 160 (80+80) MHz channel bandwidth of the transmitted packet. OFF Channel bandwidth in Non HT is not present. Unit: MHz"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:CBINonht?')
		return Conversions.str_to_scalar_enum(response, enums.WlannFbChBwInNonHt)
