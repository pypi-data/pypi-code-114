from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Paste:
	"""Paste commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("paste", core, parent)

	def set(self, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:PASTe \n
		Snippet: driver.source.bb.nfc.cblock.paste.set(commandBlock = repcap.CommandBlock.Default) \n
		Pastes a command block (which was copied before) at the given position into the command sequence. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:PASTe')

	def set_with_opc(self, commandBlock=repcap.CommandBlock.Default, opc_timeout_ms: int = -1) -> None:
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:PASTe \n
		Snippet: driver.source.bb.nfc.cblock.paste.set_with_opc(commandBlock = repcap.CommandBlock.Default) \n
		Pastes a command block (which was copied before) at the given position into the command sequence. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:PASTe', opc_timeout_ms)
