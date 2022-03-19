from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Insert:
	"""Insert commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("insert", core, parent)

	def set(self, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:INSert \n
		Snippet: driver.source.bb.nfc.cblock.insert.set(commandBlock = repcap.CommandBlock.Default) \n
		Inserts a default command block before the selected command block. The command block with this position must be existing,
		otherwise an error is returned. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:INSert')

	def set_with_opc(self, commandBlock=repcap.CommandBlock.Default, opc_timeout_ms: int = -1) -> None:
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:INSert \n
		Snippet: driver.source.bb.nfc.cblock.insert.set_with_opc(commandBlock = repcap.CommandBlock.Default) \n
		Inserts a default command block before the selected command block. The command block with this position must be existing,
		otherwise an error is returned. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:INSert', opc_timeout_ms)
