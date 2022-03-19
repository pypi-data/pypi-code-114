from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Insert:
	"""Insert commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("insert", core, parent)

	def set(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:INSert \n
		Snippet: driver.source.bb.gbas.vdb.insert.set(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Inserts a new VDB before the selected one. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
		"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:INSert')

	def set_with_opc(self, vdbTransmitter=repcap.VdbTransmitter.Default, opc_timeout_ms: int = -1) -> None:
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:INSert \n
		Snippet: driver.source.bb.gbas.vdb.insert.set_with_opc(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Inserts a new VDB before the selected one. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:INSert', opc_timeout_ms)
