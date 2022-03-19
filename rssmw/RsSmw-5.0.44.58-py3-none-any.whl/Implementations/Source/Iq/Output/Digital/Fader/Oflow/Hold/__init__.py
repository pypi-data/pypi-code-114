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

	def reset(self, digitalIq=repcap.DigitalIq.Default) -> None:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:FADer<CH>:OFLow:HOLD:RESet \n
		Snippet: driver.source.iq.output.digital.fader.oflow.hold.reset(digitalIq = repcap.DigitalIq.Default) \n
		Resets the overflow hold state and LED. \n
			:param digitalIq: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fader')
		"""
		digitalIq_cmd_val = self._cmd_group.get_repcap_cmd_value(digitalIq, repcap.DigitalIq)
		self._core.io.write(f'SOURce:IQ:OUTPut:DIGital:FADer{digitalIq_cmd_val}:OFLow:HOLD:RESet')

	def reset_with_opc(self, digitalIq=repcap.DigitalIq.Default, opc_timeout_ms: int = -1) -> None:
		digitalIq_cmd_val = self._cmd_group.get_repcap_cmd_value(digitalIq, repcap.DigitalIq)
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:FADer<CH>:OFLow:HOLD:RESet \n
		Snippet: driver.source.iq.output.digital.fader.oflow.hold.reset_with_opc(digitalIq = repcap.DigitalIq.Default) \n
		Resets the overflow hold state and LED. \n
		Same as reset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param digitalIq: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fader')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce:IQ:OUTPut:DIGital:FADer{digitalIq_cmd_val}:OFLow:HOLD:RESet', opc_timeout_ms)

	def clone(self) -> 'Hold':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Hold(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
