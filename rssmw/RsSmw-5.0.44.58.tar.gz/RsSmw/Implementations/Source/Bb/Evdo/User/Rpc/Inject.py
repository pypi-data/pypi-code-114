from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Inject:
	"""Inject commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inject", core, parent)

	def set(self, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:RPC:INJect \n
		Snippet: driver.source.bb.evdo.user.rpc.inject.set(userIx = repcap.UserIx.Default) \n
		Enables sending of user defined Reverse Power Control (RPC) pattern at the end of the current RPC mode. The former RPC
		mode is restart at the end of the pattern transmission. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:RPC:INJect')

	def set_with_opc(self, userIx=repcap.UserIx.Default, opc_timeout_ms: int = -1) -> None:
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:RPC:INJect \n
		Snippet: driver.source.bb.evdo.user.rpc.inject.set_with_opc(userIx = repcap.UserIx.Default) \n
		Enables sending of user defined Reverse Power Control (RPC) pattern at the end of the current RPC mode. The former RPC
		mode is restart at the end of the pattern transmission. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:RPC:INJect', opc_timeout_ms)
