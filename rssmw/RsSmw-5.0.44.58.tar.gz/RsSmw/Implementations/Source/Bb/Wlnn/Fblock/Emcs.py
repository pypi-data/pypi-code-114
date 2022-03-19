from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Emcs:
	"""Emcs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("emcs", core, parent)

	def set(self, eht_sig_mcs: enums.WlannFbMcs, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:EMCS \n
		Snippet: driver.source.bb.wlnn.fblock.emcs.set(eht_sig_mcs = enums.WlannFbMcs.MCS0, frameBlock = repcap.FrameBlock.Default) \n
		Sets the modulation coding scheme for modulation of the EHT-SIG bits. \n
			:param eht_sig_mcs: MCS0| MCS1| MCS3| MCS15
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.enum_scalar_to_str(eht_sig_mcs, enums.WlannFbMcs)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:EMCS {param}')

	# noinspection PyTypeChecker
	def get(self, frameBlock=repcap.FrameBlock.Default) -> enums.WlannFbMcs:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:EMCS \n
		Snippet: value: enums.WlannFbMcs = driver.source.bb.wlnn.fblock.emcs.get(frameBlock = repcap.FrameBlock.Default) \n
		Sets the modulation coding scheme for modulation of the EHT-SIG bits. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: eht_sig_mcs: MCS0| MCS1| MCS3| MCS15"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:EMCS?')
		return Conversions.str_to_scalar_enum(response, enums.WlannFbMcs)
