from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Paste:
	"""Paste commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("paste", core, parent)

	def set(self, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:PASTe \n
		Snippet: driver.source.bb.wlnn.fblock.paste.set(frameBlock = repcap.FrameBlock.Default) \n
		Pastes the selected frame block. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:PASTe')

	def set_with_opc(self, frameBlock=repcap.FrameBlock.Default, opc_timeout_ms: int = -1) -> None:
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:PASTe \n
		Snippet: driver.source.bb.wlnn.fblock.paste.set_with_opc(frameBlock = repcap.FrameBlock.Default) \n
		Pastes the selected frame block. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:PASTe', opc_timeout_ms)
