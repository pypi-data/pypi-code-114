from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EsDiffer:
	"""EsDiffer commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("esDiffer", core, parent)

	def set(self, eht_sig_differ: bool, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:ESDiffer \n
		Snippet: driver.source.bb.wlnn.fblock.esDiffer.set(eht_sig_differ = False, frameBlock = repcap.FrameBlock.Default) \n
		For EHT-160MHz/EHT-320MHz frames, activates different EHT-SIG fields for every 80 MHz channel. \n
			:param eht_sig_differ: 1| ON| 0| OFF
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.bool_to_str(eht_sig_differ)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:ESDiffer {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:ESDiffer \n
		Snippet: value: bool = driver.source.bb.wlnn.fblock.esDiffer.get(frameBlock = repcap.FrameBlock.Default) \n
		For EHT-160MHz/EHT-320MHz frames, activates different EHT-SIG fields for every 80 MHz channel. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: eht_sig_differ: 1| ON| 0| OFF"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:ESDiffer?')
		return Conversions.str_to_bool(response)
