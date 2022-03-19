from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Resolve:
	"""Resolve commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("resolve", core, parent)

	def set(self, baseStation=repcap.BaseStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:DCONflict:RESolve \n
		Snippet: driver.source.bb.c2K.bstation.dconflict.resolve.set(baseStation = repcap.BaseStation.Default) \n
		The command resolves existing domain conflicts by modifying the Walsh codes of the affected channels. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
		"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:DCONflict:RESolve')

	def set_with_opc(self, baseStation=repcap.BaseStation.Default, opc_timeout_ms: int = -1) -> None:
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:DCONflict:RESolve \n
		Snippet: driver.source.bb.c2K.bstation.dconflict.resolve.set_with_opc(baseStation = repcap.BaseStation.Default) \n
		The command resolves existing domain conflicts by modifying the Walsh codes of the affected channels. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:DCONflict:RESolve', opc_timeout_ms)
