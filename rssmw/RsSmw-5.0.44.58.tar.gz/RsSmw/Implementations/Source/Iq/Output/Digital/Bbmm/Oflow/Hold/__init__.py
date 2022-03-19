from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hold:
	"""Hold commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hold", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def reset(self, iqConnector=repcap.IqConnector.Default) -> None:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:OFLow:HOLD:RESet \n
		Snippet: driver.source.iq.output.digital.bbmm.oflow.hold.reset(iqConnector = repcap.IqConnector.Default) \n
		Resets the overflow hold state and LED. \n
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
		"""
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		self._core.io.write(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:OFLow:HOLD:RESet')

	def reset_with_opc(self, iqConnector=repcap.IqConnector.Default, opc_timeout_ms: int = -1) -> None:
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:OFLow:HOLD:RESet \n
		Snippet: driver.source.iq.output.digital.bbmm.oflow.hold.reset_with_opc(iqConnector = repcap.IqConnector.Default) \n
		Resets the overflow hold state and LED. \n
		Same as reset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:OFLow:HOLD:RESet', opc_timeout_ms)

	def clone(self) -> 'Hold':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Hold(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
