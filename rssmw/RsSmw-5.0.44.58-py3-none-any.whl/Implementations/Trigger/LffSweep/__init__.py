from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LffSweep:
	"""LffSweep commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lffSweep", core, parent)

	@property
	def immediate(self):
		"""immediate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_immediate'):
			from .Immediate import Immediate
			self._immediate = Immediate(self._core, self._cmd_group)
		return self._immediate

	@property
	def source(self):
		"""source commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_source'):
			from .Source import Source
			self._source = Source(self._core, self._cmd_group)
		return self._source

	def set(self, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: TRIGger<HW>:LFFSweep \n
		Snippet: driver.trigger.lffSweep.set(inputIx = repcap.InputIx.Default) \n
			INTRO_CMD_HELP: Executes an LF frequency sweep in the following configuration: \n
			- method RsSmw.Trigger.LffSweep.Source.set SING
			- LFO:SWE:MODE AUTO \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
		"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'TRIGger{inputIx_cmd_val}:LFFSweep')

	def set_with_opc(self, inputIx=repcap.InputIx.Default, opc_timeout_ms: int = -1) -> None:
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		"""SCPI: TRIGger<HW>:LFFSweep \n
		Snippet: driver.trigger.lffSweep.set_with_opc(inputIx = repcap.InputIx.Default) \n
			INTRO_CMD_HELP: Executes an LF frequency sweep in the following configuration: \n
			- method RsSmw.Trigger.LffSweep.Source.set SING
			- LFO:SWE:MODE AUTO \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'TRIGger{inputIx_cmd_val}:LFFSweep', opc_timeout_ms)

	def clone(self) -> 'LffSweep':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LffSweep(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
