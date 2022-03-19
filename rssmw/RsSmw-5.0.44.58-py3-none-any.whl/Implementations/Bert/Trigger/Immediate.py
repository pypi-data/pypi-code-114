from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Immediate:
	"""Immediate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("immediate", core, parent)

	def set(self) -> None:
		"""SCPI: BERT:TRIGger:[IMMediate] \n
		Snippet: driver.bert.trigger.immediate.set() \n
		For method RsSmw.Bert.Trigger.mode|method RsSmw.Bler.Trigger.mode SING, triggers a single bit error rate or block error
		rate measurement. \n
		"""
		self._core.io.write(f'BERT:TRIGger:IMMediate')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: BERT:TRIGger:[IMMediate] \n
		Snippet: driver.bert.trigger.immediate.set_with_opc() \n
		For method RsSmw.Bert.Trigger.mode|method RsSmw.Bler.Trigger.mode SING, triggers a single bit error rate or block error
		rate measurement. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'BERT:TRIGger:IMMediate', opc_timeout_ms)
