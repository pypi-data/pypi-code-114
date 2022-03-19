from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bdcm:
	"""Bdcm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bdcm", core, parent)

	def set(self, sig_bdcm: bool, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:BDCM \n
		Snippet: driver.source.bb.wlnn.fblock.bdcm.set(sig_bdcm = False, frameBlock = repcap.FrameBlock.Default) \n
		Enables the use of dual carrier modulation (DCM) in a signal B field. \n
			:param sig_bdcm: OFF| ON| 1| 0
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.bool_to_str(sig_bdcm)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:BDCM {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:BDCM \n
		Snippet: value: bool = driver.source.bb.wlnn.fblock.bdcm.get(frameBlock = repcap.FrameBlock.Default) \n
		Enables the use of dual carrier modulation (DCM) in a signal B field. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: sig_bdcm: OFF| ON| 1| 0"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:BDCM?')
		return Conversions.str_to_bool(response)
