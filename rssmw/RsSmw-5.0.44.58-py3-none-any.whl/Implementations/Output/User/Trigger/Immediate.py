from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Immediate:
	"""Immediate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("immediate", core, parent)

	def set(self, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: OUTPut<HW>:USER<CH>:TRIGger:[IMMediate] \n
		Snippet: driver.output.user.trigger.immediate.set(userIx = repcap.UserIx.Default) \n
		Generates a short pulse signal and outputs it at the USER connector. This signal can serve as a common external trigger
		signal for triggering of several R&S SMW, see Example 'Triggering several R&S SMW instruments simultaneously'. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'OUTPut<HwInstance>:USER{userIx_cmd_val}:TRIGger:IMMediate')

	def set_with_opc(self, userIx=repcap.UserIx.Default, opc_timeout_ms: int = -1) -> None:
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		"""SCPI: OUTPut<HW>:USER<CH>:TRIGger:[IMMediate] \n
		Snippet: driver.output.user.trigger.immediate.set_with_opc(userIx = repcap.UserIx.Default) \n
		Generates a short pulse signal and outputs it at the USER connector. This signal can serve as a common external trigger
		signal for triggering of several R&S SMW, see Example 'Triggering several R&S SMW instruments simultaneously'. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'OUTPut<HwInstance>:USER{userIx_cmd_val}:TRIGger:IMMediate', opc_timeout_ms)
